import pandas as pd

df = pd.read_excel(
    io="Dataset/supermarkt_sales.xlsx",
    engine="openpyxl",
    sheet_name="Sales",
    skiprows=3,
    usecols="B:R",
    nrows=1000,
)

print(df)
