import pandas as pd
df = pd.read_csv("./programming-basics/data/samples.csv")

# 1.How many samples are there? Which organisms? 🔢

print(f"Number of samples:\n{df.shape[0] * df.shape[1]}")
print(f"Unique organisms:\n{df['organism'].unique()}")

# 2. What is the mean length of all samples? 
print(f"Mean length of all samples:\n{df['length'].mean()}")

# 3. Show only E. coli samples 

print(f"Escherichia coli samples:\n{df[df['organism'] == 'Escherichia coli']}")

# 4. Show samples with GC > 42 and length > 1000
print(f"Samples with GC > 42 and length > 1000:\n{df[(df['gc_content'] > 42) & (df['length'] > 1000)]}")

# 5. Top 3 samples by GC content 🥇
print(f"Top 3 samples by GC content:\n{df.sort_values('gc_content', ascending=False).head(3)}")

#6. Add a column length_kb
df["length_kb"] = df["length"]/1000
print(f"Samples with length in KB:\n{df}")