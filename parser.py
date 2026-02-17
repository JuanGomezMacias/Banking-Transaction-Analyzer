import csv

def load_transactions(filename):
    transactions = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            transactions.append(row)
    return transactions
