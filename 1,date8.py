import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/dataset.csv")

# Separate data based on target
no_disease = df[df["target"] == 0]["age"]
disease = df[df["target"] == 1]["age"]

# Plot histogram
plt.figure(figsize=(8, 5))

plt.hist(no_disease, bins=15, alpha=0.6, label="No Disease (0)")
plt.hist(disease, bins=15, alpha=0.6, label="Disease (1)")

# Labels and title
plt.title("Age Distribution by Heart Disease Status")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.legend()

plt.show()