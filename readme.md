# Learning Data Visualization

This Visualization is using K-Means Algorithm to classify the User Data. K-Means Algorithm is an unsupervised algorithm and it is can be use in this case study. We need to define the K value then
we'll define the cluster centroids. The algorithm simply describe in the below steps.

1. Initialize the k value, this value will become the cluster centroids or we can called it mean.
2. Categorized each item to the closest cluster centroids.
3. Repeat the process for some iterations until the dataset is clusterized

In the pseudocode the algorithm is written as follows:

```
BEGIN

Initialize k means with random values
  For a given number of iterations:
    iterate through the items:
      Find the mean, closest to the item --> this is by calculating the euclidian distance between the item and the mean

      Assign the item to the mean cluster.

      Update the mean by shifting the average of the items in that cluster.

    When we already find the cluster then we can get the k - means 
END
```

Data Source : MySQL

## We can create the API with node RED

## To Install Dependencies

```
make init
```

## To Run

```
make run clean
```

### REFERENCES

https://www.ibm.com/cloud/learn/unsupervised-learning#toc-applicatio-omDVIJIs
https://www.geeksforgeeks.org/k-means-clustering-introduction/
kj
https://www.cdata.com/kb/tech/mysql-python-pandas.rst
https://www.youtube.com/watch?v=QhhQE9FmC14
