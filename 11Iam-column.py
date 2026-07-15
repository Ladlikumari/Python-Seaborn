import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset("titanic")

g = sns.lmplot(
    data=titanic,
    x="age",
    y="fare",
    col="class",
    hue="survived",
    height=5,
    aspect=1
)

g.set_titles("{col_name} Class")
g.set_axis_labels("Age","Fare")

plt.show()