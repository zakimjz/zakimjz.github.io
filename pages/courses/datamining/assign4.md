<!--
.. title: CSCI4390-6390 Assign4
.. slug: dm_assign4
.. date: 2025-10-13 12:00:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign4: EM Clustering

**Due Date**: Oct 22 (Wed), before midnight (11:59:59PM)

## Data

Download the [Breast Cancer Wisconsin (Diagnostic)
Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) from
the UCI Machine Learning repository. You should parse and store the data as a data matrix.
The ID variable will not be used, and the Diagnosis variable will be used only as labels
to determine the ground truth clustering. The remaining 30 continuous attributes will comprise the data matrix, which
is $n=569$ points in $d=30$ dimensional space.

Use sklearn's MinMaxScaler to make sure all attributes are between 0 and 1.


## Jupyter Notebook

You must submit a self-contained jupyter notebook, with all of your **code and output**.
You must use NumPy, with well known/inbuilt libraries for data input (e.g., pandas). Plots
must be in inline mode (i.e., embedded) in the notebook, using matplotlib.

## EM Algorithm

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

As another practical point, you can get an error when inverting the covariance
matrix, so you should add a small ridge value $\lambda$ value along the
diagonal entries to make the matrix invertible. 
You should also use scipy.stats.multivariate_normal.logpdf with *allow_singular* flag set to True.


### Experimentation and Results

Apply your algorithm on the data from above, using $k=2$ clusters.
Run your code several times (due to the different random initial center
selections),  and report the clustering with the best NMI score. 
Your output should comprise the following for (only) the best cluster found:

* The final mean for each cluster
* The final covariance matrix for each cluster
* Size of each cluster, after assigning  each point to the cluster with highest posterior probability $P(c_i | x_j)$.
* The Normalized Mutual Information (NMI) score for your clustering.
    CSCI4390 can use *sklearn.metrics.normalized_mutual_info_score**, but
    CSCI6390 must implement this based on Eq. 17.8 in the book.


Once you have the best clustering, plot the data projected onto the first two principal
components of the data, and color the points according to the cluster assignments. Points
where the true label and the predicted cluster match the malignant class should be red,
those where the true label and the predicted cluster members match the benign class should
be green, and all other points should be blue. This will help you visualize the quality of
your clustering. 



## What to submit

* Submit your notebook named as **assign4.ipynb** via submitty.

The notebook
should be self-contained, i.e., it should include all output from all the
parts, including figures. It should not hardcode file paths.


If you decide to consult ChatGPT (or other similar AI tools), you must
declare this in your notebook, with a brief text description of your
successes and failures, e.g., what prompts you tried, what worked, what did
not work, how you fixed it, etc. Include this as a markdown cell in your
notebook.


---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
