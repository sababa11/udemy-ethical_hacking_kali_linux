import requests
import re
from urllib.parse import urlparse, urljoin


def extract_links(url):
    response = requests.get(url)
    # print(response.text)
    return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))

target_url = "http://testphp.vulnweb.com"
href_links = extract_links(target_url)

for i, link in enumerate(href_links):
    link = urljoin(target_url, link)
    print(i, link)
