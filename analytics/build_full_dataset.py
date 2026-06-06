import requests
import pandas as pd

companies = {
    "NVDA": "1045810",
    "AMD": "2488",
    "INTC": "50863"
}

HEADERS = {
    "User-Agent": "Rohith your_email@example.com"
}


def get_company_facts(cik):

    cik = str(cik).zfill(10)

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()


def get_metric(data, metric_name):

    try:

        metric = (
            data["facts"]["us-gaap"]
            [metric_name]["units"]["USD"]
        )

        results = {}

        for item in metric:

            if item.get("form") != "10-K":
                continue

            fy = item.get("fy")

            if fy is None:
                continue

            results[fy] = item.get("val")

        return results

    except:
        return {}


rows = []

for company, cik in companies.items():

    print(f"Processing {company}")

    data = get_company_facts(cik)

    revenue = get_metric(
        data,
        "RevenueFromContractWithCustomerExcludingAssessedTax"
    )

    assets = get_metric(
        data,
        "Assets"
    )

    liabilities = get_metric(
        data,
        "Liabilities"
    )

    for year in revenue.keys():

        rows.append({
            "company": company,
            "year": year,
            "revenue": revenue.get(year),
            "assets": assets.get(year),
            "liabilities": liabilities.get(year)
        })

df = pd.DataFrame(rows)

df = df.sort_values(
    ["company", "year"]
)

df.to_csv(
    "financial_full.csv",
    index=False
)

print(df.head())
print("\nSaved financial_full.csv")