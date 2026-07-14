import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Random seed
np.random.seed(42)

# Student data
study_hours = np.random.normal(5, 2, 100)
exam_scores = study_hours * 8 + np.random.normal(0, 10, 100)
anxiety_level = np.random.randint(1, 10, 100)

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Scatter plot with color and size variation
scatter = ax.scatter(
    study_hours,
    exam_scores,
    c=anxiety_level,
    s=anxiety_level * 15,
    cmap="RdYlGn_r",
    alpha=0.7,
    edgecolors="black",
    linewidth=0.4
)

# Colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("Anxiety Level", fontsize=11)

# Trend line
z = np.polyfit(study_hours, exam_scores, 1)
p = np.poly1d(z)

x_line = np.linspace(0, 12, 100)

ax.plot(
    x_line,
    p(x_line),
    color="blue",
    linewidth=2,
    linestyle="--",
    label="Trend Line"
)

# Labels
ax.set_title(
    "Study Hours vs Exam Scores\n(Size/Color = Anxiety Level)",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Study Hours", fontsize=12)
ax.set_ylabel("Exam Scores", fontsize=12)

ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

ax.set_xlim(-0.5, 13)
ax.set_ylim(-5, 105)

# Annotate best and worst performers
max_idx = exam_scores.argmax()
min_idx = exam_scores.argmin()

ax.annotate(
    "Best",
    xy=(study_hours[max_idx], exam_scores[max_idx]),
    xytext=(8, 95),
    arrowprops=dict(arrowstyle="->"),
    fontsize=11,
    color="green"
)

ax.annotate(
    "Worst",
    xy=(study_hours[min_idx], exam_scores[min_idx]),
    xytext=(1, 10),
    arrowprops=dict(arrowstyle="->"),
    fontsize=11,
    color="red"
)

plt.tight_layout()
plt.show()