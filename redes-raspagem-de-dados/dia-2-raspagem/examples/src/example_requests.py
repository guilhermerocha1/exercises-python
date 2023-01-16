import requests
import time

response = requests.get('http://books.toscrape.com/')
# print(response.status_code)
# print(response.headers)
# print(response.text)

for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response.status_code)
    time.sleep(5)