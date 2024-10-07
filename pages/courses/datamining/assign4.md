<!--
.. title: CSCI4390-6390 Assign4
.. slug: dm_assign4
.. date: 2024-10-07 12:00:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign4: Density Clustering

**Due Date**: Oct 14, before midnight (11:59:59PM)

---
## Part I: Clustering Algorithm

### Dataset

Download the [Steel Industry Energy Consumption
Dataset](https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption) from the UCI
Machine Learning repository. Extract the Steel_industry_data.csv datafile. You should parse and
store the data as a data matrix, focusing only on the 6 continuous
attributes (see datafile or link above for names/descriptions). Thus, your data matrix
will have 35040 points in 6 dimensions. However, in addition you should
record the last attribute (load type) for each point. We will use this as
the ground truth load type for
computing the NMI metric for the clustering.
Also, it is a good idea to scale all
attributes to be within the range 0 to 1. For this you should use [sklearn.preprocessing.MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html).

### DENCLUE Algorithm

Implement the DENCLUE density-based clustering algorithm given in
Algorithm 15.2 on page 388.

Use mean-shift updates to compute the attractor for each point. Use
logsumexp as needed. For CSCI6390, in addition implement the gradient
ascent based update to find the attractors.

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

For CSCI6390, report your findings about the differences between the
mean-shift vs the gradient ascent based attractor finding step, e.g.,
convergence time, quality of clusters, etc.

---

## Part II: Questions

Submit your solutions to the following questions:

* Chapter 15: Q3, in addition CSCI6390 students must also do Q5
* Chapter 16: Q6a and Q6c.

You can write out the solutions on paper, take an image and attach it so it
displays in your notebook. For example, you can call "from IPython.display import Image", and then use
Image("IMG_NAME").

---

## What to submit

* Submit your notebook named as **assign4.ipynb** via submitty. And submit
    the solutions to the questions above within the notebook.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
