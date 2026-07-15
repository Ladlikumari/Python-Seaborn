import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset("titanic")

g = sns.lmplot(
    data=titanic,
    x="age",
    y="fare",
    height=6,
    aspect=1.3,
    scatter_kws={
        "color":"blue",
        "alpha":0.6,
        "s":60
    },
    line_kws={
        "color":"red",
        "linewidth":2
    }
)

g.set_axis_labels("Age", "Fare")
plt.title("Basic LM Plot")

plt.show()