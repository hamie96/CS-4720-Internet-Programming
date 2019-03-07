

import sqlite3

conn = sqlite3.connect("services/chinook.db")

try:
    pass
    crs = conn.cursor()

    cmd1 = "select CustomerId, FirstName, LastName from customers"
    crs.execute(cmd1)

    for customer_row in crs:
        # print(customer_row)
        cust_id = customer_row[0]
        num_tracks = 0
        total_invoice = 0

        cmd2 = "select * from Invoices where CustomerId = ?"
        crs2 = conn.cursor()
        crs2.execute(cmd2, [cust_id])
        for invoice_row in crs2:
            total_invoice += invoice_row[8]
            # print(invoice_row)
            crs3 = conn.cursor()
            cmd3 = "select * from invoice_items where InvoiceId = ?"
            crs3.execute(cmd3, [invoice_row[0]])
            for invoiceItem_row in crs3:
                # print(invoiceItem_row)
                num_tracks += 1
        # print("number of tracks ", num_tracks)
        # print("total invoices", total_invoice)
        template = "{:3}  {:15}  {:15}  {:3}  {:8.2f}"
        # id  lastname firstname numberoftracks invoicetotal
        line = template.format(cust_id, customer_row[2],
                      customer_row[1],num_tracks, total_invoice)
        print(line)

finally:
    conn.close()

#  List of customers with names and customer ids
# Given a customer id, give a list of invoices for that customer
# Given an invoice id, give a list of invoice items for that invoice











