import pandas as pd

def load_quickbooks_transactions(csv_file, output_file):
    # Load the QuickBooks transactions from the exported CSV file
    qb_data = pd.read_csv(csv_file)

    # Save the transactions to the output file
    qb_data.to_csv(output_file, index=False)
    print(f"QuickBooks transactions saved to {output_file}")

if __name__ == "__main__":
    # Update the path to match where you'll place the exported CSV file
    load_quickbooks_transactions("./company_file/Transaction_List_By_Date.csv", "./output_files/quickbooks_transactions.csv")

