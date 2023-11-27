<!--
.. title: CSCI4390-6390 Assign6
.. slug: dm_assign6
.. date: 2023-11-26 12:00:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign6: Clustering: Density and Spectral

**Due Date**: Dec 4, before midnight (11:59:59PM)


You will use the 
[Iris Dataset]((https://archive.ics.uci.edu/dataset/53/iris).
Do not use the last column, which denotes the class label. It will only be
use to test the NMI value. The other columns denote the input variables for
clustering.


---

# CSCI4390/6390: Density Clustering

Implement the DENCLUE density-based clustering algorithm given in 
Algorithm 15.2 on page 388. 

Use mean-shift updates to compute the attractor for each point. Use
logsumexp as needed.

Once you have computed the attractors, for step 7 where you check for
density reachable, you should basically merge two attractors (and all points
attracted to them) using a distance threshold $\theta$. That is, two
attractors that are within $\theta$ distance of each other should be merged
together into a single cluster. Thus, each cluster will be given by a set of
attractors (along with all points attracted to any one of them).

Note that this method does not use the number of clusters as input, so you
need to choose $\theta$ carefully to report the final clustering.
Run your code using different thresholds and report the clustering with the best NMI score.

Your program output should consist of the following information:

* Number of clusters.
* Size of each cluster.
* The Normalized Mutual Information (NMI) score for your clustering.
    You can use [sklearn.metrics.normalized_mutual_info_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html) using 'geometric' as average_method.

Note that you should try to obtain 3 clusters.

---

# CSCI6390 Only: Spectral Clustering

In addition, implement the spectral algorithm 16.1 on pg 406.
To define the similarity matrix, use the Gaussian kernel (see Eq 5.10):
$$a_{ij} = \exp\{-(\mathbf{x}_i - \mathbf{x}_j) / 2\sigma^2\}$$
where $\sigma^2$ is the variance parameter, that you have to choose on your
own.
Run your code using different $\sigma^2$ values and report the clustering with the best NMI score.

Your program output should consist of the following information:

* Number of clusters.
* Size of each cluster.
* The Normalized Mutual Information (NMI) score for your clustering.

---

## What to submit

* Submit your notebook named as **assign6.ipynb** via submitty.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action. Use of AI tools
must be documented.

