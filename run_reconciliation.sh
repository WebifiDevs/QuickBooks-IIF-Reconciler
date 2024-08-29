#!/bin/bash

# Set the working directory where your Python scripts are located
WORKING_DIR="/path/to/reconciliation_automation"
cd "$WORKING_DIR"

# Step 1: Extract transactions from PDF bank statement
echo "Step 1: Extracting transactions from PDF..."
python3 extract_transactions.py
if [ $? -ne 0 ]; then
    echo "Failed to extract transactions from PDF."
    exit 1
fi

# Step 2: Load QuickBooks transactions
echo "Step 2: Loading QuickBooks transactions..."
python3 load_quickbooks_transactions.py
if [ $? -ne 0 ]; then
    echo "Failed to load QuickBooks transactions."
    exit 1
fi

# Step 3: Match transactions
echo "Step 3: Matching transactions..."
python3 match_transactions.py
if [ $? -ne 0 ]; then
    echo "Failed to match transactions."
    exit 1
fi

# Step 4: Reconcile transactions in QuickBooks
echo "Step 4: Reconciling transactions in QuickBooks..."
python3 reconcile_quickbooks.py
if [ $? -ne 0 ]; then
    echo "Failed to reconcile transactions in QuickBooks."
    exit 1
fi

# Step 5: Generate and send reconciliation report
echo "Step 5: Generating and sending reconciliation report..."
python3 generate_report.py
if [ $? -ne 0 ]; then
    echo "Failed to generate or send reconciliation report."
    exit 1
fi

echo "Reconciliation process completed successfully."
