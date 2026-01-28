from pygbif import occurrences
from pygbif import species
import pandas as pd

# Ref: https://techdocs.gbif.org/en/data-use/download-formats 

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


res = occurrences.search(
    scientificName=["Thunnus albacares","Katsuwonus pelamis"],
    hasCoordinate=True,
    limit=1000
)

df = pd.DataFrame(res['results'])
# Data exploration
df[['decimalLatitude','decimalLongitude','eventDate']]

# Save to CSV
df.to_csv('dataset/thunnus_albacares_gbif.csv', index=False)
print("Data saved to dataset/thunnus_albacares_gbif.csv")

