import re
from pathlib import Path

def extract_revenue(text):
    patterns = [
        r"Net revenue[s]?\s+\$?([\d,]+)",
        r"Revenue[s]?\s+\$?([\d,]+)",
        r"Total revenue[s]?\s+\$?([\d,]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)

    return None


def read_filing(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


if __name__ == "__main__":

    filing_paths = list(
        Path("data/sec-edgar-filings").rglob("full-submission.txt")
    )

    for path in filing_paths:

        text = read_filing(path)

        revenue = extract_revenue(text)

        print("\n--------------------")
        print(path)
        print("Revenue:", revenue)