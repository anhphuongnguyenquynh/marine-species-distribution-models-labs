#%% Import Libraries
import pandas as pd
import xarray as xr
import numpy as np
from datetime import timedelta

#%% Load data
gbif_df = pd.read_csv('../dataset/gbif_five_species_asia_cleaned.csv')
gbif_df = gbif_df[gbif_df['year'] >= 2000]
print(gbif_df.shape)
print(gbif_df.head(5))

#%% Import Libraries
gbif_df['eventDate'] = pd.to_datetime(gbif_df['eventDate'], errors='coerce')
#gbif_df = gbif_df.dropna(subset=['eventDate', 'decimalLatitude', 'decimalLongitude'])
print(gbif_df.shape)

#%% Normalize lat long
gbif_df['decimalLatitude'] = pd.to_numeric(gbif_df['decimalLatitude'])
gbif_df['decimalLongitude'] = pd.to_numeric(gbif_df['decimalLongitude'])

## Loại bỏ các điểm lỗi (tọa độ 0,0 thường là lỗi hệ thống)
gbif_df = gbif_df[(gbif_df['decimalLatitude'] != 0) & (gbif_df['decimalLongitude'] != 0)]

## Normalize longtitude (-180 to 180 -> 0 to 360 because Copernicus uses 0-360)
def normalize_lon(lon):
    return lon + 360 if lon < 0 else lon

gbif_df["lon_norm"] = gbif_df["decimalLongitude"].apply(normalize_lon)
gbif_df["lat_norm"] = gbif_df["decimalLatitude"]


print(gbif_df.head(5))


#%% Computing bounding box and time range

BUFFER_DEG = 1.0  # ~100km buffer

min_lon = gbif_df["lon_norm"].min() - BUFFER_DEG
max_lon = gbif_df["lon_norm"].max() + BUFFER_DEG
min_lat = gbif_df["lat_norm"].min() - BUFFER_DEG
max_lat = gbif_df["lat_norm"].max() + BUFFER_DEG

print("Bounding box:")
print(f"Lon: {min_lon:.2f} → {max_lon:.2f}")
print(f"Lat: {min_lat:.2f} → {max_lat:.2f}")

## Compute time range
TIME_BUFFER_DAYS = 2

start_date = gbif_df["eventDate"].min() - timedelta(days=TIME_BUFFER_DAYS)
end_date   = gbif_df["eventDate"].max() + timedelta(days=TIME_BUFFER_DAYS)

start_datetime = start_date.strftime("%Y-%m-%d")
end_datetime   = end_date.strftime("%Y-%m-%d")

print("Time range:")
print(start_datetime, "→", end_datetime)

#%% Set year variable
YEAR = 2023

#%% Extract environmental data
nc_path = f'../dataset/env_copernius/env_{YEAR}.nc'
ds_env = xr.open_dataset(nc_path)

variables = ["thetao", "mlotst", "uo", "vo"]
ds_subset = ds_env[variables]

print(ds_subset)

#%% Remove depth dimension if exists
ds_subset = ds_env[variables].isel(depth=0, drop=True)

print(ds_subset)


# %% Mapping environmental data to GBIF records
def get_nc_values(row, ds):
    try:
        point_data = ds_subset.sel(
            time=row['eventDate'],
            longitude=row['lon_norm'],
            latitude=row['lat_norm'],
            method='nearest'
        )
        return pd.Series({
            'sea_surface_temperature': point_data['thetao'].values.item(),
            'mixed_layer_depth': point_data['mlotst'].values.item(),
            'zonal_current': point_data['uo'].values.item(),
            'meridional_current': point_data['vo'].values.item()
        })
    except Exception as e:
        print(f"Error retrieving data for row {row.name}: {e}")
        return pd.Series({
            'sea_surface_temperature': np.nan,
            'mixed_layer_depth': np.nan,
            'zonal_current': np.nan,
            'meridional_current': np.nan
        })

# %% Update table and merge data
## Filter gbif_df year = YEAR
gbif_df = gbif_df[gbif_df['year'] == YEAR]
print(f"Number of GBIF records for year {YEAR}: {len(gbif_df)}")

## Merge environmental data
env_data = gbif_df.apply(get_nc_values, axis=1, ds=ds_subset)
merge_df = pd.concat([gbif_df.reset_index(drop=True), env_data], axis=1)
print(merge_df.shape)
print(merge_df.head(5))

# %% export to csv
file_name = f'fish_env_{YEAR}.csv'
merge_df.to_csv(f'../dataset/fish_env_gbif_copernius/{file_name}', index=False)
print(f"Merge data saved to: {file_name}")

# %%
