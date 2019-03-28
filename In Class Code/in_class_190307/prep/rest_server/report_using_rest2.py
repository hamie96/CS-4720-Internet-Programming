
from services import chinook_services
import requests
from json_with_dates import loads

PORT = 54321

r = requests.get("http://localhost:{}/chinook/customer".format(PORT))
customers = loads(r.text)
#print(customers)

for customer_row in customers:
    cust_id = customer_row[0]
    # print(cust_id)

    r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/customer/{}".format(PORT, cust_id))
    inv_ii = loads(r.text)
    # print(invoices)
    num_tracks = len(inv_ii)

    total_invoice = 0
    for i in range(num_tracks):
        if i == 0:
            total_invoice += inv_ii[i][0]
        elif inv_ii[i][1] != inv_ii[i-1][0]:
            total_invoice += inv_ii[i][0]
        else:
            pass  # do nothing

    template = "{:3}  {:15}  {:15}  {:3}  {:8.2f}"
    line = template.format(cust_id, customer_row[2],
                           customer_row[1], num_tracks, total_invoice)
    print(line)
