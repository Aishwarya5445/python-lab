import pandas as pd

# Load CSV file
df = pd.read_csv(r"F:\25335A0515_python\Book1.csv")

# Sorting by a column (example: 'Age')
sorted_df = df.sort_values(by="age")
print("Sorted Data:\n", sorted_df)

# Slicing rows (first 5 rows)
print("\nFirst 5 rows:\n", df[0:5])

# Slicing specific columns
print("\nSelected Columns:\n", df[["name", "age"]])