import pandas as pd
import xarray as xr
import numpy as np
from datetime import timedelta
import os

# Environmental Copernius dataset
env_variables = [
    {
        "env_var": "thetao", # Để check trong file .nc của Copernius # Nhiệt độ nước biển #3D: lat, long, time, depth
        "prefix_file": "phy_thetao", #Để check tên file trong folder
        "column_name": "phy_thetao" # Để lưu tên column
    },
    {
        "env_var": "so", # Salinity #3D: lat, long, time, depth
        "prefix_file": "phy_so",
        "column_name": "phy_so"
    },
    {
        "env_var": "mlotst", # Mixed Layer # 2D: lat, long, time
        "prefix_file": "phy_mlotst",
        "column_name": "phy_mlotst"
    },
    {
        "env_var": "uo", # Velocity #3D: lat, long, time, depth
        "prefix_file": "phy_uo_vo",
        "column_name": "phy_uo"       
    },
    {
        "env_var": "vo", # Velocity #3D: lat, long, time, depth
        "prefix_file": "phy_uo_vo",
        "column_name": "phy_vo"         
    },
    {
        "env_var": "chl", # Nồng độ diệp lục và Phytoplankton #3D: lat, long, time, depth
        "prefix_file": "bio_chl_phyc",
        "column_name": "bio_chl"
    },
    {
        "env_var": "phyc", # Nồng độ diệp lục và Phytoplankton #3D: lat, long, time, depth
        "prefix_file": "bio_chl_phyc",
        "column_name": "bio_phyc"
    },
    {
        "env_var": "o2", # Dissoved Oxygen #3D: lat, long, time, depth
        "prefix_file": "bio_o2",
        "column_name": "bio_o2"
    }
]

 # Time variable
YEAR = 2022
time_range = {
    "year": YEAR,
    "start_datetime": f"{YEAR}-01-01",
    "end_datetime": f"{YEAR}-12-31"
    }

# Load dataset
gbif_df = pd.read_csv('./dataset/gbif_five_species_asia_cleaned.csv')
gbif_df_filtered = gbif_df[
    (gbif_df['year'] == YEAR)
] #at least year >2000
print(gbif_df_filtered.shape)

#%% Convert time to datetime
gbif_df_filtered['datetime'] = pd.to_datetime(
    gbif_df_filtered['eventDate'],
    format='mixed',
    utc=True
)
gbif_df_filtered['date'] = gbif_df_filtered['datetime'].dt.date
print(gbif_df_filtered.shape)


# Function join fish GBIF dataset to env from Copernius
def fish_join_env(fish_csv, env_var, year):
    """
    Join fish csv with environment from copernius
    """
    for item in env_var:
        file_dir = f"./dataset/env_copernius/env_{YEAR}"
        file_name = f"{item['prefix_file']}_{year}.nc"
        
        #Check file exist or not
        file_path = os.path.join(file_dir, file_name)

        if os.path.exists(file_path):
            # Load file
            ds = xr.open_dataset(file_path)

            print("Env file info:", ds.info)
            print("Env file info:", ds.data_vars)
            print("Env file info:", ds.coords)

            # 3. Vectorized Mapping (như đã học)
            lat_pts = xr.DataArray(fish_csv['decimalLatitude'], dims='index')
            lon_pts = xr.DataArray(fish_csv['decimalLongitude'], dims='index')
            time_pts = xr.DataArray(fish_csv['date'], dims='index')

            #Extract data
            extracted = ds.sel(latitude=lat_pts, longitude=lon_pts, time=time_pts, method='nearest')

            #Combine with dataframe
            #fish_csv[['thetao']] = extracted[['thetao']].to_dataframe()[['thetao']].values
            env_name = item['env_var']
            print("extracted env", extracted)
            fish_csv[env_name] = extracted[env_name].to_dataframe()[env_name].values
        else:
            print(f"{file_path} is not founded")

if __name__ == "__main__":
    print(f"Start join year {YEAR}")

    fish_join_env(gbif_df_filtered, env_variables, YEAR)

    print(gbif_df_filtered.shape)

    print(gbif_df_filtered.head(5))

    gbif_df_filtered.to_csv(f'./dataset/fish_env_{YEAR}.csv')

    print("Done")

