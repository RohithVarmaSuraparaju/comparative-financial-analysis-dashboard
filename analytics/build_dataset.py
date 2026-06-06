import requests
import pandas as pd

companies = {
    "NVDA": "1045810",
    "AMD": "2488",
    "INTC": "50863"
}

headers = {
    "User-Agent": "Rohith your_email@example.com"
}

def get_company_facts(cik):
    cik = str(cik).zfill(10)

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    response = requests.get(url, headers=headers)

    return response.json()


def get_metric(data, metric_name):

    try:
        metric = data["facts"]["us-gaap"][metric_name]["units"]["USD"]

        rows = []

        for item in metric:
            if item.get("form") == "10-K":

                rows.append({
                    "fy": item.get("fy"),
                    "value": item.get("val")
                })

        return rows

    except:
        return []


all_rows = []

for company, cik in companies.items():

    data = get_company_facts(cik)

    revenues = get_metric(
        data,
        "RevenueFromContractWithCustomerExcludingAssessedTax"
    )

    for r in revenues:

        all_rows.append({
            "company": company,
            "year": r["fy"],
            "revenue": r["value"]
        })

df = pd.DataFrame(all_rows)

df = (
    df.sort_values(["company", "year"])
      .drop_duplicates(
          subset=["company", "year"],
          keep="last"
      )
)

print(df)

df.to_csv(
    "financial_metrics.csv",
    index=False
)

print("\nSaved financial_metrics.csv")