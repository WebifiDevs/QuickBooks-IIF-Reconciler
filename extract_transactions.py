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
                if len(parts) == 3:
                    date, description, amount = parts
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
    extract_transactions_from_pdf("./bank_statements/1JAN_2024_statements-2063-.pdf", "./output_files/bank_transactions.csv")
