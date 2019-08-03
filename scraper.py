import requests
from bs4 import BeautifulSoup

URL = 'https://www.costco.com/Lenovo-Flex-5-Series-2-in-1-Touchscreen-Laptop---Intel-Core-i7---GeForce-MX130---4K-Ultra-HD---Active-Stylus.product.100408249.html'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers =headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup. prettify())