from pygbif import occurrences
from pygbif import species
import pandas as pd

# Ref: https://techdocs.gbif.org/en/data-use/download-formats 
# Crawl Scientific Names Done Separately
# Not yet download by Genus. By Genus -> Get taxonKey -> Download Occurrences

target_scientificName = [
    "Thunnus albacares", #Cá ngừ vây vàng - Yellowfin Tuna
    "Katsuwonus pelamis", #Cá ngừ vằn - Skipjack Tuna
    "Scomberomorus commerson", #Cá thu đao/ cá thu ngàng - Spanish mackerel
    "Trichiurus lepturus", #Cá hố - Largehead hairtail
    "Pampus argenteus", #Cá chim - Pomfret
]

target_genus = [
    "Decapterus", #Cá nục - Round scad
    "Sardinella", #Cá trích - Sardine/Herring
    "Engraulis", #Cá cơm - Anchovy
    "Epinephelus", #Cá mú - Groupers
    "Lutjanus", #Cá hồng - Sanppers
]

# res = occurrences.search(
#     scientificName="Pampus argenteus",
#     hasCoordinate=True,
#     continent="ASIA", # Asia
#     limit=1000
# )

for i in target_scientificName:
    res_i = occurrences.search(
        scientificName=i,
        hasCoordinate=True,
        continent="ASIA", # Asia
        limit=1000
    )
    df = pd.DataFrame(res_i['results'])
    # Data exploration
    print(df[['scientificName','decimalLatitude','decimalLongitude','eventDate']])

    # Save to CSV
    name_file = i.replace(" ", "_").lower()
    df.to_csv(f'dataset/gbif_asia/gbif_asia_{name_file}.csv', index=False)
    print(f"Data saved to dataset/gbif_asia/gbif_asia_{name_file}.csv")



