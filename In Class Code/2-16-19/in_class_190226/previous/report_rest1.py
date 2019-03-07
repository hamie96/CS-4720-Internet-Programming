
import requests
from previous import json_with_dates

PORT = 8000

custResponse = requests.get("http://localhost:8000/chinook/customer")
# print(custResponse.text)

# print(custResponse.text[0])
customers = json_with_dates.loads(custResponse.text)
# print(customers)
# print(customers[0])

for customer in customers:
    cust_id = customer[0]
    invoiceResponse = requests.get(
        "http://localhost:{}/chinook/invoice/customer/{}".format(PORT, cust_id)
    )
    invoices = json_with_dates.loads(invoiceResponse.text)
    # print(invoices)
    # print(invoices[0])

    total = 0

    for invoice in invoices:
        invoice_id = invoice[0]
        total += invoice[8]


        item_response = requests.get(
            "http://localhost:{}/chinook/invoice-item/invoice/{}".format(PORT, invoice_id)
        )
        items = json_with_dates.loads(item_response.text)

        count = len(items)

    template = "{:3}  {:15}  {:15}  {:3}  {:8.2f}"
    line = template.format(cust_id, customer[2],
                           customer[1], count, total)
    print(line)





