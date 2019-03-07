import requests



url = "http"//ksuwe.kennesaw.edu.........."



r = requests..get(url)



print("response code", r.status_code)



print("headers", r.headers)  # returns as distionary



print("content type", r.headers["Content-Type"])



print("content length", r.headers["Content-Length"])



print(r.text)



# print(r.json()) 

