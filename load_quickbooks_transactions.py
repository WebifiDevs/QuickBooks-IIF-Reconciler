import win32com.client

def load_quickbooks_transactions(qbw_file, output_file):
    qb = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
    qb.OpenConnection("", "QuickBooks Automation")
    qb.BeginSession(qbw_file, 0)  # 0 = Open in single-user mode

    # Create and send a request to get all transactions
    request = """<QBXML>
                     <QBXMLMsgsRq onError="continueOnError">
                         <TxnQueryRq>
                             <TxnTypeFilter>Check</TxnTypeFilter>
                             <!-- Add other filters if needed -->
                         </TxnQueryRq>
                     </QBXMLMsgsRq>
                 </QBXML>"""
    response = qb.ProcessRequest(request)
    qb.EndSession()
    qb.CloseConnection()

    # Save the transactions to a CSV file
    with open(output_file, 'w') as file:
        file.write(response)
    print(f"QuickBooks transactions saved to {output_file}")

if __name__ == "__main__":
    load_quickbooks_transactions("./quickbooks_company_files/Webify_Services_LTD.qbb", "./output_files/quickbooks_transactions.csv")
