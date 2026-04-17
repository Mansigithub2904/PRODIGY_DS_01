import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load data
df = pd.read_csv("data/cleaned_population.csv")

# Calculate statistics
mean_val = df["Population"].mean()
median_val = df["Population"].median()

# Plot histogram
plt.figure(figsize=(10,6))

plt.hist(df["Population"], bins=30, alpha=0.7)

# Add mean & median lines
plt.axvline(mean_val, linestyle='dashed', linewidth=2, label=f"Mean: {int(mean_val)}")
plt.axvline(median_val, linestyle='solid', linewidth=2, label=f"Median: {int(median_val)}")

# Titles and labels
plt.title("Population Distribution", fontsize=16, fontweight='bold')
plt.xlabel("Population", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Improve readability
plt.ticklabel_format(style='plain', axis='x')
plt.legend()

# Save and show
plt.tight_layout()
plt.savefig("outputs/histogram.png")
print("✅ histogram created!")
plt.show()
