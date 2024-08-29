# AutoReconcile

AutoReconcile is an automation tool designed to streamline the process of reconciling bank transactions with QuickBooks records. It extracts transactions from PDF files, matches them, and generates an IIF file for easy import into QuickBooks, facilitating seamless reconciliation.

## Table of Contents

- [AutoReconcile](#autoreconcile)
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
  - [Contributing](#contributing)
  - [License](#license)

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
   git clone https://github.com/yourusername/AutoReconcile.git
   cd AutoReconcile
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

## Usage

### Step 1: Extract Transactions

1. Place the bank statement PDF in the `bank_statements/` directory.
2. Place the QuickBooks `Transaction List by Date` PDF in the `company_file/` directory.

### Step 2: Match Transactions

1. Run the main script to start the extraction and matching process:
   ```bash
   ./run_reconciliation.sh
   ```
2. Review the preliminary report generated in the `output_files/` directory.

### Step 3: Generate Report

1. The script will generate a detailed reconciliation report showing matched and unmatched transactions.

### Step 4: Generate IIF File

1. If you choose to proceed, the script will generate an IIF file based on unmatched transactions for import into QuickBooks.

### Step 5: Import IIF into QuickBooks

1. Open QuickBooks Desktop.
2. Go to `File > Utilities > Import > IIF Files`.
3. Select the generated IIF file (`reconciliation_import.iif`) from the `output_files/` directory and complete the import.

## Project Structure

```
AutoReconcile/
│
├── bank_statements/                # Directory for bank statement PDFs
├── company_file/                   # Directory for QuickBooks PDFs and other files
├── output_files/                   # Directory for generated CSVs, reports, and IIF files
│   ├── bank_transactions.csv       # Extracted bank transactions
│   ├── quickbooks_transactions.csv # Extracted QuickBooks transactions
│   ├── reconciliation_matches.csv  # Matched transactions
│   ├── reconciliation_unmatched_bank.csv # Unmatched bank transactions
│   ├── reconciliation_unmatched_qb.csv   # Unmatched QuickBooks transactions
│   ├── reconciliation_report.xlsx  # Reconciliation report
│   ├── reconciliation_import.iif   # Generated IIF file for QuickBooks import
│
├── extract_transactions.py         # Script for extracting transactions from PDFs
├── generate_report.py              # Script for generating reconciliation report
├── generate_iif.py                 # Script for generating IIF file from unmatched transactions
├── match_transactions.py           # Script for matching transactions between bank and QuickBooks
├── run_reconciliation.sh           # Main bash script to run the entire reconciliation process
├── requirements.txt                # Required Python libraries
└── README.md                       # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or raise an issue to discuss any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

