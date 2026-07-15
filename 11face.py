import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset("titanic")

g = sns.FacetGrid(
    titanic,
    col="sex",
    height=5,
    aspect=1
)

g.map(
    sns.histplot,
    "age",
    bins=20,
    kde=True,
    color="steelblue"
)

g.set_axis_labels("Age","Count")
g.set_titles("Gender : {col_name}")

plt.show()