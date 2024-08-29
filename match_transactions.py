import pandas as pd

def match_transactions(bank_file, qb_file, output_file):
    bank_data = pd.read_csv(bank_file)
    qb_data = pd.read_csv(qb_file)

    matches = pd.merge(bank_data, qb_data, on=['Date', 'Amount'], how='inner')
    unmatched_bank = bank_data[~bank_data.apply(tuple, 1).isin(matches.apply(tuple, 1))]
    unmatched_qb = qb_data[~qb_data.apply(tuple, 1).isin(matches.apply(tuple, 1))]

    matches.to_csv(f"{output_file}_matches.csv", index=False)
    unmatched_bank.to_csv(f"{output_file}_unmatched_bank.csv", index=False)
    unmatched_qb.to_csv(f"{output_file}_unmatched_qb.csv", index=False)
    print(f"Matched and unmatched transactions saved to {output_file}_*.csv")

if __name__ == "__main__":
    match_transactions("./output_files/bank_transactions.csv", "./output_files/quickbooks_transactions.csv", "./output_files/reconciliation")
