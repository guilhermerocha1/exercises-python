import requests
from parsel import Selector

image_url_base = "http://books.toscrape.com/"
response = requests.get('http://books.toscrape.com/catalogue/the-grand-design_405/index.html')

title_selector = Selector(text=response.text).css("h1::text").get()
price_selector = Selector(text=response.text).css(".price_color::text").re_first(r"\d+\.\d{2}")
description_selector = Selector(text=response.text).css(".product_page > p::text").get()
image_url_selector = Selector(text=response.text).css("img::attr(src)").get()
availability = Selector(text=response.text).css(".product_main .availability::text").re_first(r"\d")

book = []
book.append({
  "title": title_selector,
  "price": price_selector,
  "description": description_selector,
  "image_url": image_url_base + image_url_selector,
  "availability": availability
})

print(book)