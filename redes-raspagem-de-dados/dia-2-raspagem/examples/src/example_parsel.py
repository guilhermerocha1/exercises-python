from parsel import Selector
import requests

response = requests.get('http://books.toscrape.com/')
selector = Selector(text=response.text)

titles = selector.css(".product_pod h3 a::attr(title)").getall()
princes = selector.css(".product_price .price_color::text").getall()

for product in selector.css(".product_pod"):
    title = product.css("h3 a::attr(title)").get()
    price = product.css(".price_color::text").re(r"£\d+\.\d{2}")
    print(title, price)

next_page_url = selector.css(".next a::attr(href)").get()