<!--
.. title: CSCI4390-6390 Assign4
.. slug: dm_assign4
.. date: 2025-10-30 12:00:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign4: Clustering -- EM and DENCLUE

**Due Date**: Oct 29 (Wed), before midnight (11:59:59PM)

## Data

Download the [Complex Data](https://www.cs.rpi.edu/~zaki/www/DMCOURSE/data/complex8.csv),
which comprises 2551 points in a 2D space. The first two columns give the coordinates of
the points and the last column denotes the "true" cluster label. You should use the third
column only to assess the clustering quality via the NMI metric, and only the first two
coordinates should be used for the clustering algorithm. You should plot the data with
colors based on the true labels to visualize the data.


## Jupyter Notebook

You must submit a self-contained jupyter notebook, with all of your **code and output**.
You must use NumPy, with well known/inbuilt libraries for data input (e.g., pandas). Plots
must be in inline mode (i.e., embedded) in the notebook, using matplotlib.
If you use AI to assist with the assignment,
you must clearly document the tool used, and the prompts used for each part of the
assignment. Include the prompts as markdown
cells in your notebook (for each part/instance).


## Part I: EM Algorithm

Implement the Expectation-Maximization (EM) algorithm for clustering
(see Algorithm 13.3 in Chapter 13).

For initializing the clusters, CSCI4390 students should select $k$ random "actual" points in the dataset 
as the cluster centers, and CSCI6390 students should choose the $k$ farthest "actual" points starting with an initial random point in the data. However, once you have chosen the centers, assign each point to the
closest center to compute the covariance matrix and the prior probabilities
of each cluster.

For practical purposes, it is better to use log probabilities so that we can
effectively handle very small probability values,
otherwise, you may find that
weights of a point for the clusters are zero. For
expectation step the scipy.special.logsumexp function can be useful for log probabilities.
You should also use scipy.stats.multivariate_normal.logpdf if you work with log probabilities.


### Experimentation and Results

Apply your algorithm on the data from above, using $k=8$ clusters.
Run your code several times (due to the different random initial center
selections),  and report the clustering with the best NMI score. 
Your output should comprise the following for (only) the best cluster found:

* The final mean for each cluster
* The final covariance matrix for each cluster
* Size of each cluster, after assigning  each point to the cluster with highest posterior probability $P(c_i | x_j)$.
* The Normalized Mutual Information (NMI) score for your clustering, using the
*sklearn.metrics.normalized_mutual_info_score** which compares the true cluster labels,
with those determined by your algorithm (see Eq. 17.8, and corresponding section
in the books for what NMI means).

Once you have the best clustering, plot the clusters found using your algorithm 
and color the points based on your labels (not the true labels).

## DENCLUE Density Based Clustering

Implement the DENCLUE density-based clustering algorithm (Alg 15.2, pg 388).
Use mean-shift updates to compute the attractor for each point, as defined in the
FindAttactor function (lines 11-17). Use logsumexp if needed (this is beneficial if the
exp values are too small).

Note that this method does not use the number of clusters as input, so you
need to choose the width parameter $h$, the minimum density value $\xi$, 
and the distance threshold $\theta$ for merging attractors (see class notes for the latter) 
to find a good clustering.
Run your code using different values of these parameters to find 8 clusters 
and report the clustering with the best NMI score.

Your program output should consist of the following information for the best clustering:

* Size of each cluster.
* The Normalized Mutual Information (NMI) score for your clustering.
    You can use sklearn.metrics.normalized_mutual_info_score to compute.

Once you have the best clustering, plot the clusters found using your algorithm 
and color the points based on your labels (not the true labels).

How does EM compare with DENCLUE on this dataset?


## What to submit

* Submit your notebook named as **assign4.ipynb** via submitty.

The notebook
should be self-contained, i.e., it should include all output from all the
parts, including figures. It should not hardcode file paths.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
