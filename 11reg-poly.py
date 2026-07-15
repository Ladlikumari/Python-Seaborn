import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset("titanic")

plt.figure(figsize=(10,6))

sns.regplot(
    data=titanic,
    x="age",
    y="fare",
    order=2,
    scatter_kws={
        "color":"purple",
        "alpha":0.5,
        "s":50
    },
    line_kws={
        "color":"orange",
        "linewidth":3
    }
)

plt.title("Polynomial Regression", fontsize=15)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.grid(True)

plt.tight_layout()
plt.show()