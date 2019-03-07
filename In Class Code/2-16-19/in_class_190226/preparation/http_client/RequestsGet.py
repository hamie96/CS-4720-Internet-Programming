
import requests

r = requests.get("http://ksuweb.kennesaw.edu/~bsetzer/4720sp19/nanoc/output/index.html")
print("status", r.status_code)
print(r.headers)
for h in sorted(r.headers):
    tmpl = "{:20} {:20}"
    line = tmpl.format(h, r.headers[h])
    print(line)
print(r.text)
