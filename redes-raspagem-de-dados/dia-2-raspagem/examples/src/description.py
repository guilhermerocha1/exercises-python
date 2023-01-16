from parsel import Selector
import requests

URL_BASE = 'https://books.toscrape.com/catalogue/'

response = requests.get(URL_BASE + 'page-1.html')
selector = Selector(text=response.text)

href = selector.css(".product_pod h3 a::attr(href)").get()
detail_page_url = URL_BASE + href

details_response = requests.get(detail_page_url)
details_selector = Selector(text=details_response.text)

details = details_selector.css(".product_page h2::text").get()

print(details)