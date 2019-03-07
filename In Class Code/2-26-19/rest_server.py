
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
import re
from services import chinook_services
import json_with_dates

class RestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pass
        # decide which path is being used
        # self.path is the path from the request

        m = re.fullmatch("/chinook/customer", self.path)

        if m :
            # matches the first regex
            data = chinook_services.customer_list()
        else:
            # did not match
            m = re.fullmatch(r"/chinook/invoice/customer/(\d+)", self.path)
            if m:
                cust_id = int(m.group(1))
                data = chinook_services.invoices_for_customer(cust_id)
            else:
                m = re.fullmatch(r"/chinook/invoice-item/invoice/(\d+)", self.path)
                if m:
                    invoice_id = int(m.group(1))
                    data = chinook_services.items_for_invoice(invoice_id)
                else:
                    m = re.fullmatch(r"/chinook/items/invoices/customers", self.path)
                    data = chinook_services.items_invoices_customers()
                    if m:
                        pass
                    else:
                        data = None


        # send appropriate response back

        if data:
            # path matched, good response
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            jdata = json_with_dates.dumps(data)
            self.wfile.write(jdata.encode("UTF-8"))
        else:
            # path did not match
            self.send_response(404)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write("invalid path: {}".format(self.path).encode("utf-8"))


PORT = 8000


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
server_address = ('', PORT)
httpd = HTTPServer(server_address, RestHandler)
httpd.serve_forever()
