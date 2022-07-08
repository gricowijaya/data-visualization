from markdown import markdown
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests as req
import numpy as np
import csv
import sys


def get_data_and_write(url):

    # print(filename[0:16])  # only get the ./resource/json/data.json/strings
    # print(womanFashions[29:29])  # only get the http://ml.cakeplabs.com:1891/
    # only get the path-name for the filename /woman-fashions
    # print(womanFashions[29:50])

    # only the get path name since it started from the 29th characters
    json_filename = f"./resource/json/{url[29:50]}.json"
    csv_filename = f"./resource/csv/{url[29:50]}.csv"
    json_path = Path(json_filename)
    csv_path = Path(csv_filename)

    # check If the file exists or not
    if (json_path.is_file() or csv_path.is_file()) :
        pass
    
    try:
        # get the data from the API
        res = req.get(url)
        data = res.json()

        # write to json
        file = open(json_filename, "w")
        file.write(json.dumps(data))
        file.close

        # write to csv
        with open(json_filename, encoding='utf8') as inputFile:
            data = pd.read_json(inputFile)
        data.to_csv(csv_filename,
                    encoding='utf8', index=False)
    except:
        print('Data is not saved')
        print(sys.exc_info())
    else:
        print(f'CSV data is saved in {csv_filename}')
        print(f'JSON data is saved in {json_filename}')


def get_csv_data(filename):
    data = pd.read_csv(filename, index_col='id')
    return data[0:5]
    pass


def filter_data_by_price(url, start_value, end_value):
    id = []
    price = []

    json_filename = f"./resource/json/{url[29:50]}.json"
    csv_filename = f"./resource/csv/{url[29:50]}.csv"

    data = get_csv_data(csv_filename)
    # print(data[0:])

    # for item in data:
    #     if int(item[0:]['price']) > f'{start_value}' and int(item[0:]['price']) <= end_value:
    #         id.append(item['id'])
    #         price.append(item['price'])
    create_graph(csv_filename.capitalize(), id, price)
    pass


def create_graph(plot_title, title, price):
    x = title
    y = price
    plt.plot(x, y)
    plt.title(plot_title)
    plt.xlabel("ID Product")
    plt.ylabel("Price")
    plt.show()
    pass


def create_table():
    table = f"""
    |ID Product | Price |
    |-----------|-------|
    |-----------|-------|
    """
    html = markdown(table, extensions=["tables"])
    print(html)
    pass
