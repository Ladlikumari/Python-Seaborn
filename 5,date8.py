import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/dataset.csv")

male_no = df[(df["sex"] == 1) & (df["target"] == 0)]["thalach"]
male_yes = df[(df["sex"] == 1) & (df["target"] == 1)]["thalach"]
female_no = df[(df["sex"] == 0) & (df["target"] == 0)]["thalach"]
female_yes = df[(df["sex"] == 0) & (df["target"] == 1)]["thalach"]

plt.figure(figsize=(8,6))

plt.boxplot(
    [male_no, male_yes, female_no, female_yes],
    tick_labels=[
        "Male\nNo Disease",
        "Male\nDisease",
        "Female\nNo Disease",
        "Female\nDisease"
    ]
)

plt.title("Maximum Heart Rate by Sex and Target")
plt.xlabel("Sex and Heart Disease Status")
plt.ylabel("Maximum Heart Rate (thalach)")

plt.show()