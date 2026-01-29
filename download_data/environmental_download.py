import copernicusmarine

# Lon: 27.24 → 141.57
# Lat: -10.77 → 37.74
# Time range:
# 2014-05-21 → 2026-01-03
#         # Biogeochemical
#         "chl",       # Chlorophyll-a
#         "o2",        # Dissolved oxygen

copernicusmarine.subset(
    dataset_id="cmems_mod_glo_phy_my_0.083deg_P1D-m",
    variables = [
        # Physical
        "thetao",    # Sea surface temperature
        "mlotst",    # Mixed layer depth
        "uo",        # Zonal current
        "vo",        # Meridional current
    ],
    minimum_longitude=27.24,
    maximum_longitude=141.57,
    minimum_latitude=-10.77,
    maximum_latitude=37.74,

    minimum_depth=0.5,
    maximum_depth=1.0,

    start_datetime="2023-01-01",
    end_datetime="2023-12-31",
    output_filename="env_2023.nc"
)

print("Physical data env_2023 downloaded!")



