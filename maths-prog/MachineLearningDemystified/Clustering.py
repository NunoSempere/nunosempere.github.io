directory = '/home/nuno/Documents/Jobs/IDInsight'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import the algorithms
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import Birch
from sklearn.mixture import GaussianMixture

## Install the dataframe
insuranceDataFrame = pd.read_csv(directory + '/insurance_clean_continuous.csv')

## Gather the algorithms
clusterings = [KMeans(n_clusters=3, random_state=0).fit(insuranceDataFrame), AffinityPropagation(affinity='euclidean', convergence_iter=100, copy=True, damping=.9, max_iter=200, preference=None, verbose=False).fit(insuranceDataFrame), MeanShift().fit(insuranceDataFrame), SpectralClustering(n_clusters=3, affinity='nearest_neighbors', n_neighbors = 20, random_state=0).fit(insuranceDataFrame), AgglomerativeClustering(n_clusters=3).fit(insuranceDataFrame), DBSCAN(eps=500, min_samples=3).fit(insuranceDataFrame), Birch(branching_factor=50, n_clusters=3, threshold=0.5, compute_labels=True).fit(insuranceDataFrame)]
    # This takes a while
names = ["KMeans", "AffinityPropagation", "MeanShift", "SpectralClustering", "AgglomerativeClustering", "DBSCAN", "Birch"]
assert(len(names)==len(clusterings))

## Plot the plots
sns.set()

## This produces *a lot* of plots!
for k in range(len(names)):

    insuranceDataFrame["cluster"] = clusterings[k].labels_

    n= len(np.unique(clusterings[k].labels_))

    for variable in insuranceDataFrame.columns:
        sns_plot = sns.relplot(x="charges", y=variable, hue="cluster", data=insuranceDataFrame, palette = sns.color_palette("hls", n))
        plt.subplots_adjust(top=0.9)  ## Makes more room at the top
        plt.title(names[k] + ": charges ~ " + variable, y=1.3)
        sns_plot.savefig("figures/" + names[k] + "-" + variable + ".png")

## Gaussian Requires different syntax
clustering = GaussianMixture(n_components=3).fit(insuranceDataFrame)
n= len(np.unique(clustering.predict(insuranceDataFrame)))
insuranceDataFrame["cluster"] = clustering.predict(insuranceDataFrame)

for variable in insuranceDataFrame.columns:
    sns_plot = sns.relplot(x="charges", y=variable, hue="cluster", data=insuranceDataFrame,palette=sns.color_palette("hls", n))
    plt.subplots_adjust(top=0.9)  ## Makes more room at the top
    plt.title("GaussianMixture" + ": charges ~ " + variable, y=1.3)
    sns_plot.savefig("figures/" +"GaussianMixture" + "-" + variable + ".png")
