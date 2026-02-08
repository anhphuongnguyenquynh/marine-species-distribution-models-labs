# Marine Species Distribution Modelling

## Objectives
The purpose of this notebook is to build a fishmap - an ocean marine species distribution. This is a type of Spatio-Temporal Prediction. 

To formulate the problem:
    y(s,t) ~ f(environment(s,t), space, time)
with:
- s: location (lat, lon, depth)
- t: time (month, season, year)
- 𝑌: prediction. y could be: 1/ Presence / absence 2/ Abundance / density 3/ Hotspot probability

## I. Collect data

1.1 Environmental/ Oceanographic

|  | **Product line** | **dataset_id** | **Spatial resolution** | **Lat-Long** | **Time** | **Environmental variables (En)** | **Environmental variables (VI)** | **Shorten variables** |
|---|---|---|---|---|---|---|---|---|
| **1** | **GLOBAL_ANALYSISFORECAST_PHY_001_024** |  | 1/12 degree 0.083 | Global : 180°W-180°E ; 89°S – 90°N | daily (10/2016 - now) |  |  |  |
| 1.1 | https://documentation.marine.copernicus.eu/PUM/CMEMS-GLO-PUM-001-024.pdf | cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m |  |  |  | Sea Surface Temperature SST | Nhiệt độ nước biển | thetao |
| 1.2 |  | cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m |  |  |  | Salinity | Độ mặn | so (psu) |
| 1.3 |  | cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m |  |  |  | Eastward Velocity | Dòng chảy hướng Đông - trục X | uo (m/s) |
| 1.4 |  | ^ |  |  |  | Northward Velocity | Dòng chảy hướng Bắc - trục Y | vo (m/s) |
| 1.5 |  | cmems_mod_glo_phy_anfc_0.083deg_P1D-m |  |  |  | Mixed Layer Depth | Độ dày tầng hỗn hợp | mlotst (m) |
| **2** | **GLOBAL_ANALYSISFORECAST_BIO_001_028** |  | 1/4 0.25 | Global ocean (180°W-180°E ; 90°S – 90°N) | daily |  |  |  |
| 2.1 | https://documentation.marine.copernicus.eu/PUM/CMEMS-GLO-PUM-001-028.pdf | cmems_mod_glo_bgc-pft_anfc_0.25deg_P1D-m |  |  |  | Chlorophyll-a | Nồng độ diệp lục - a | chl (mg/m^3) |
| 2.2 |  | cmems_mod_glo_bgc-bio_anfc_0.25deg_P1D-m |  |  |  | Dissolved Oxygen | Oxy hòa tan | o2 (mmol/m^3) |
| 2.3 |  | ^ |  |  |  | Total Primary Production of Phyto | Lượng carbon hữu cơ được tạo ra bởi thực vật phù du (phytoplankton) | nppv (mg/m^3) |

Note: Nhiều paper: SST + Chl-a + MLD = core predictors

Data types: NetDCF file
Source: Corpenius link.

1.2 Fishing data
- Global Fishing Watch: [Fleet + fish](https://globalfishingwatch.org/data-download/datasets/public-fishing-effort)
- FAO: [Fish distribution source link](https://www.fao.org/fishery/en/collection/global_production?lang=en) Lat, long and the type of fish, missing date
- OBIS: Link. 
- GBIF: Link. Lat, long, date and the type of fish. Presence/absence type of fish
After crawling data from these sources, I filtered date, and lat long and preprocessing to get environmental data 

## II. Data Preprocessing
- Problem: presence-only. Đây là vấn đề khá phổ biến đối với bài toán species distribution modelling. Không giống binary classification (dữ liệu có được là Có/Không rồi predict), mình chỉ có thể có dữ liệu có đối với 1 vài địa điểm, và không có nghĩa tất cả các điểm còn lại là không có, và số lượng các điểm có khá ít. Để giải quyết bài toán này, có 1 vài cách:
+ Thêm dữ liệu 

## III. Solutions
There are three main solutions to solve this problem:
| **#** | **Method** | **Model** | **Description** | **Data Input** | **Evaluation metrics** | **Results** | **Link** | **Note** |
|---|---|---|---|---|---|---|---|---|
| **1** | **Statistical** |  |  |  |  |  |  |  |
|  |  | Generalized Linear Model |  |  |  |  |  |  |
| **2** | **Machine Learning** |  |  |  |  |  |  |  |
| **3** | **Deep Learning** |  |  |  |  |  |  |  |
|  |  | Multi Layer Perceptron |  |  |  |  |  |  |

## III. Evaluation


## References
