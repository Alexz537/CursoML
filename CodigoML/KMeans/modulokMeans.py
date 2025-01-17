import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat


def init_centroids(X, k): #X es el numero de datos
                          # y k es el numero de centroides
    m, n = X.shape
    centroids = np.zeros((k, n))#formato de la forma k, n
    idx = np.random.randint(0, m, k)#arreglo

    for i in range(k):
        centroids[i,:] = X[idx[i],:]
    return centroids


def run_k_means(X, initial_centroids, max_iters):
    m, n = X.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(m)
    centroids = initial_centroids

    for i in range(max_iters):
          idx = find_closest_centroids(X, centroids)
          centroids = compute_centroids(X, idx, k)
    return idx, centroids

def find_closest_centroids(X, centroids):
    m = X.shape[0]
    k = centroids.shape[0]
    idx = np.zeros(m)#numpy para darle formato

    for i in range(m):
        min_dist = 1000000
        for j in range(k):
            dist = np.sum((X[i,:] - centroids[j,:]) ** 2)
            if dist < min_dist:
                min_dist = dist
                idx[i] = j
    return idx

def compute_centroids(X, idx, k):
    m, n = X.shape
    centroids = np.zeros((k, n))#numpy para darle formato

    for i in range(k):
        indices = np.where(idx == i)
        centroids[i,:] = (np.sum(X[indices,:], axis=1) / len(indices[0])).ravel()

    return centroids

