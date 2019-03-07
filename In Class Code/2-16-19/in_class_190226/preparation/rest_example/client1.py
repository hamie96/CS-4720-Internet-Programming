import requests

PORT = 54321

# r = requests.get("http://localhost:{}/chinook/customer".format(PORT))
# r = requests.get("http://localhost:54321/chinook/customer")
# r = requests.get("http://localhost:{}/chinook/invoice/customer/7".format(PORT))
# r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/78".format(PORT))
# r = requests.get("http://localhost:{}/chinook/invoice-item/invoice".format(PORT))
# r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/customer/1".format(PORT))
r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/customer".format(PORT))
print("status", r.status_code)
# print(r.headers)
for h in sorted(r.headers):
    tmpl = "{:20} {:20}"
    line = tmpl.format(h, r.headers[h])
    print(line)
r.encoding = "UTF-8"
print(r.text)
print(r.encoding)
