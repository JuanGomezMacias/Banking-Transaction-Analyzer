from parser import load_transactions
from rules import evaluate_transactions
from report import save_flagged

def main():
    transactions = load_transactions("transactions.csv")
    flagged = evaluate_transactions(transactions)

    print(f"Flagged {len(flagged)} suspicious transactions")
    save_flagged("flagged.csv", flagged)

if __name__ == "__main__":
    main()
