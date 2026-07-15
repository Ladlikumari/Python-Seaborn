import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/dataset.csv")

# Count of chest pain type by target
count = pd.crosstab(df["cp"], df["target"])

count.plot(kind="bar", figsize=(8,5))

plt.title("Chest Pain Type Distribution")
plt.xlabel("Chest Pain Type (cp)")
plt.ylabel("Number of Patients")
plt.legend(["No Disease (0)", "Disease (1)"])

plt.show()