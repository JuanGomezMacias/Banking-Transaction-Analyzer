Banking Transaction Analyzer

A Python-based data analysis tool that scans financial transaction datasets and flags potentially suspicious activity using rule-based detection logic.

This project was built to demonstrate practical data processing, modular program design, and the application of software to financial risk detection problems.

Features

Parses transaction datasets from CSV files

Detects suspicious financial patterns such as:

Unusually large transfers

Rapid repeated transactions

Geographic inconsistencies between transactions

Generates a report of flagged transactions for review

Modular code structure separating:

Data parsing

Rule evaluation

Reporting

Technologies Used

Python 3

CSV file processing

Basic data analysis techniques

Rule-based anomaly detection logic

Project Structure
banking-transaction-analyzer/
│
├── main.py              # Runs the program
├── parser.py            # Handles CSV loading and formatting
├── rules.py             # Contains suspicious activity logic
├── report.py            # Outputs flagged transactions
├── sample_transactions.csv
└── README.md
How It Works

The program loads transaction records from a CSV file.

Each transaction is evaluated against predefined detection rules.

Transactions meeting suspicious criteria are flagged.

A summary report of flagged entries is printed or saved.

Example Output
Flagged 2 suspicious transactions:

ID    Amount    Country    Timestamp    Account
1023  9800      RU         2026-01-14    ACC445
2041  12000     CN         2026-01-15    ACC223
How to Run

Install Python 3 if not already installed

Clone the repository:

git clone https://github.com/yourusername/banking-transaction-analyzer.git

Navigate into the folder:

cd banking-transaction-analyzer

Run the program:

python main.py
Why I Built This

I created this project to explore how software can support financial monitoring systems by identifying patterns that may indicate fraud or unusual activity. It also helped me practice designing modular Python programs and working with structured datasets.

Possible Future Improvements

Add visualization of transaction patterns

Implement machine learning anomaly detection

Add configurable rule thresholds via config file

Export results to PDF or Excel reports

Add unit tests for detection logic
