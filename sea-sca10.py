import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


penguins = sns.load_dataset('penguins').dropna()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Basic scatter
sns.scatterplot(
data=penguins,
x='flipper_length_mm',
y='body_mass_g',
ax=axes[0]
)
axes[0].set_title("Basic Scatter")

# Advanced scatter
sns.scatterplot(
data=penguins,
x='flipper_length_mm',
y='body_mass_g',
hue='species', # color by species
style='island', # shape by island
size='bill_length_mm', # size by bill length
palette='Set1',
sizes=(20, 200),


alpha=0.8,
edgecolors='black',
linewidth=0.3,
ax=axes[1]
)
axes[1].set_title("Advanced Scatter")
axes[1].legend(bbox_to_anchor=(1.05, 1),
loc='upper left',
fontsize=8)

plt.suptitle("Penguin Scatter Plots",
fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()