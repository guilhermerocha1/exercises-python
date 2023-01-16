from parsel import Selector
import requests


URL_BASE = 'https://books.toscrape.com/catalogue/'
next_page_url = 'page-1.html'

while next_page_url:
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)

    titles = selector.css(".product_pod h3 a::attr(title)").getall()
    princes = selector.css(".product_price .price_color::text").getall()

    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").get()
        print(title, price)

    next_page_url = selector.css(".next a::attr(href)").get()
