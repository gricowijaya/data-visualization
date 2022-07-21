from markdown import markdown
from pathlib import Path
from sklearn.cluster import KMeans  # For Clustering
from sklearn.preprocessing import MinMaxScaler  # For Preprocessing
from sklearn.datasets import make_blobs  # For Preprocessing
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests as req
import numpy as np
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
    if (json_path.is_file() or csv_path.is_file()):
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


def create_graph(url, start_value, end_value):

    # json_filename = f"./resource/json/{url[29:50]}.json"
    # csv_filename = f"./resource/csv/{url[29:50]}.csv"

    # # data = get_csv_data(csv_filename)
    # data = pd.read_csv(csv_filename)

    # km = KMeans(n_clusters=5)

    # y_predicted = km.fit_predict(data[['id', 'price']])
    # data['cluster'] = y_predicted

    # data1 = data[data.cluster == 0]
    # data2 = data[data.cluster == 1]
    # data3 = data[data.cluster == 2]
    # data4 = data[data.cluster == 3]
    # data5 = data[data.cluster == 4]

    # plt.scatter(data1.id,  data1['price'], color='green')
    # plt.scatter(data2.id,  data2['price'], color='red')
    # plt.scatter(data3.id,  data3['price'], color='black')
    # plt.scatter(data4.id,  data4['price'], color='blue')
    # plt.scatter(data5.id,  data5['price'], color='yellow')
    # plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[
    #             :, 1], color='purple', marker='*', label='centroid')

    # plt.xlabel('id')
    # plt.ylabel('price')
    # plt.show()

    # scaler = MinMaxScaler()

    # data['price'] = scaler.transform(data['price'])
    # scaler.fit(data.id)
    # data.id = scaler.transform(data.id)
    # print(data)

    # y_predicted = km.fit_predict(data[['id', 'price']])
    # data['cluster'] = y_predicted
    # k_rng = range(1, 10)
    # sse = []
    # # for k in k_rng:
    # #     km = KMeans(n_clusters=k)
    # #     km.fit(data[['price']])
    # #     sse.append(km.intertia_)
    # # plt.plot(range(1, 11), sse)
    # # plt.show()

    pass


def elbow_range(url):
    csv_filename = f"./resource/csv/{url[29:50]}.csv"
    data = pd.read_csv(csv_filename)

    km = KMeans(n_clusters=5)
