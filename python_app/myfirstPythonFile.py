import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('C:/Users/Admin/Desktop/module_5_23062025JC/python_app/03_Library SystemCustomers.csv')

#drop na
df = df.dropna(How='all')

df['Book checkout'] =pd.to_datetime(df['Book checkout'].str.rplace('"',''), errors='coerce')

#drop duplicates
df = df.drop_duplicates()

df.reset_index(drop=True, inplace = True)

print("\n=== Cleaned Data ===") 
print(df)

print("\nFinal shape:", df.shape)

df.to_csv("Cleaned_03_Library SystemBook.csv", index=False)

print(f"Cleaned file saved as Cleaned_03_Library SystemBook.csv")