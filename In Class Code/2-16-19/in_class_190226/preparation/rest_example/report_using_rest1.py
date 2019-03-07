import requests
from previous.json_with_dates import loads

PORT = 54321

r = requests.get("http://localhost:{}/chinook/customer".format(PORT))
customers = loads(r.text)
#print(customers)

for customer_row in customers:
    cust_id = customer_row[0]
    # print(cust_id)

    r = requests.get("http://localhost:{}/chinook/invoice/customer/{}".format(PORT, cust_id))
    invoices = loads(r.text)
    # print(invoices)

    total_invoice = 0
    num_tracks = 0

    for invoice_row in invoices:
        total_invoice += invoice_row[8]

        r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/{}".format(PORT, invoice_row[0]))
        invoice_items = loads(r.text)
        for invoiceItem_row in invoice_items:
            num_tracks += 1
    template = "{:3}  {:15}  {:15}  {:3}  {:8.2f}"
    line = template.format(cust_id, customer_row[2],
                           customer_row[1], num_tracks, total_invoice)
    print(line)
