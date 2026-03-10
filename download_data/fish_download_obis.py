#%%
from __future__ import annotations

import pandas as pd
from pyobis import occurrences


def build_bbox_wkt(west: float, south: float, east: float, north: float) -> str:
    return (
        f"POLYGON(({west} {south}, {east} {south}, {east} {north}, "
        f"{west} {north}, {west} {south}))"
    )


def fetch_obis_occurrences(
    genus: str,
    geometry_wkt: str,
    startdate: str | None = None,
    enddate: str | None = None,
    page_size: int = 5000,
    max_records: int | None = None,
) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    offset = 0

    while True:
        search = occurrences.search(
            scientificname=genus,
            geometry=geometry_wkt,
            startdate=startdate,
            enddate=enddate,
            size=page_size,
            offset=offset,
        )
        search.execute()
        df = search.to_pandas()

        if df.empty:
            break

        frames.append(df)

        if len(df) < page_size:
            break

        offset += page_size
        if max_records is not None and offset >= max_records:
            break

    if frames:
        return pd.concat(frames, ignore_index=True)

    return pd.DataFrame()


def select_output_columns(df: pd.DataFrame, genus: str, common_name_vi: str) -> pd.DataFrame:
    column_map = {
        "scientificName": "scientificName",
        "decimalLatitude": "decimalLatitude",
        "decimalLongitude": "decimalLongitude",
        "eventDate": "eventDate",
    }

    available = [col for col in column_map if col in df.columns]
    result = df[available].copy() if available else df.copy()

    if "scientificName" not in result.columns and "scientificname" in df.columns:
        result["scientificName"] = df["scientificname"]

    result["genus"] = genus
    result["common_name_vi"] = common_name_vi

    desired_cols = [
        "genus",
        "common_name_vi",
        "scientificName",
        "decimalLatitude",
        "decimalLongitude",
        "eventDate",
    ]
    for col in desired_cols:
        if col not in result.columns:
            result[col] = pd.NA

    return result[desired_cols]


def main() -> None:
    north = 37.74
    west = 27.24
    east = 141.57
    south = -10.77
    geometry_wkt = build_bbox_wkt(west, south, east, north)

    genera = {
        "Clupea": "Cá Trích",
        "Scomber": "Cá Thu",
        "Thunnus": "Cá Ngừ",
    }

    all_frames: list[pd.DataFrame] = []

    for genus, common_name in genera.items():
        print(f"--- Đang tải dữ liệu OBIS cho chi: {genus} ({common_name}) ---")
        raw_df = fetch_obis_occurrences(
            genus=genus,
            geometry_wkt=geometry_wkt,
            startdate="2020-01-01",
            enddate="2025-12-31",
            page_size=5000,
        )

        if raw_df.empty:
            print(f"Không có dữ liệu cho {genus}.")
            continue

        cleaned = select_output_columns(raw_df, genus, common_name)
        all_frames.append(cleaned)

    if not all_frames:
        print("Không tìm thấy dữ liệu nào từ OBIS.")
        return

    result = pd.concat(all_frames, ignore_index=True)
    result = result.dropna(subset=["decimalLatitude", "decimalLongitude", "eventDate"])

    output_path = "obis_occurrence_asia_clupea_scomber_thunnus.csv"
    result.to_csv(output_path, index=False)
    print(f"Đã lưu {len(result)} bản ghi vào: {output_path}")


if __name__ == "__main__":
    main()

# %%
