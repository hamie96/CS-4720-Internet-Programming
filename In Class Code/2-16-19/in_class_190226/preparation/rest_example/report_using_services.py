from services import chinook_services

customers = chinook_services.customer_list()

for customer_row in customers:
    cust_id = customer_row[0]
    invoices = chinook_services.invoices_for_customer(cust_id)

    total_invoice = 0
    num_tracks = 0
    for invoice_row in invoices:
        total_invoice += invoice_row[8]

        invoice_items = chinook_services.items_for_invoice(invoice_row[0])
        for invoiceItem_row in invoice_items:
            num_tracks += 1
    template = "{:3}  {:15}  {:15}  {:3}  {:8.2f}"
    line = template.format(cust_id, customer_row[2],
                           customer_row[1], num_tracks, total_invoice)
    print(line)
