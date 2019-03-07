
import requests

url = "http://ksuweb.kennesaw.edu/~bsetzer/4720sp19/nanoc/output/notes/module04/m04C2-requests-package/"

r = requests.get(url)

print("response code", r.status_code)

print("headers", r.headers)

print("content type", r.headers["Content-Type"])

print("content length", r.headers["Content-Length"])

print(r.text)
# print(r.json())


