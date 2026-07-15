
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset("titanic")

g = sns.lmplot(
    data=titanic,
    x="age",
    y="fare",
    hue="sex",
    markers=["o","s"],
    height=6,
    aspect=1.3
)

g.set_axis_labels("Passenger Age","Ticket Fare")

plt.show()