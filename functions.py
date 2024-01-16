import json


def get_products_data():
    with open("static/products.json", "tr", encoding='utf-8') as json_file:
        data = json.load(json_file)

    return data
