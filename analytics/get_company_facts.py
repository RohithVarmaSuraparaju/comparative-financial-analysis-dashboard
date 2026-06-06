import requests
import pandas as pd

companies = {
    "NVDA": "1045810",
    "AMD": "2488",
    "INTC": "50863"
}

def get_revenue(cik):
    cik = str(cik).zfill(10)

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    headers = {
        "User-Agent": "Rohith your_email@example.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed for {cik}")
        return None

    data = response.json()

    try:
        revenue_data = data["facts"]["us-gaap"]["RevenueFromContractWithCustomerExcludingAssessedTax"]["units"]["USD"]

        rows = []

        for item in revenue_data[-10:]:
            rows.append({
                "fy": item.get("fy"),
                "value": item.get("val")
            })

        return pd.DataFrame(rows)

    except Exception as e:
        print(e)
        return None


for company, cik in companies.items():
    print(f"\n{company}")
    print(get_revenue(cik))