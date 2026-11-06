def average(values):
    return sum(values) / len(values)

path = "../data/samples.csv"
gc_content = []
with open(path) as f:
    next(f)
    for line in f:
        sample, gc, length = line.strip().split(",")
        gc_content.append(float(gc))

print(average(gc_content))

import pandas as pd

df = pd.read_csv("../data/samples.csv")
print(df["gc_content"].mean())

print(df.describe())