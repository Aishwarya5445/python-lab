import pandas as pd

# Load CSV file
df = pd.read_csv(r"F:\25335A0515_python\Book1.csv")

# Add new column
df["project marks"] = df["marks"] * 0.10
df["total marks"]=df["marks"]+ df["project marks"]

# Rename column
df.rename(columns={"name": "Student_Names"}, inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Display cleaned data
print("Modified and Cleaned Data:\n", df)