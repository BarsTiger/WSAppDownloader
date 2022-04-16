import requests
import re

api_url = "https://store.rg-adguard.net/api/GetFiles"


def get_files(product_url):
    print("Collecting links...")
    r = requests.post(api_url, data={
        'type': 'url',
        'url': product_url,
        'ring': 'Slow',
        'lang': 'en-US'
    }).text

    links = dict()
    for line in r.split("\n"):
        try:
            link = re.search('<tr style.*<a href=\"(?P<url>.*)"\s.*>(?P<text>.*)<\/a>', line).groups()
            if re.search("_(x86|x64|neutral).*appx|msix(|bundle)$", link[1]):
                links[link[1]] = link[0]
        except AttributeError:
            pass

    return links
