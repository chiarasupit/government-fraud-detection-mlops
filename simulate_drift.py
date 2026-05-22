import pandas as pd
import numpy as np
import os

# Create writable data folder
os.makedirs(
    "/Users/frangkysupit/Downloads/data",
    exist_ok=True
)

# Load original dataset
df = pd.read_csv(
    "/Users/frangkysupit/Downloads/creditcard.csv"
)

print("Generating 12 months of simulated drifted data...\n")

# Create 12 months of modified datasets
for month in range(1, 13):

    modified = df.copy()

    # Random drift factor each month
    random_change = np.random.uniform(0.95, 1.15)

    # Apply drift to transaction amounts
    modified["Amount"] = (
        modified["Amount"] * random_change
    )

    # Save modified monthly dataset
    save_path = (
        f"/Users/frangkysupit/Downloads/data/month_{month:02}.csv"
    )

    modified.to_csv(
        save_path,
        index=False
    )

    print(
        f"Month {month:02} dataset created "
        f"(Drift Factor: {random_change:.3f})"
    )

print("\nAll monthly datasets generated successfully.")