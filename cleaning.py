# ==============================
# REAL ESTATE PRICE ANALYSIS PROJECT
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ==============================
# LOAD DATA
# ==============================

df = pd.read_csv("Bengaluru_House_Data.csv")

print("Initial Shape:", df.shape)

# ==============================
# DATA CLEANING
# ==============================

# Drop unnecessary column if exists
if "area_type" in df.columns:
    df = df.drop("area_type", axis=1)

# Drop important nulls
df = df.dropna(subset=["location", "size", "total_sqft", "bath", "price"])

# Extract BHK
df["bhk"] = df["size"].apply(lambda x: int(x.split(" ")[0]))
df = df.drop("size", axis=1)

# Convert total_sqft

def convert_sqft(x):
    if "-" in str(x):
        tokens = x.split("-")
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None

df["total_sqft"] = df["total_sqft"].apply(convert_sqft)
df = df.dropna(subset=["total_sqft"])

# Clean location
df["location"] = df["location"].apply(lambda x: x.strip())

location_counts = df["location"].value_counts()
rare_locations = location_counts[location_counts <= 10]

df["location"] = df["location"].apply(
    lambda x: "other" if x in rare_locations else x
)
if "society" in df.columns:
    df = df.drop("society", axis=1)

# Remove unrealistic sqft per bhk
df = df[df["total_sqft"] / df["bhk"] >= 300]

# Remove extreme bath values
df = df[df["bath"] <= df["bhk"] + 2]

print("After Cleaning Shape:", df.shape)

# ==============================
# FEATURE ENGINEERING
# ==============================

# Price per sqft
df["price_per_sqft"] = (df["price"] * 100000) / df["total_sqft"]

# Price Category
df["price_category"] = pd.cut(
    df["price"],
    bins=[0, 50, 100, 200, 1000],
    labels=["Budget", "Mid-Range", "Premium", "Luxury"]
)

# ==============================
# RENTAL YIELD ESTIMATION
# ==============================

df["estimated_monthly_rent"] = df["price"] * 100000 * 0.005
df["annual_rent"] = df["estimated_monthly_rent"] * 12
df["rental_yield"] = (df["annual_rent"] / (df["price"] * 100000)) * 100

# ==============================
# ROI SIMULATION (5 YEARS)
# ==============================

growth_rate = 0.06
years = 5

df["future_price_5yr"] = df["price"] * ((1 + growth_rate) ** years)
df["roi_5yr"] = ((df["future_price_5yr"] - df["price"]) / df["price"]) * 100

# ==============================
# INVESTMENT SCORE
# ==============================

scaler = MinMaxScaler()

df["sqft_scaled"] = scaler.fit_transform(df[["total_sqft"]])
df["price_sqft_scaled"] = scaler.fit_transform(df[["price_per_sqft"]])

df["investment_score"] = (
    df["sqft_scaled"] * 0.6 +
    (1 - df["price_sqft_scaled"]) * 0.4
)

# ==============================
# LOCATION LEVEL ANALYSIS
# ==============================

location_summary = df.groupby("location").agg({
    "price": "mean",
    "total_sqft": "mean",
    "price_per_sqft": "mean",
    "rental_yield": "mean",
    "roi_5yr": "mean",
    "investment_score": "mean"
}).sort_values(by="investment_score", ascending=False)

print("\nTop Investment Locations:")
print(location_summary.head(10))

# ==============================
# MACHINE LEARNING MODEL
# ==============================

X = df[["total_sqft", "bath", "bhk", "price_per_sqft"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = r2_score(y_test, y_pred)

print("\nModel R2 Score:", accuracy)

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", ascending=False)

print("\nFeature Importance:")
print(importance)

# ==============================
# VISUALIZATIONS
# ==============================

plt.figure(figsize=(8,5))
plt.hist(df["price"], bins=30)
plt.title("Price Distribution")
plt.xlabel("Price (Lakhs)")
plt.ylabel("Frequency")vvvvvvvvvvvvvvvvvvvv
plt.show()

plt.figure(figsize=(10,5))
df.groupby("location")["price_per_sqft"].mean().sort_values().tail(10).plot(kind="bar")
plt.title("Top 10 Expensive Locations (Price per Sqft)")
plt.show()

# ==============================
# SAVE CLEAN DATA
# ==============================

df.to_csv("Cleaned_Bengaluru_Investment_Data.csv", index=False)

print("\nProject Completed Successfully.")
