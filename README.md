# IIFReconciler

IIFReconciler is an automation tool designed to streamline the process of reconciling bank transactions with QuickBooks records. It extracts transactions from PDF files, matches them, and generates an .iif (`Intuit Interchange Format`) file for easy import into QuickBooks, facilitating seamless reconciliation.

## Table of Contents

- [IIFReconciler](#iifreconciler)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Step 1: Extract Transactions](#step-1-extract-transactions)
    - [Step 2: Match Transactions](#step-2-match-transactions)
    - [Step 3: Generate Report](#step-3-generate-report)
    - [Step 4: Generate IIF File](#step-4-generate-iif-file)
    - [Step 5: Import IIF into QuickBooks](#step-5-import-iif-into-quickbooks)
  - [Project Structure](#project-structure)

## Features

- **Automated Transaction Extraction**: Extracts transactions from bank statements and QuickBooks reports in PDF format.
- **Transaction Matching**: Matches transactions between bank records and QuickBooks, identifying discrepancies.
- **Report Generation**: Generates a detailed report on matched and unmatched transactions.
- **IIF File Generation**: Automatically generates an IIF file for importing unmatched transactions into QuickBooks.
- **Seamless Integration**: Easy-to-use scripts that integrate smoothly with QuickBooks for reconciliation.

## Requirements

- Python 3.7 or higher
- QuickBooks Desktop (for IIF import)
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/IIFReconciler.git
   cd IIFReconciler
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv virt
   source virt/bin/activate  # On Windows use `virt\Scripts\activate`
   ```

3. **Install Required Python Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Required Directories**:
   - Since the `.gitignore` file is set to ignore empty directories, you need to manually create the required directories:
   ```bash
   mkdir -p bank_statements company_file output_files
   ```

## Usage

### Step 1: Extract Transactions

1. Place the bank statement PDF files in the `bank_statements/` directory.
2. Place the QuickBooks `Transaction List by Date` PDF in the `company_file/` directory.

### Step 2: Match Transactions

1. Run the main script to start the extraction and matching process:
   ```bash
   ./run.sh
   ```
2. The script will extract transactions from the PDFs and combine them into a single CSV file for matching.

### Step 3: Generate Report

1. The script will generate a detailed reconciliation report showing matched and unmatched transactions, saved in the `output_files/` directory.

### Step 4: Generate IIF File

1. If you choose to proceed, the script will generate an IIF file based on unmatched transactions for import into QuickBooks.

### Step 5: Import IIF into QuickBooks

1. Open QuickBooks Desktop.
2. Go to `File > Utilities > Import > IIF Files`.
3. Select the generated IIF file (`reconciliation_import.iif`) from the `output_files/` directory and complete the import.

## Project Structure

```
IIFReconciler/
│
├── bank_statements/                # Directory for bank statement PDFs (create manually)
├── company_file/                   # Directory for QuickBooks PDFs and other files (create manually)
├── output_files/                   # Directory for generated CSVs, reports, and IIF files (create manually)
│   ├── bank_transactions_combined.csv # Combined bank transactions file
│   ├── quickbooks_transactions.csv    # Extracted QuickBooks transactions
│   ├── reconciliation_matches.csv     # Matched transactions
│   ├── reconciliation_unmatched_bank.csv # Unmatched bank transactions
│   ├── reconciliation_unmatched_qb.csv   # Unmatched QuickBooks transactions
│   ├── reconciliation_report.xlsx     # Reconciliation report
│   ├── reconciliation_import.iif      # Generated IIF file for QuickBooks import
│
├── extract_transactions.py         # Script for extracting transactions from PDFs
├── generate_report.py              # Script for generating reconciliation report
├── generate_iif.py                 # Script for generating IIF file from unmatched transactions
├── match_transactions.py           # Script for matching transactions between bank and QuickBooks
├── run.sh           # Main bash script to run the entire reconciliation process
├── requirements.txt                # Required Python libraries
└── README.md                       # Project documentation
```
