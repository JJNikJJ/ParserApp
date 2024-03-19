import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"}


def download(url):
    response = requests.get(url, headers=headers, stream=True)
    r = open("C:\\Users\\ALFA\\Documents\\image\\" + url.split("/")[-1], "wb")
    for chunk in response.iter_content(1024 * 1024):
        r.write(chunk)
    r.close()


def get_html():
    for count in range(1, 8):

        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")  # html.parser
        data = soup.find_all("div", class_="w-full rounded border")
        for el in data:
            card_url = "https://scrapingclub.com" + el.find("a").get("href")
            yield card_url


def array():
    for card_url in get_html():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")  # html.parser
        data = soup.find("div", class_="my-8 w-full rounded border")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4", class_="my-4 card-price").text
        text = data.find("p", class_="card-description").text
        img = "https://scrapingclub.com" + data.find("img", class_="card-img-top").get("src")
        download(img)
        yield name, price, text, img
