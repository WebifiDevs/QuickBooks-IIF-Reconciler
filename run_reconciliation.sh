#!/bin/bash

# Set the working directory where your Python scripts are located
WORKING_DIR="$(pwd)"  # Sets the working directory to the current directory
cd "$WORKING_DIR"

# Define an array of months for January to July
months=("January" "February" "March" "April" "May" "June" "July")

# Create output_files directory if not exists
mkdir -p output_files

for month in "${months[@]}"; do
    # Step 1: Extract transactions from the PDF bank statement for each month
    echo "Step 1: Extracting transactions from bank statement PDF for $month 2024..."
    python extract_transactions.py "./bank_statements/${month}_2024.pdf" "./output_files/bank_transactions_${month}.csv"
    if [ $? -ne 0 ]; then
        echo "Failed to extract transactions from $month 2024 PDF."
        exit 1
    fi
done

# Step 2: Extract transactions from QuickBooks Transaction List by Date PDF
echo "Step 2: Extracting transactions from QuickBooks Transaction List by Date PDF..."
python extract_transactions.py "./company_file/Transaction_List_By_Date.pdf" "./output_files/quickbooks_transactions.csv"
if [ $? -ne 0 ]; then
    echo "Failed to extract transactions from QuickBooks PDF."
    exit 1
fi

# Step 3: Combine all bank transactions into one file for matching
echo "Step 3: Combining all bank transactions into a single file..."
cat ./output_files/bank_transactions_*.csv > ./output_files/bank_transactions_combined_temp.csv
if [ $? -ne 0 ]; then
    echo "Failed to combine bank transactions."
    exit 1
fi

# Rename the temporary combined file to the final output file
mv ./output_files/bank_transactions_combined_temp.csv ./output_files/bank_transactions_combined.csv
if [ $? -ne 0 ]; then
    echo "Failed to rename combined transactions file."
    exit 1
fi

echo "Combined transactions saved to ./output_files/bank_transactions_combined.csv"

# Step 4: Match transactions
echo "Step 4: Matching transactions..."
python match_transactions.py "./output_files/bank_transactions_combined.csv" "./output_files/quickbooks_transactions.csv" "./output_files/reconciliation"
if [ $? -ne 0 ]; then
    echo "Failed to match transactions."
    exit 1
fi

# Step 4.5: Generate a preliminary report and ask user to proceed
echo "Generating preliminary reconciliation report..."
python generate_report.py "./output_files/reconciliation_matches.csv" "./output_files/reconciliation_unmatched_bank.csv" "./output_files/reconciliation_unmatched_qb.csv" "./output_files/reconciliation_report.xlsx"
if [ $? -ne 0 ]; then
    echo "Failed to generate preliminary reconciliation report."
    exit 1
fi

echo "Preliminary reconciliation report generated at ./output_files/reconciliation_report.xlsx"
echo "Please review the report before proceeding."

# Ask the user if they want to proceed with the reconciliation
read -p "Do you want to proceed with generating an IIF file for QuickBooks import? (yes/no): " user_choice

if [[ "$user_choice" != "yes" ]]; then
    echo "Reconciliation process aborted by the user."
    exit 0
fi

# Step 5: Generate IIF file for QuickBooks import
echo "Step 5: Generating IIF file for QuickBooks import..."
python generate_iif.py "./output_files/reconciliation_unmatched_bank.csv" "./output_files/reconciliation_unmatched_qb.csv" "./output_files/reconciliation_import.iif"
if [ $? -ne 0 ]; then
    echo "Failed to generate IIF file."
    exit 1
fi

echo "IIF file generated: ./output_files/reconciliation_import.iif"
echo "You can now import this file into QuickBooks to complete the reconciliation process."

echo "Reconciliation process completed successfully."
