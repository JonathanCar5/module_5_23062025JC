import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('03_Library SystemCustomers.csv')

#drop na
df = df.dropna(how='all')

df['Book checkout'] =pd.to_datetime(df['Book checkout'].str.rplace('"',''), errors='coerce')

#drop duplicates
df = df.drop_duplicates()

df.reset_index(drop=True, inplace = True)

print("\n=== Cleaned Data ===") 
print(df)

print("\nFinal shape:", df.shape)

df.to_csv("Cleaned_03_Library SystemCustomers.csv", index=False)

print("Cleaned file saved as Cleaned_03_Library SystemCustomers.csv")

import pandas as pd

# Load the original CSV
df = pd.read_csv("python_app\Cleaned_Books.csv")

# Save to a new CSV
df.to_csv("Cleaned_Books2.csv", index=False)