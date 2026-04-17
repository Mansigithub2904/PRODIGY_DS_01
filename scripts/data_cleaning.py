import pandas as pd

# Load dataset (after downloading manually)
df = pd.read_csv("population.csv", skiprows=4)

# Drop unnecessary columns
df = df.drop(columns=[
    "Country Code",
    "Indicator Name",
    "Indicator Code"
])

# Rename column
df = df.rename(columns={"Country Name": "Country"})

# Convert wide → long format
df = df.melt(id_vars=["Country"], 
             var_name="Year", 
             value_name="Population")

# Convert data types
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Population"] = pd.to_numeric(df["Population"], errors="coerce")

# Remove missing values
df = df.dropna()

# Filter recent data (optional but recommended)
df = df[df["Year"] >= 2000]

# Save cleaned data
df.to_csv("data/cleaned_population.csv", index=False)

print("✅ Data cleaned and saved!")