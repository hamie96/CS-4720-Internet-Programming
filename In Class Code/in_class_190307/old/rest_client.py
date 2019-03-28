
import requests
import json_with_dates

r = requests.get("http://localhost:54321/chinook/customer")
print(r.text)
print(r.text[0])
print(json_with_dates.loads(r.text))
print(json_with_dates.loads(r.text)[0])

r = requests.get("http://localhost:54321/chinook/customer")
customers = json_with_dates.loads(r.text)

for customer in customers:
    print(customer)

