import pandas as pd

def generate_report(matched_file, unmatched_bank_file, unmatched_qb_file, report_file):
    matched = pd.read_csv(matched_file)
    unmatched_bank = pd.read_csv(unmatched_bank_file)
    unmatched_qb = pd.read_csv(unmatched_qb_file)

    with pd.ExcelWriter(report_file) as writer:
        matched.to_excel(writer, sheet_name='Matched Transactions', index=False)
        unmatched_bank.to_excel(writer, sheet_name='Unmatched Bank Transactions', index=False)
        unmatched_qb.to_excel(writer, sheet_name='Unmatched QB Transactions', index=False)
    print(f"Reconciliation report saved to {report_file}")

if __name__ == "__main__":
    generate_report(
        "./output_files/reconciliation_matches.csv",
        "./output_files/reconciliation_unmatched_bank.csv",
        "./output_files/reconciliation_unmatched_qb.csv",
        "./output_files/reconciliation_report.xlsx"
    )
