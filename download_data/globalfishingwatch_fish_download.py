from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

START_DATE = "2023-01-01"
END_DATE   = "2023-12-31"

GEARS = [
    "TUNA_PURSE_SEINES",
    "SET_LONGLINES"
]

query = f"""
SELECT
  date,
  lat,
  lon,
  gear_type,
  fishing_hours
FROM `global-fishing-watch.global_footprint_of_fisheries.fishing_effort`
WHERE
  date BETWEEN "{START_DATE}" AND "{END_DATE}"
  AND region = "EEZ_VNM"
  AND gear_type IN UNNEST({GEARS})
"""

df = client.query(query).to_dataframe()
print(df.head())
df.to_csv("fishing_effort_vnm_2023.csv", index=False)
print("Data saved to fishing_effort_vnm_2023.csv")