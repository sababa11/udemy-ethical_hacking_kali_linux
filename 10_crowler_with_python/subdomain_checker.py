import requests

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException as e:
        # print("No such subdomain: " + url)
        pass

target_url = "facebook.com"

with open("subdomains.txt", "r") as file:
    subdomains = file.read().splitlines()
    file.close()

result = []

for i, subdomain in enumerate(subdomains):
    test_url = "https://" + subdomain + "." + target_url
    responce = request(test_url)
    if responce:
        print("Subdomain %s exists: " % test_url)
        result.append(test_url)
        pass
