import polars as pl
import glob

# Path to the folder containing invoice files
invoices_folder = "invoices"

# Use glob to get a list of all CSV files in the "invoices" folder
invoice_files = sorted(glob.glob(f"{invoices_folder}/*.csv"))

# Loop through each invoice file
for file in invoice_files:
    # Read the CSV file into a Polars DataFrame
    df = pl.read_csv(file)
    print(df)
    # Calculate the sum of the "Total Price" column
    total_sum = df['Total Price'].sum()
    
    # Get the number of invoices (rows)
    item_count = df.height
    item_sum=df["Quantity"].sum()
    # Print the results for each file
    print("*" *30)
    print(f"File: {file}")
    print(f"Total Item Quantity: {item_sum}")
    print(f"Number of Items: {item_count}")
    print(f"Total sum of prices: ${total_sum:.2f}")
    print("*" * 30)