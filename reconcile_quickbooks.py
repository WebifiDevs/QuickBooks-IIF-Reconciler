import win32com.client
import pandas as pd

def reconcile_transactions_in_quickbooks(qbw_file, matched_file):
    qb = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
    qb.OpenConnection("", "QuickBooks Automation")
    qb.BeginSession(qbw_file, 0)

    matched_data = pd.read_csv(matched_file)
    for _, row in matched_data.iterrows():
        # Logic to find and mark transactions as reconciled
        print(f"Reconciling transaction: {row['Date']} - {row['Amount']}")

    qb.EndSession()
    qb.CloseConnection()
    print("Reconciliation completed in QuickBooks")

if __name__ == "__main__":
    reconcile_transactions_in_quickbooks("./quickbooks_company_files/Webify_Services_LTD.qbb", "./output_files/reconciliation_matches.csv")
