#Este  programa toma una base de datos (de condiciones climaticas)
#e identifica cuales son las regiones
#donde se espera que exista mas lluvia
#usando el algoritmo de kMeans de ML

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat

#funcion para estimar los centroides de cada cluster
def find_closest_centroids(X, centroids):
    m = X.shape[0]
    k = centroids.shape[0]
    idx = np.zeros(m)

    for i in range(m):
        min_dist = 1000000
        for j in range(k):
            dist = np.sum((X[i,:] - centroids[j,:]) ** 2)
            if dist < min_dist:
                min_dist = dist
                idx[i] = j    
    return idx

#Carguemos una base de datos del clima
data = loadmat('data/clustering_colors.mat')
X = data['X']

#Propongamos unos centroides iniciales (deben ser aleatorios o con valores dados)
initial_centroids = np.array([[3, 3], [6, 2], [8,5]])
#pusimos solo 3

#Estimemos donde estan los centroides mas cercanos a nuestros puntos 
idx = find_closest_centroids(X, initial_centroids)
print(idx[0:1000])#el indice del centroide en el que esta cada dato en el rango

#Necesitamos una funcion para calcular el centroide de un cluster, el cual
#la media de los centroides asignados al cluster
def compute_centroids(X, idx, k):
    m, n = X.shape
    centroids = np.zeros((k, n))#numpy para darle formato

    for i in range(k):
        indices = np.where(idx == i)
        centroids[i,:] = (np.sum(X[indices,:], axis=1) / len(indices[0])).ravel()
    
    return centroids

#compute_centroids(X, idx, 3)

#Funcion para correr el algoritmo
def run_k_means(X, initial_centroids, max_iters):
    m, n = X.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(m)
    centroids = initial_centroids

    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, k)
 
    return idx, centroids

#Escribimos el algoritmo (nuestro resultado es las posiciones de los centroides)
idx, centroids = run_k_means(X, initial_centroids, 10)#el 10 es las veces definidas que busca, mientras mas, mejor
#print(idx)
print(centroids)

#hacer graficas

#hacer graficas
#Aqui definimos nuestros cluster
cluster1 = X[np.where(idx == 0)[0],:]
cluster2 = X[np.where(idx == 1)[0],:]
cluster3 = X[np.where(idx == 2)[0],:]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')
ax.legend()

plt.xlabel('Diferencia de temperatura')
plt.ylabel('Diferencia de presion')
plt.savefig("kmeans_recargado.pdf")
