import pandas as pd

# Load CSV file
df = pd.read_csv(r"F:\25335A0515_python\Book1.csv")

# Display first 5 rows
print("Head:\n", df.head())

# Display last 5 rows
print("\nTail:\n", df.tail())

# Display information about dataset
print("\nInfo:")
df.info()

# Display statistical summary
print("\nDescribe:\n", df.describe())

