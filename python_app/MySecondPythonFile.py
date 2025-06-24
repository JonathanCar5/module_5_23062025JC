import pandas as pd

# Enrich the dataset with additional information.
# Example enrichment: add a new column with the number of days on loan
def dataEnrich(data):
    if 'Book_checkout' in data.columns and 'Book_returned' in data.columns:
        data['Book_checkout'] = pd.to_datetime(data['Book_checkout'])
        data['Book_returned'] = pd.to_datetime(data['Book_returned'])
        data['days_on_loan'] = (data['Book_returned'] - data['Book_checkout']).dt.days
        print("Data has been enriched with the number of days on loan.")
    return data

# Load your data into a DataFrame
df = pd.read_csv('03_Library Systembook.csv')

# Drop rows where all elements are NaN
df = df.dropna(how='all')

# Drop duplicate rows
df = df.drop_duplicates()

# Remove leading and trailing double quotes from the 'date' column
df['Book checkout'] = df['Book checkout'].str.strip('"')

# Reset index
df.reset_index(drop=True, inplace=True)

print("\n=== Cleaned Data ===") 
print(df)

print("\nFinal shape:", df.shape)

# Save the cleaned data to a new CSV file
df.to_csv("Cleaned_03_Library Systembook.csv", index=False)

# Enrich the data
df = dataEnrich(df)

# Save the enriched data to a new CSV file
df.to_csv("Enriched_03_Library Systembook.csv", index=False)

print("Cleaned file saved as Cleaned_03_Library Systembook.csv")
print("Enriched file saved as Enriched_03_Library Systembook.csv")