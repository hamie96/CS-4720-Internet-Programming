

from services.db import DbConnector


connector = DbConnector("chinook.db")


#  List of customers with names and customer ids
def customer_list():
    """
    Return a list of customers with name and id
    :return:
        """
    # return connector.do_command("select CustomerId, FirstName, LastName from customers")
    return connector.do_command("select * from customers")


# Given a customer id, give a list of invoices for that customer
def invoices_for_customer(customer_id):
    return connector.do_command("select * from Invoices where CustomerId = ?", [customer_id])


# Given an invoice id, give a list of invoice items for that invoice
def items_for_invoice(invoice_id):
    return connector.do_command("select * from invoice_items where InvoiceId = ?", [invoice_id])


def invoice_items_for_customer(customer_id):
    cmd = """
        select inv.Total, inv.InvoiceId,  ii.InvoiceLineId
        from invoices as inv, invoice_items as ii
        where inv.InvoiceId = ii.InvoiceId and inv.CustomerId = ?
    """
    return connector.do_command(cmd, [customer_id])


def items_invoices_customers():
    cmd = """
        select cu.CustomerId, cu.FirstName, cu.LastName, inv.InvoiceId, inv.Total
        from invoices as inv, invoice_items as ii, customers as cu 
        where inv.InvoiceId = ii.InvoiceId and inv.CustomerId = cu.CustomerId
    """
    return connector.do_command(cmd)


if __name__ == "__main__":
    # print(customer_list())
    # print(invoices_for_customer(1))
    # print(items_for_invoice(98))
    # print(invoice_items_for_customer(2))
    iic = items_invoices_customers()
    tot_len = 0
    for cust in customer_list():
        ii = invoice_items_for_customer(cust[0])
        tot_len += len(ii)
    print(len(iic), tot_len)
