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

| Biến (Tiếng Anh / Tiếng Việt) | Tên biến kỹ thuật | Đơn vị | Mô tả | Dataset ID |
|---|---|---|---|---|
| 1. Sea Water Potential Temperature (Nhiệt độ nước biển) | thetao | $^\circ C$ | Quyết định vùng nhiệt độ tối ưu và khả năng sinh tồn của cá. | GLOBAL_ANALYSISFORECAST_PHY_001_024 |
| 2. Sea Water Salinity (Độ mặn) | so | $10^{-3}$ (psu) | Quan trọng cho cá vùng cửa sông và các loài nhạy cảm với áp suất thẩm thấu. | GLOBAL_ANALYSISFORECAST_PHY_001_024 |
| 3. Eastward Velocity (Dòng chảy hướng Đông) | uo | $m/s$ | Thành phần vận tốc dòng chảy theo trục X. | GLOBAL_ANALYSISFORECAST_PHY_001_024 |
| 4. Northward Velocity (Dòng chảy hướng Bắc) | vo | $m/s$ | Thành phần vận tốc dòng chảy theo trục Y. | GLOBAL_ANALYSISFORECAST_PHY_001_024 |
| 5. Mixed Layer Thickness (Độ dày tầng hỗn hợp) | mlotst | $m$ | Độ sâu mà tại đó các đặc tính lý học được trộn lẫn đồng nhất. | GLOBAL_ANALYSISFORECAST_PHY_001_024 |
| 6. Mass Concentration of Chlorophyll-a (Nồng độ Diệp lục-a) | chl | $mg/m^3$ | Chỉ thị cho năng suất sinh học và sự hiện diện của thức ăn (phù du). | GLOBAL_ANALYSISFORECAST_BIO_001_028 |
| 7. Mole Concentration of Dissolved Oxygen (Oxy hòa tan) | o2 | $mmol/m^3$ | Nồng độ oxy trong nước; giới hạn vùng cư trú của các loài. | GLOBAL_ANALYSISFORECAST_BIO_001_028 |
| 8. Net Primary Production of Carbon (Sản lượng sơ cấp thuần) | nppv | $mg/m^3/day$ | Tốc độ tạo ra vật chất hữu cơ, phản ánh độ giàu có của ngư trường. | GLOBAL_ANALYSISFORECAST_BIO_001_028 |
| 9. Sea Water pH (Độ pH nước biển) | ph | $1$ | Chỉ số axit/kiềm, ảnh hưởng đến sự phát triển vỏ cá và rạn san hô. | GLOBAL_ANALYSISFORECAST_BIO_001_028 |
| 10. Mole Concentration of Nitrate (Nồng độ Nitrate) | no3 | $mmol/m^3$ | Muối dinh dưỡng chính thúc đẩy sự phát triển của chuỗi thức ăn. | GLOBAL_ANALYSISFORECAST_BIO_001_028 |
| 11. Sea Surface Height (Mực nước biển) | zos | $m$ | Giúp xác định các vùng nước trồi (upwelling) nơi thường có nhiều cá. | GLOBAL_ANALYSISFORECAST_PHY_001_024 |

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
