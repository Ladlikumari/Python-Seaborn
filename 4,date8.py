import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dataset/dataset.csv")

no_disease = df[df["target"] == 0]
disease = df[df["target"] == 1]

plt.figure(figsize=(8,6))

# Scatter Plot
plt.scatter(no_disease["age"], no_disease["trestbps"],
            color="blue", label="No Disease (0)", alpha=0.7)

plt.scatter(disease["age"], disease["trestbps"],
            color="orange", label="Disease (1)", alpha=0.7)

# Trend Line for No Disease
m1, b1 = np.polyfit(no_disease["age"], no_disease["trestbps"], 1)
plt.plot(no_disease["age"],
         m1 * no_disease["age"] + b1,
         color="blue")

# Trend Line for Disease
m2, b2 = np.polyfit(disease["age"], disease["trestbps"], 1)
plt.plot(disease["age"],
         m2 * disease["age"] + b2,
         color="orange")

plt.title("Resting Blood Pressure by Age and Target")
plt.xlabel("Age")
plt.ylabel("Resting Blood Pressure (trestbps)")
plt.legend()

plt.show()