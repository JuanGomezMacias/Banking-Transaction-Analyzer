import csv

def save_flagged(filename, flagged):
    if not flagged:
        print("No suspicious transactions.")
        return

    keys = flagged[0].keys()
    with open(filename, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(flagged)
