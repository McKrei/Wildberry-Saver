import grequests
import time


def search_right_product(search):
    urls = [
        f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query={search}&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1, 61)]

    rs = (grequests.get(u) for u in urls)
    lst = grequests.map(rs)
    all_products = [product for f in lst for product in f.json()['data']['products']]
    result = []
    for product in all_products:
        dct = {'product_id': product.get('id'), 'salePriceU': product.get('salePriceU') / 100,
               'name': product.get('name')}
        result.append(dct)
    return result

# ToDo: Добавить функцию получения из БД списка запросов

# ToDo: Добавить функцию записи данных в БД
