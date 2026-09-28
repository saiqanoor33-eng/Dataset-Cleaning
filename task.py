import pandas as pd

df = pd.read_csv("movies.csv")

print("===== BEFORE CLEANING =====")
print("Rows:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

df = df.drop_duplicates()

df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df["title"] = df["title"].fillna("Unknown")
df["genres"] = df["genres"].fillna("Unknown")
df["year"] = df["year"].fillna(df["year"].median())
df["rating"] = df["rating"].fillna(df["rating"].median())

df = df[(df["year"] >= 1900) & (df["year"] <= 2026)]
df = df[(df["rating"] >= 0) & (df["rating"] <= 10)]

df["year"] = df["year"].astype(int)
df["rating"] = df["rating"].astype(float)

df.to_csv("movies_cleaned.csv", index=False)

print("\n===== AFTER CLEANING =====")
print("Rows:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nCleaned dataset saved successfully!")