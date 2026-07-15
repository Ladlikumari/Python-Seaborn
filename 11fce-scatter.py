import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset("titanic")

g = sns.FacetGrid(
    titanic,
    col="class",
    row="survived",
    height=4,
    aspect=1.2
)

g.map_dataframe(
    sns.scatterplot,
    x="age",
    y="fare",
    hue="sex",
    alpha=0.7
)

g.add_legend()
g.set_axis_labels("Age","Fare")

plt.show()