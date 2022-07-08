import pandas as pd
import matplotlib.pyplot as plt
import json
import requests as req
from markdown import markdown


def write_woman_fashions_data(url):
    womanFashions = []
    res = req.get(url)
    data = res.json()
    file = open(f"./resource/json/womanFashions.json", "w")
    file.write(json.dumps(data))
    file.close
    # pass


def read_woman_fashions_data():
    plot_title = "Woman Fashion Data"
    id = []
    price = []
    suffix = " Item Has Price below Rp 4000 with the amount of Rp "
    # file = open("./resource/womanFashions.json", "r")
    # data = json.load(file)

    with open("./resource/json/womanFashions.json", encoding='utf8') as inputFile:
        data = pd.read_json(inputFile)

    try:
        data.to_csv('./resource/csv/womanFashions.csv',
                    encoding='utf8', index=False)
    except:
        print('Data is not saved')
    else:
        print('CSV data is saved in ./resource/csv/womanFashions.csv')

    # for item in data:
    #     if item['price'] > 4000 and item['price'] < 10000:
    #         # add the item name and convert the item price into string
    #         # print(item['title'] + suffix + str(item['price']))
    #         id.append(item['id'])
    #         price.append(item['price'])
    # create_graph(plot_title, id, price)
    pass


def write_man_fashions_data(url):
    womanFashions = []
    res = req.get(url)
    data = res.json()
    file = open(f"./resource/manFashions.json", "w")
    file.write(json.dumps(data))
    file.close
    # pass


def read_man_fashions_data():
    plot_title = "Man Fashion Data"
    id = []
    price = []
    suffix = " Item Has Price below Rp 4000 with the amount of Rp "
    with open("./resource/json/manFashions.json", encoding='utf8') as inputFile:
        data = pd.read_json(inputFile)

    try:
        data.to_csv('./resource/csv/manFashions.csv', encoding='utf8', index=False)
    except:
        print('Data is not saved')
    else:
        print('CSV data is saved in ./resource/csv/manFashions.csv')
    # for item in data:
    #     if item['price'] > 0 and item['price'] < 10000:
    #         # add the item name and convert the item price into string
    #         print(item['title'] + suffix + str(item['price']))
    #         id.append(item['id'])
    #         price.append(item['price'])
    # create_graph(plot_title, id, price)
    pass


def create_graph(plot_title, title, price):
    x = title
    y = price
    plt.plot(x, y)
    plt.title(plot_title)
    plt.xlabel("ID Product")
    plt.ylabel("Price")
    plt.show()
    # pass


def create_table():
    table = f"""
    |ID Product | Price |
    |-----------|-------|
    |-----------|-------|
    """
    html = markdown(table, extensions=["tables"])
    print(html)
