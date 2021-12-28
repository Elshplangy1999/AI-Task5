# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:49:38 2021

@author: Emad Elshplangy
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer as tf
# from sklearn.metrics import adjusted_rand_score as ars
from kneed import KneeLocator

#Getting the dataset
dataset = pd.read_csv("Wuzzuf_Jobs.csv")

dataset['Title'] = pd.factorize(dataset['Title'])[0]
dataset['Company'] = pd.factorize(dataset['Company'])[0]

X = dataset.iloc[:, [0, 1]].values
print(X)

from sklearn.cluster import KMeans

wcss = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
# Showing Elbow Point
# plt.plot(range(1, 20), wcss)
# plt.title('The Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()
# # Choosing the elpow point
k1 = KneeLocator(range(1, 20), wcss, curve="convex", direction="decreasing")
print(k1.elbow)

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters=k1.elbow, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# # Visualising the clusters
for i in range(k1.elbow):
    color_list = ['red', 'blue', 'green', 'cyan', 'magenta', 'marron', 'black', 'pink','gold']
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=color_list[i], label=f'Cluster{i+1}')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='coral', label='Centroids')
plt.title('Clusters of Jobs')
plt.xlabel('Jobs')
plt.ylabel('Companies')
plt.legend()
plt.show()