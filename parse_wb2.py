from datetime import datetime
import requests
import time
import datetime
import connect_base
from datetime import date


def get_products(url):
    products = requests.get(url).json()['data']['products']
    return products






start = time.time()
def search_right_product(search):
    products = []
    urls = [
        f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query={search}&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1, 61)]
    for url in urls:
        products += get_products(url)

    return products


# print(len(all_products))
# print(len(all_products[1]))





current_date = date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()


#user = connect_base.User(name='Alex', email='Podiyachiy-a@mail.ru')

# connect_base.session.add(user)
# connect_base.session.commit()

user_input = input('Кто ты пользователь? ')

users = connect_base.session.query(connect_base.User).all()
for userx in users:
    print(userx.email)
    if user_input == userx.name:
        print(f'Привет {userx.name} !')
        search = input('Что будем искать? - ')  # Вводим запрос
        discount_amount = input('Каков размер скидки для этого товара устроит? - ')
        print('Хорошо. Сейчас произведем мониторинг и сформируем базу')

        queryx = connect_base.Query(query=search, discount=discount_amount)  # Записываем в базу запрос и размер скидки
        connect_base.session.add(queryx)  # Отправляем в базу
        connect_base.session.commit()

        long_lst = len(search_right_product(search)) # Длина списка товаров
        all_products = search_right_product(search) # Список всех полученных товаров

        for i in range(0, long_lst): # Идем по списку всех товаров
            title = all_products[i].setdefault("name")
            priced = all_products[i].setdefault('salePriceU')
            price = float(priced/100)
            id_product = all_products[i].setdefault('id')
            brand_product = all_products[i].setdefault('brand')
            print(title, 'стоит ', price, ' рублей')


            productsx = connect_base.Product(product_id=id_product, name=title, previous_price=price, price=price, updated_at=current_date_time) # Запись в БД уникальный id-продукта, наименование его
                                                                                                                                                    # и, для текущего запроса, цена
            connect_base.session.add(productsx) # Отправляем в базу
            connect_base.session.commit()

            # notificationx = connect_base.Notification(products_id=id_product, previous_price=price, current_price=0, created_at=datetime.now)
            #
            # connect_base.session.add(notificationx)  # Отправляем в базу
            # connect_base.session.commit()


    else:
        print('Такого пользователя нет пока  ')



# добавляем запись в таблицу
# user = User(name='John', age=30)
# session.add(user)
# session.commit()


# получаем записи из таблицы
# users = session.query(User).all()
# for user in users:
#     print(user.id, user.name, user.age)


print(time.time() - start)

# for k, v in all_products[15].items():
#     print(k, v)
