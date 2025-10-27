from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

# url = input("Enter a website for extraction process: ")
# url = "http://testphp.vulnweb.com"
url = "https://www.hit.ac.il"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data)

for i, link in enumerate(soup.find_all("a")):
    link = urljoin(url, link.get("href"))
    print(i, link)
