

import requests
from json_with_dates import loads

PORT = 54321

r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/customer".format(PORT))
rows = loads(r.text)

last_cust_id = -1
last_invoice_id = -1
last_fname = None
last_lname = None
running_tot = None
running_count = None

for (cust_id, fname, lname, inv_id, inv_tot) in rows:
    if cust_id != last_cust_id:
        if last_cust_id >= 0:
            template = "{:3}  {:15}  {:15}  {:3}  {:8.2f}"
            line = template.format(last_cust_id, last_fname,
                                   last_lname, running_count, running_tot)
            print(line)
        running_tot = 0
        running_count = 0
        last_cust_id = cust_id
        last_fname = fname
        last_lname = lname
    elif inv_id != last_invoice_id:
        running_tot += inv_tot
        last_invoice_id  = inv_id
    running_count += 1

template = "{:3}  {:15}  {:15}  {:3}  {:8.2f}"
line = template.format(last_cust_id, last_fname,
                       last_lname, running_count, running_tot)
print(line)
