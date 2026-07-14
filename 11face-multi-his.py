import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset("titanic")

g = sns.FacetGrid(
    titanic,
    col="embark_town",
    col_wrap=2,
    height=4
)

g.map(
    sns.histplot,
    "fare",
    bins=15,
    kde=True,
    color="orange"
)

g.set_titles("{col_name}")
g.set_axis_labels("Fare","Frequency")

plt.show()