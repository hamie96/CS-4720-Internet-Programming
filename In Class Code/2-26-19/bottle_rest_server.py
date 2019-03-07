
from bottle import route, run, response

from services.chinook_services import item_invoices_customers, items_for_invoice,       invoices_for_customer, customer_list, invoice_items_for_customer

from json_with_dates import dumps

@route('/chinook/customer')
def customers():
        data = customer_list()
        response.content_type = 'application/json'
        return dumps(data)

@route('/chinook/invoice-item/invoice/')
def invoices(customer_id):
    data = items_for_invoice(item_id)

run(host='localhost', port=8080)
