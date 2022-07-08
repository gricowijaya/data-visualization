import pandas as pd
import matplotlib.pyplot as plt
import json
import requests as req
import numpy as np
import csv
from markdown import markdown


def get_data_and_write(url):
    # print(filename[0:16])  # only get the ./resource/json/data.json/strings
    # print(womanFashions[29:29])  # only get the http://ml.cakeplabs.com:1891/
    # only get the path-name for the filename /woman-fashions
    # print(womanFashions[29:50])

    prefix_json_filename = f"./resource/json/"
    prefix_csv_filename = f"./resource/csv/"
    filename = f'{url[29:50]}'

    try:
        # get the data from the API
        res = req.get(url)
        data = res.json()

        # write to json
        file = open(f'{prefix_json_filename}{filename}.json', "w")
        file.write(json.dumps(data))
        file.close

        # write to csv
        with open(f'{prefix_json_filename}{filename}.json', encoding='utf8') as inputFile:
            data = pd.read_json(inputFile)
        data.to_csv(f'{prefix_csv_filename}{filename}.csv',
                    encoding='utf8', index=False)
    except:
        print('Data is not saved')
    else:
        print(f'CSV data is saved in {prefix_csv_filename}{filename}.csv')
        print(f'JSON data is saved in {prefix_csv_filename}{filename}.json')


def filter_data_by_price(url, start_value, end_value):
    prefix_json_filename = f"./resource/json/"
    prefix_csv_filename = f"./resource/csv/"
    filename = f'{url[29:50]}'
    data = pd.read_csv(f"{prefix_csv_filename}{filename}.csv", index_col='id')
    print(data[0:5])

    # for item in data:
    #     if item['price'] > start_value and item['price'] < end_value:
    #         # add the item name and convert the item price into string
    #         # print(item['title'] + suffix + str(item['price']))
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


def read_csv_data(filename):
    # with open('./resource/csv/manFashions.csv') as data:
    #     csv_reader = csv.reader(data, delimiter=',')
    #     line_count = 0
    #     for row in csv_reader:
    #         if line_count == 0:
    #             print(f'Column name for this are {", ".join(row)}')
    #             line_count += 1
    #         else:
    #             print(f'Column name for this are {", ".join(row)}')
    #             line_count += 1
    #     print(f'Processed {line_count} lines.')

    data = pd.read_csv(f"./resource/csv/{filename}.csv", index_col='id')
    print(data[0:5])
