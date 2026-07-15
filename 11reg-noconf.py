import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

# Create figure
plt.figure(figsize=(10,6))

# Regression Plot
sns.regplot(
    data=titanic,
    x="age",
    y="fare",
    scatter_kws={
        "color":"skyblue",
        "alpha":0.6,
        "s":60
    },
    line_kws={
        "color":"red",
        "linewidth":3
    }
)

# Title and Labels
plt.title("Regression Plot between Age and Fare", fontsize=16)
plt.xlabel("Age of Passenger", fontsize=12)
plt.ylabel("Ticket Fare", fontsize=12)

# Grid
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()