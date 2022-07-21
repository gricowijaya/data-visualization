import numpy as np # for number manipulation
import matplotlib.pyplot as plt # for plot
import pandas as pd
from pandas.core.common import random_state # for data manipulation
import seaborn as sns # for plotting
import datetime as dt


# Library for clustering
from sklearn.datasets import make_blobs # dummy library
from sklearn.preprocessing import StandardScaler # dummy library
from sklearn.cluster import KMeans # for KMeans algorithm
from sklearn.decomposition import PCA # for KMeans algorithm
from yellowbrick.cluster import KElbowVisualizer # for finding the optimal k value
# from sklearn.metrics import silhouette_score 
from collections import Counter


def create_data(): 
    filename = "./resource/csv/woman-fashions.csv"

    df = pd.read_csv(filename)
    print(f'df.head() \n { df.head() }')
    # Univariate Analysis
    print(f'df.describe \n { df.describe() }')

    data = df[['id','price']]
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    print(f'## data_scaled \n { data_scaled }') # the total 

    # Generate the elbow_range
    model = KMeans()
    visualizer = KElbowVisualizer(model, k=(1,12)).fit(data_scaled)
    # visualizer.show()

    # print(df.info)
    # column = ['price', 'condition_int']

    kmeans = KMeans(n_clusters=4, init='k-means++', algorithm="elkan", random_state=1)
    # label = kmeans.fit_predict(data_scaled)
    # print(f'## label  \n { label }')

    # filtered_label0 = data_scaled[label == 0]
    # plt.scatter(filtered_label0[:,0] ,filtered_label0[:,1])

    label = kmeans.fit_predict(data_scaled)
    print(f'## label  \n { label }')

    filtered_label0 = data_scaled[label == 0]
    filtered_label1 = data_scaled[label == 1]
    filtered_label2 = data_scaled[label == 2]
    filtered_label3 = data_scaled[label == 3]
    plt.scatter(filtered_label0[:,0] ,filtered_label0[:,1])
    plt.scatter(filtered_label1[:,0] ,filtered_label1[:,1])
    plt.scatter(filtered_label2[:,0] ,filtered_label2[:,1])
    plt.scatter(filtered_label3[:,0] ,filtered_label3[:,1])
    plt.show()

    # plt.plot(range(1,11), wcss)
    # plt.title('Elbow Method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss values')
    # plt.show()

    pass

# Function not working
def create_data_tested_not_working():
    filename = "./resource/csv/woman-fashions.csv"

    df = pd.read_csv(filename, encoding="ISO-8859-1")

    data = df[['id','price']]
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    print(f'## data_scaled \n { data_scaled }') # the total 

    # Generate the elbow_range
    model = KMeans()
    visualizer = KElbowVisualizer(model, k=(1,12)).fit(data_scaled)
    # visualizer.show() # uncomment trace the results


    # Create the k-means
    # kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300,algorithm="elkan", random_state=0).fit(data_scaled)
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300,algorithm="elkan", random_state=0)
    label = kmeans.fit_predict(data_scaled)
    print(f'## label  \n { label }')

    filtered_label0 = data_scaled[label == 0]
    plt.scatter(filtered_label0[:,0] ,filtered_label0[:,1])

    # trace the kmeans object value
    # print(f'kmeans.labels_ = { kmeans.labels_ }') # the predicted labels
    # print(f'kmeans.inertia_ = { kmeans.inertia_ }') # the total 
    # print(f'kmeans.n_iter_ = {kmeans.n_iter_}')
    # print(f'kmeans.cluster_centers_ = { kmeans.cluster_centers_ }')
    # print(f'Counter(kmeans.labels_)= { Counter(kmeans.labels_) }')

    pass

# Creating Dummy Data
def dummy_data():
    data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6, random_state=50)

    points = data[0]
    kmeans = KMeans(n_clusters=4)

    # fit kmeans object to data
    kmeans.fit(points)

    # print location of clusters learned by kmeans object
    print(kmeans.cluster_centers_)

    # save new clusters for chart
    y_km = kmeans.fit_predict(points)

    plt.scatter(points[y_km == 0,0], points[y_km ==0,1], s=100, c='red')
    plt.scatter(points[y_km == 1,0], points[y_km ==1,1], s=100, c='black')
    plt.scatter(points[y_km == 2,0], points[y_km ==2,1], s=100, c='blue')
    # plt.scatter(points[y_km == 3,0], points[y_km ==3,1], s=100, c='cyan')
    plt.show()
    pass
