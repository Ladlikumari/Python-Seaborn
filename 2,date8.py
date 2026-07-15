import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dataset/dataset.csv")

no_disease = df[df["target"] == 0]
disease = df[df["target"] == 1]

plt.figure(figsize=(8,6))

# Scatter Plot
plt.scatter(no_disease["chol"], no_disease["thalach"],
            color="blue", label="No Disease (0)", alpha=0.7)

plt.scatter(disease["chol"], disease["thalach"],
            color="orange", label="Disease (1)", alpha=0.7)

# Regression Line for No Disease
m1, b1 = np.polyfit(no_disease["chol"], no_disease["thalach"], 1)
plt.plot(no_disease["chol"],
         m1 * no_disease["chol"] + b1,
         color="blue")

# Regression Line for Disease
m2, b2 = np.polyfit(disease["chol"], disease["thalach"], 1)
plt.plot(disease["chol"],
         m2 * disease["chol"] + b2,
         color="orange")

plt.title("Cholesterol Levels vs Maximum Heart Rate")
plt.xlabel("Cholesterol (chol)")
plt.ylabel("Maximum Heart Rate (thalach)")
plt.legend()

plt.show()