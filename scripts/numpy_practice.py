import numpy as np
import pandas as pd
df = pd.read_csv("./programming-basics/data/samples.csv")
print(df.head())

# In scripts/numpy_practice.py, using the length column as an array: 
# 1. Print the mean, median and standard deviation
lengths = df["length"].to_numpy()
mean_lengths = np.mean(lengths)
median_lengths = np.median(lengths)
st_dev_lengths = np.std(lengths)
print(f"Mean: {mean_lengths}. Median: {median_lengths}. Standard Deviation: {st_dev_lengths}")

# 2. Convert all lengths to kb (one line, no loop)
print(f"Lengths array: {lengths}") 
lengths_kb = lengths / 1000
print (f"Lengths in kb: {lengths_kb}")

# 3. How many samples are longer than 1000 bp?
df_greater_1000_bp = df[df["length"] > 1000]
lengths_greater_1kb = df_greater_1000_bp["length"].to_numpy()
print(f"Number of samples longer than 1000 bp: {len(lengths_greater_1kb)}")

# 4. Which is bigger here: mean or median? What does that tell you? 🤔
# Mean is bigger than median, which indicates that the distribution of lengths is 
# right-skewed (there are some very long samples that are pulling the mean up).

# 5. Bonus: np.percentile(lengths, 90): what does it mean?
print(np.percentile(lengths, 90))

# It means that 90% of the samples have a length less than or equal to this value, 
# and 10% of the samples have a length greater than this value.
