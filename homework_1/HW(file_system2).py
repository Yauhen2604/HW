import json


def purchase():
    user_dict = {}
    name = []
    price = []
    product = input('enter name prod')
    price_product = int(input('enter prise'))
    if product != 'stop':
        name.append(product)
        price.append(price_product)
        user_dict = dict(zip(name, price))
    with open('user_purchases.json', 'w', encoding='utf-8') as f:
        json.dump(user_dict, f, ensure_ascii=False)


purchase()
with open('user_purchases.json') as f:
    purchases = json.load(f)
    res = 0
    for i in purchases.values():
        res = res + i
    print(res)
