import pandas
import matplotlib.pyplot as plt
import json
import requests as req


def write_woman_fashions_data(url):
    womanFashions = []
    res = req.get(url)
    data = res.json()
    print(data)
    # for i in data:
    #     title = data['title']
    #     womanFashions.append(title)
    # checking the output
    # print(womanFashions)
    pass
