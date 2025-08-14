# preprocessing/step1_preprocess.py
print("🚀 Script started")
import pandas as pd

# Load the datasets
print("📂 Loading datasets...")
crop_df = pd.read_csv("Crop_recommendation.csv")
soil_df = pd.read_csv("soil.csv")
production_df = pd.read_excel("India Agriculture Crop Production - Copy.xlsx")
print("✅ Files loaded successfully")

# Clean column names
soil_df.columns = soil_df.columns.str.strip()
soil_df["District"] = soil_df["District"].str.upper().str.strip()
production_df["District"] = production_df["District"].str.upper().str.strip()
print("🧹 Cleaned all datasets")

# Clean and filter production data
production_df = production_df.dropna(subset=["District", "Crop", "Year", "Production", "Yield"])
yield_threshold = production_df["Yield"].median()
production_df["Success"] = production_df["Yield"].apply(lambda x: 1 if x >= yield_threshold else 0)

# Merge with soil data
merged_df = pd.merge(production_df, soil_df, on="District", how="left")
merged_df_final = merged_df.dropna(subset=["Zn %", "Fe%", "Cu %", "Mn %", "B %", "S %"])
print("📁 Saved merged dataset")
# Save processed data
crop_df.to_csv("processed_crop_data.csv", index=False)
merged_df_final.to_csv("processed_production_data.csv", index=False)

print("✅ Preprocessing complete. Cleaned datasets saved in /data.")
