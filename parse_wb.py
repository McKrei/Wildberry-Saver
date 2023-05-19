import requests
import time

def get_products(url):
    # Получаем список продуктов из JSON-ответа на запрос
    products = requests.get(url).json()['data']['products']
    return products

def get_urls(query):
    # Генерируем список URL-адресов для запросов, включая параметры запроса и номера страницы
    urls = [
        f'https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query={query}&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1, 61)
    ]
    return urls

all_products = []
start = time.time()

def start_parsing():
    query = input("Введите запрос: ")
    urls = get_urls(query)

    for url in urls:
        products = get_products(url)
        all_products.extend(products)

# Запускаем парсинг
start_parsing()

print(time.time() - start)
print(len(all_products))
