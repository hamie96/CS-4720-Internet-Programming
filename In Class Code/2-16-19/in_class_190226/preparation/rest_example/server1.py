

import http.server
import socketserver
import re
from services.chinook_services import items_for_invoice, invoices_for_customer, \
    customer_list, items_invoices_customers
from previous.json_with_dates import dumps
import logging

PORT = 54321


class RestServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        m = re.fullmatch(r"/chinook/customer", self.path)
        if m:
            data = customer_list()
        else:
            m = re.fullmatch(r'/chinook/invoice/customer/(\d+)', self.path)
            if m:
                cust_id = int(m.group(1))
                data = invoices_for_customer(cust_id)
            else:
                m = re.fullmatch(r"/chinook/invoice-item/invoice/(\d+)", self.path)
                if m:
                    inv_id = int(m.group(1))
                    data = items_for_invoice(inv_id)
                else:
                    m = re.fullmatch("/chinook/invoice-item/invoice/customer", self.path)
                    if m:
                        data = items_invoices_customers()
                    else:
                        data = None

        if data:
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            edat = dumps(data)
            logging.debug(edat)
            self.wfile.write(edat.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write("invalid path: {}".format(self.path).encode("utf-8"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    server_address = ('', PORT)
    httpd = socketserver.TCPServer(server_address, RestServer)
    httpd.serve_forever()



