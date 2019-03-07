


import requests
from previous import json_with_dates

PORT = 8000

response = requests.get("http://localhost:8000/chinook/items/invoices/customers")
table = json_with_dates.loads(response.text)

for row in table:
    print(row)

