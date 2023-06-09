import grequests
import time
import schedule
from . import db
from .models import Query
from .crud import add_product_history_data
from send_mail import send_email


def search_right_product(query):
    urls = [
        f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query={query}&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1, 61)]
    rs = (grequests.get(u) for u in urls)
    all_products = []

    for el in grequests.map(rs, size=350):
        try:
            if el.status_code == 200:
                all_products += el.json()['data']['products']
        except Exception as err:
            print(err)

    # all_products = [product for f in lst for product in f.json()['data']['products']]
    result = []
    for product in all_products:
        dct = {'product_id': product.get('id'), 'salePriceU': product.get('salePriceU') / 100,
               'name': product.get('name')}
        result.append(dct)
    return result


def run_task():
    queries = Query.query.all()  # Получаем все запросы из базы
    for query in queries:
        all_products = search_right_product(query.query_title)
        for i in range(0, len(all_products)): # Идем по списку всех товаров
            product_name = all_products[i].get("name")
            priced = all_products[i].get('salePriceU')
            current_price = int(priced/100)
            product_id = all_products[i].get('product_id')
            data = add_product_history_data(product_id, product_name, current_price, query)
            if data:
                send_email(*data)


def main():
    schedule.every(6).hours.do(run_task)
    while True:
        try:
            schedule.run_pending()
        except Exception as E:
            time.sleep(1)


if __name__ == '__main__':
    main()

