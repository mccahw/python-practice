import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Testing basic numpy arrays
# One-dimensional array
a1 = np.array([1, 2, 3, 4])
print(a1)
print(a1.shape)

# Two-dimensional flat array (row vector)
a2 = np.array([[1, 2, 3, 4]])
print(a2)
print(a2.shape)

# Two-dimensional tall array (column vector)
a3 = np.array([[1], [2], [3], [4]])
print(a3)
print(a3.shape)

# Numpy can be used to make matricies
M1 = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [0, 0, 1]])
print(M1)
print("M1 Size\nm: {} n: {}".format(M1.shape[0], M1.shape[1]))

# Arrays can be reshaped
M2 = np.reshape(M1, (1, 12))
print(M2)
print(M2.shape)

a1_vec = np.reshape(a1, (a1.shape[0], 1))
print(a1_vec)
print("Reshaped a1: ", a1_vec.shape)

# Numpy arrays are different than Python lists
l = [1, 2, 3, 4]
l_np = np.array(l)
print(l)
print(l_np)
print(l*5)
print(l_np*5)

# Pandas is highly compatible with Numpy
np.random.seed(42)
M4 = np.random.randn(10, 5)
print(M4)
df = pd.DataFrame(M4)
print(df)

# Pandas columns can be renamed
df.columns = ["col1", "col2", "col3", "col4", "col5"]
print(df)

# Pandas columns can be used with Numpy
print(df["col1"].shape)

# Pandas supports many statistical operations on data
print(df.describe())

# Subsets of dataframes can be created as well
df_subset = df[["col1", "col2"]]
print(df_subset)

# Column names can be assigned to existing, non-Pandas arrays
M5 = np.array([["no", "factor1", 0],
               ["yes", "factor2", 2],
               ["no", "factor3", 0],
               ["no", "factor4", 2],
               ["yes", "factor1", 1],
               ["no", "factor2", 3],
               ["yes", "factor5", 3],
               ["no", "factor1", 0],
               ["yes", "factor5", 3],
               ["yes", "factor1", 2],
               ["yes", "factor5", 1],
               ["no", "factor1", 2],
               ["no", "factor2", 0],
               ["yes", "factor1", 1],
               ["no", "factor3", 2]
               ])
df2 = pd.DataFrame(M5, columns=["Request", "Factor", "Impact"])
df2["Impact"] = df2["Impact"].astype(int)
print(df2)

# Adding an extra column to data
np.random.seed()
cs = np.random.uniform(low=-1, high=1, size=M5.shape[0])
print(cs)
df2["kll_index"] = cs
print(df2)

# Match elements where condition is met
condition = df2["Request"] == "no"
print(condition)
print(df2[condition])

# Apply a function to all elements
mapping = {"factor1": "NA", "factor2": "MX",
           "factor3": "LX", "factor4": "TY", "factor5": "PSOX"}
df2["EDX"] = df2["Factor"].apply(lambda x: mapping.get(x, "Not Found"))
print(df2)

# Change the contents of a column
condition = df2["Factor"] == "factor1"
df.loc[condition, "Request"] = "no"
print(df2)

# Sorting DataFrames
df2.sort_values(by=["kll_index"],
                ascending=True,
                inplace=True)
print(df2)

# Sorting values does NOT change the index!
# The index can be reset however
df2.reset_index(inplace=True)
print(df2)

# Resetting the index adds a column with the old index
# This can be dropped
df2.drop(columns=["index"], inplace=True)
print(df2)

# Aggregations can be performed on columns with Matplotlib
df_agg = df2.groupby("EDX").sum().reset_index()
print(df_agg)

# MATPLOTLIB

# Scatter plots
plt.figure(figsize=(15, 10))  # set the window size
x = df2["Impact"]
y = df2["kll_index"]
plt.scatter(x, y, color="blue", marker="*")
plt.title("Consumption index vs Impact")
plt.xlabel("Impact")
plt.ylabel("Consumption_index")
plt.show()

# Create some more random data to graph
# Create a correlated variable
df2["y"] = df2["kll_index"].apply(
    lambda x: np.exp(x)*2 if np.random.uniform(-1, 1) < 0
    else np.exp(x)/2)
plt.figure(figsize=(15, 10))
x = df2["kll_index"]
y = df2["y"]
plt.scatter(x, y, color="blue", marker="*")
plt.title("Consumption index vs target scatterplot")
plt.xlabel("Consumption index")
plt.ylabel("Target")
plt.show()

# The same data can be expressed linearly
plt.figure(figsize=(15, 10))
x = df2["kll_index"]
y = df2["y"]
plt.plot(x, y, color="red", marker="*")
plt.title("Consumption index vs target scatterplot")
plt.xlabel("Consumption Index")
plt.ylabel("Target")
plt.show()

# Multiple plots are shown by multiple plot calls
df2["y2"] = df2["kll_index"].apply(
    lambda x: np.exp(x)*2 if np.random.uniform(-0.5, 2) < 0
    else np.exp(x)/2)
plt.figure(figsize=(15, 10))
x = df2["kll_index"]
y1 = df2["y"]
y2 = df2["y2"]
plt.plot(x, y1, color="red", marker="*")
plt.plot(x, y2, color="blue", marker="o")
plt.title("Consumption index vs target scatterplot")
plt.xlabel("Consumption Index")
plt.ylabel("Target")
plt.show()

# Bar plot directly from DataFrames
ax = df_agg.plot.bar(x='EDX', y='Impact', rot=0, figsize=(15, 10))
plt.title("Barplot")
plt.xlabel("EDX")
plt.ylabel("Counts")
plt.show()

# Same can be done for mulitple bar plots
df_agg["Impact2"] = [3,4,7,10,1]
df_bar = df_agg[["EDX","Impact","Impact2"]]
df_bar.set_index("EDX", inplace=True)
df_bar.plot.bar(figsize=(15,10))
plt.show()

# Piecharts can also be plotted from DataFrames
df_bar.plot.pie(y="Impact", figsize=(15,10))
plt.show()