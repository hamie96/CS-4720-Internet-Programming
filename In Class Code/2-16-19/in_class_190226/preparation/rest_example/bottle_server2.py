
# just their basic example

from bottle import route, run, response
from services.chinook_services import items_for_invoice, invoices_for_customer, \
        customer_list, invoice_items_for_customer, items_invoices_customers
from previous.json_with_dates import dumps


@route("/chinook/customer")
def customers():
    response.content_type = "application/json"
    data = customer_list()
    return dumps(data)
    # return data

@route("/chinook/invoice/customer/<customer_id:int>")
def invoices(customer_id):
    response.content_type = "application/json"
    data = invoices_for_customer(customer_id)
    return dumps(data)

@route("/chinook/invoice-item/invoice/<invoice_id:int>")
def items(invoice_id):
    response.content_type = "application/json"
    data = items_for_invoice(invoice_id)
    return dumps(data)


@route("/chinook/invoice-item/invoice/customer")
def items_invoices_customers_all():
    response.content_type = "application/json"
    data = items_invoices_customers()
    return dumps(data)


@route("/chinook/invoice-item/invoice/customer/<customer_id:int>")
def items(customer_id):
    response.content_type = "application/json"
    data = invoice_items_for_customer(customer_id)
    return dumps(data)

run(host='localhost', port=54321)

