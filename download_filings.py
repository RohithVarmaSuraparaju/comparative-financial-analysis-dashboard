from sec_edgar_downloader import Downloader

dl = Downloader(
    "CustomerInsightsAI",
    "rohithvarma166@gmail.com",
    "data"
)

companies = ["NVDA", "AMD", "INTC"]

for company in companies:
    dl.get("10-K", company, limit=3)

print("Done")