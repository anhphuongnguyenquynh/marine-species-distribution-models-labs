import copernicusmarine
import os

#Document: https://documentation.marine.copernicus.eu/PUM/CMEMS-GLO-PUM-001-024.pdf 
#Document: https://documentation.marine.copernicus.eu/PUM/CMEMS-GLO-PUM-001-028.pdf

# Environmental datasets to download from Copernicus Marine Service
marine_datasets = [
    {
        "dataset_id": "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m", 
        "variables": ["thetao"], # Nhiệt độ nước biển #3D: lat, long, time, depth
        "prefix_file": "phy_thetao"
    },
    {
        "dataset_id": "cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m", 
        "variables": ["so"], # Salinity #3D: lat, long, time, depth
        "prefix_file": "phy_so"
    },
    {
        "dataset_id": "cmems_mod_glo_phy_anfc_0.083deg_P1D-m", 
        "variables": ["mlotst"], # Mixed Layer # 2D: lat, long, time
        "prefix_file": "phy_mlotst"
    },
    {
        "dataset_id": "cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m", 
        "variables": ["uo", "vo"], # Velocity #3D: lat, long, time, depth
        "prefix_file": "phy_uo_vo"
    },
    {
        "dataset_id": "cmems_mod_glo_bgc-pft_anfc_0.25deg_P1D-m", 
        "variables": ["chl", "phyc"], # Nồng độ diệp lục và Phytoplankton #3D: lat, long, time, depth
        "prefix_file": "bio_chl_phyc"
    },
    {
        "dataset_id": "cmems_mod_glo_bgc-bio_anfc_0.25deg_P1D-m", 
        "variables": ["o2"], # Dissoved Oxygen #3D: lat, long, time, depth
        "prefix_file": "bio_o2"
    }
]

 # Time variable
YEAR = 2022
time_range = {
    "year": YEAR,
    "start_datetime": f"{YEAR}-01-01",
    "end_datetime": f"{YEAR}-12-31"
    }

# Function to download environmental variables from Copernius
def download_env_copernius(datasets, time):
    """
    Download .nc files about environmental variables from Copernicus Marine Service.
    """
    for item in datasets:
        file_dir = f"./dataset/env_copernius/env_{time['year']}"
        file_name = f"{item['prefix_file']}_{time['year']}.nc"
        
        #Check file exist or not
        file_path = os.path.join(file_dir, file_name)
        if os.path.exists(file_path):
            print(f"{file_name} is already downloaded")
        
        else:
            print(f"\nDownloading {file_name} from dataset: {item['dataset_id']}")
            try:
                copernicusmarine.subset(
                dataset_id=item['dataset_id'],
                variables=item['variables'],

                minimum_longitude=27.24,
                maximum_longitude=141.57,
                minimum_latitude=-10.77,
                maximum_latitude=37.74,

                minimum_depth=0.0,
                maximum_depth=0.5,

                start_datetime=time['start_datetime'],
                end_datetime=time['end_datetime'],

                output_directory=file_dir,
                output_filename=file_name )
                
                print(f"==> Download completed: {file_name}")
            
            except Exception as e:
                print(f"Oh nooo! Error when downloading {file_name}: {e}")

if __name__ == "__main__":
    download_env_copernius(marine_datasets, time_range)

    print("Download all files completed")

