from datetime import datetime

LARGE_TRANSFER = 10000
RAPID_SECONDS = 30

def check_large_transfer(tx):
    return tx["amount"] > LARGE_TRANSFER

def check_rapid_transactions(tx, prev_tx):
    if prev_tx is None:
        return False

    t1 = datetime.fromisoformat(tx["timestamp"])
    t2 = datetime.fromisoformat(prev_tx["timestamp"])
    diff = (t1 - t2).total_seconds()

    return diff < RAPID_SECONDS and tx["account"] == prev_tx["account"]

def evaluate_transactions(transactions):
    flagged = []
    prev = None

    for tx in transactions:
        reasons = []

        if check_large_transfer(tx):
            reasons.append("Large transfer")

        if check_rapid_transactions(tx, prev):
            reasons.append("Rapid repeated transaction")

        if reasons:
            tx["flags"] = "; ".join(reasons)
            flagged.append(tx)

        prev = tx

    return flagged
