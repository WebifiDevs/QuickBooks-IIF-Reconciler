#!/bin/bash

# Set the working directory where your Python scripts are located
WORKING_DIR="$(pwd)"  # Sets the working directory to the current directory
cd "$WORKING_DIR"

# Step 1: Extract transactions from PDF bank statement January_2024.pdf
echo "Step 1: Extracting transactions from bank statement PDF..."
python extract_transactions.py "./bank_statements/January_2024.pdf" "./output_files/bank_transactions.csv"
if [ $? -ne 0 ]; then
    echo "Failed to extract transactions from PDF."
    exit 1
fi

# Step 2: Extract transactions from QuickBooks Transaction List by Date PDF
echo "Step 2: Extracting transactions from QuickBooks Transaction List by Date PDF..."
python extract_transactions.py "./company_file/Transaction_List_By_Date.pdf" "./output_files/quickbooks_transactions.csv"
if [ $? -ne 0 ]; then
    echo "Failed to extract transactions from QuickBooks PDF."
    exit 1
fi

# Step 3: Match transactions
echo "Step 3: Matching transactions..."
python match_transactions.py "./output_files/bank_transactions.csv" "./output_files/quickbooks_transactions.csv" "./output_files/reconciliation"
if [ $? -ne 0 ]; then
    echo "Failed to match transactions."
    exit 1
fi

# Step 3.5: Generate a preliminary report and ask user to proceed
echo "Generating preliminary reconciliation report..."
python generate_report.py "./output_files/reconciliation_matches.csv" "./output_files/reconciliation_unmatched_bank.csv" "./output_files/reconciliation_unmatched_qb.csv" "./output_files/reconciliation_report.xlsx"
if [ $? -ne 0 ]; then
    echo "Failed to generate preliminary reconciliation report."
    exit 1
fi

echo "Preliminary reconciliation report generated at ./output_files/reconciliation_report.xlsx"
echo "Please review the report before proceeding."

# Ask the user if they want to proceed with the reconciliation
read -p "Do you want to proceed with reconciling transactions in QuickBooks? (yes/no): " user_choice

if [[ "$user_choice" != "yes" ]]; then
    echo "Reconciliation process aborted by the user."
    exit 0
fi

# Step 4: Reconcile transactions in QuickBooks
echo "Step 4: Reconciling transactions in QuickBooks..."
python reconcile_quickbooks.py "./company_file/Webify_Services_LTD.QBB" "./output_files/reconciliation_matches.csv"
if [ $? -ne 0 ]; then
    echo "Failed to reconcile transactions in QuickBooks."
    exit 1
fi

echo "Reconciliation process completed successfully."
