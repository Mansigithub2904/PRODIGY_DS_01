import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/cleaned_population.csv")

# Get latest year data
latest_year = df["Year"].max()
latest_df = df[df["Year"] == latest_year]

# Top 10 countries
top10 = latest_df.sort_values(by="Population", ascending=False).head(10)

# Plot
plt.figure(figsize=(12,7))
bars = plt.bar(top10["Country"], top10["Population"])

# Titles and labels
plt.title(f"Top 10 Most Populated Countries ({latest_year})", fontsize=16, fontweight='bold')
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population", fontsize=12)

# Rotate labels
plt.xticks(rotation=45, ha='right')

# Grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Format numbers
plt.ticklabel_format(style='plain', axis='y')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{int(height):,}', ha='center', va='bottom', fontsize=9)

# Highlight top country (first bar)
bars[0].set_edgecolor('black')
bars[0].set_linewidth(2)

# Layout fix
plt.tight_layout()

# Save & show
plt.savefig("outputs/barchart.png")
print("✅ bar chart created!")
plt.show()


