import pdfplumber
import csv

def extract_transactions_from_pdf(pdf_file, output_file):
    transactions = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                parts = line.split(',')
                if len(parts) >= 3:
                    date, description, amount = parts[0], parts[1], parts[-1]
                    amount = amount.replace(',', '').replace('.', '', amount.count('.') - 1).strip()
                    try:
                        transactions.append({
                            'Date': date.strip(),
                            'Description': description.strip(),
                            'Amount': float(amount)
                        })
                    except ValueError as e:
                        print(f"Error parsing line: {line} - {e}")
                        continue

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    print(f"Transactions extracted and saved to {output_file}")

if __name__ == "__main__":
    # Extract transactions from multiple bank statements for stress testing
    months = ["January", "February", "March", "April", "May", "June", "July"]
    for month in months:
        extract_transactions_from_pdf(f"./bank_statements/{month}_2024.pdf", f"./output_files/bank_transactions_{month}.csv")

    # Extract transactions from the QuickBooks Transaction List by Date PDF
    extract_transactions_from_pdf("./company_file/Transaction_List_By_Date.pdf", "./output_files/quickbooks_transactions.csv")
