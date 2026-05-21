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

# Create 12 months of drifted datasets
for month in range(1, 13):

    modified = df.copy()

    # Simulate data drift
    drift_factor = 1 + (month * 0.02)

    modified["Amount"] = (
        modified["Amount"] * drift_factor
    )

    # Save modified dataset
    modified.to_csv(
        f"/Users/frangkysupit/Downloads/data/month_{month:02}.csv",
        index=False
    )

    print(f"Month {month} dataset created.")