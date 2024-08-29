import csv

def generate_iif_from_csv(unmatched_bank_file, unmatched_qb_file, output_iif_file):
    with open(unmatched_bank_file, 'r') as bank_csv, open(unmatched_qb_file, 'r') as qb_csv, open(output_iif_file, 'w') as iif_file:
        bank_reader = csv.DictReader(bank_csv)
        qb_reader = csv.DictReader(qb_csv)

        # Write headers for IIF file
        iif_file.write("!TRNS	TRNSTYPE	DATE	ACCNT	AMOUNT	MEMO\n")
        iif_file.write("!SPL		DATE	ACCNT	AMOUNT	MEMO\n")
        iif_file.write("!ENDTRNS\n")

        # Add unmatched bank transactions to IIF
        for row in bank_reader:
            iif_file.write(f"TRNS	BANK	{row['Date']}	Bank Account	-{row['Amount']}	{row['Description']}\n")
            iif_file.write(f"SPL		{row['Date']}	Expense	{row['Amount']}	{row['Description']}\n")
            iif_file.write("ENDTRNS\n")

        # Add unmatched QuickBooks transactions to IIF
        for row in qb_reader:
            iif_file.write(f"TRNS	BANK	{row['Date']}	Bank Account	{row['Amount']}	{row['Description']}\n")
            iif_file.write(f"SPL		{row['Date']}	Expense	-{row['Amount']}	{row['Description']}\n")
            iif_file.write("ENDTRNS\n")

    print(f"IIF file generated: {output_iif_file}")

if __name__ == "__main__":
    generate_iif_from_csv(
        "./output_files/reconciliation_unmatched_bank.csv",
        "./output_files/reconciliation_unmatched_qb.csv",
        "./output_files/reconciliation_import.iif"
    )
