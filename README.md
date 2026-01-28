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

Spatial and temporal gradients of key oceanographic variables:
- Temperature (Nhiệt độ bề mặt):
- Mixed layer depth (Độ sâu lớp hỗn hợp):
- Chlorophyll concentraion (Nồng độ diệp lục):
- Normalized chlorophyll (Diệp lục chuẩn hóa):

Besides, there are some other variables:
- Salinity (Độ mặn) (Optional):
- Phytoplankton concentration (Nồng độ thực vật phù du):
- Dissolved oxygen (Oxy hòa tan) 

Data types: NetDCF file
Source: Corpenius link.

1.2 Fishing data
- Global Fishing Watch: [Fleet + fish](https://globalfishingwatch.org/data-download/datasets/public-fishing-effort)
- FAO: [Fish distribution source link](https://www.fao.org/fishery/en/collection/global_production?lang=en) Lat, long and the type of fish, missing date
- OBIS: Link. 
- GBIF: Link. Lat, long, date and the type of fish. Presence/absence type of fish
After crawling data from these sources, I filtered date, and lat long and preprocessing to get environmental data 

## II. Solutions
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
