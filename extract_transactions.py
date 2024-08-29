import pdfplumber
import csv
import re
import os
import shutil

def is_valid_date(date_str):
    return bool(re.match(r'\d{1,2}/\d{1,2}/\d{2,4}', date_str))

def is_valid_amount(amount_str):
    try:
        float(amount_str.replace(',', ''))
        return True
    except ValueError:
        return False

def extract_transactions_from_pdf(pdf_file, output_file):
    transactions = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                parts = line.split(',')
                if len(parts) >= 3:
                    date, description, amount = parts[0].strip(), parts[1].strip(), parts[-1].strip()

                    if is_valid_date(date) and is_valid_amount(amount):
                        transactions.append({
                            'Date': date,
                            'Description': description,
                            'Amount': float(amount.replace(',', ''))
                        })
                    else:
                        print(f"Skipped non-transaction line: {line}")

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    print(f"Transactions extracted and saved to {output_file}")

def combine_transaction_files(output_file, *input_files):
    temp_file = output_file + ".tmp"
    
    with open(temp_file, 'w', newline='') as outfile:
        writer = None
        for file in input_files:
            with open(file, 'r') as infile:
                reader = csv.DictReader(infile)
                if writer is None:
                    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                    writer.writeheader()
                for row in reader:
                    writer.writerow(row)
    
    shutil.move(temp_file, output_file)
    print(f"Combined transactions saved to {output_file}")

if __name__ == "__main__":
    # Process each month's statement
    months = ["January", "February", "March", "April", "May", "June", "July"]
    transaction_files = []
    for month in months:
        output_file = f"./output_files/bank_transactions_{month}.csv"
        extract_transactions_from_pdf(f"./bank_statements/{month}_2024.pdf", output_file)
        transaction_files.append(output_file)

    # Combine all monthly transactions into one file
    combine_transaction_files("./output_files/bank_transactions_combined.csv", *transaction_files)

    # Extract QuickBooks transactions
    extract_transactions_from_pdf("./company_file/Transaction_List_By_Date.pdf", "./output_files/quickbooks_transactions.csv")
