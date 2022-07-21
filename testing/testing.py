from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

def create_data():
    data = make_blobs(n_samples=200, n_features=20, centers=4, cluster_std=1.6, random_state=50)
    points = data[0]
    plt.scatter(data[0][:,0], data[0][:,1], c=data[1], cmap='viridis')
    plt.xlim(-15,15)
    plt.ylim(-15,15)
    plt.show()
    pass
