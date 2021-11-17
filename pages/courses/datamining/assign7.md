<!--
.. title: CSCI4390-6390 Assign7
.. slug: dm_assign7
.. date: 2021-11-14 20:00:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign6: Clustering: EM and Kernel KMeans

**Due Date**: Nov 22, before midnight (11:59:59PM, Alofi Time; GMT-11)


You will use the 
[Appliances energy prediction data set](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction#).
You should ignore the first attribute, which is a date-time variable,
and you should also remove the last attribute, which is a duplicate of
the previous one. Also, the first attribute (after removing the
date-time variable), which denotes the
**Appliances Energy Use**, will NOT be used for clustering; instead we
will use it as the cluster label to assess the performance of the
clustering methods. Thus, ignoring "date", "Appliances", and "rv2", 
the remaining attributes will be used as the data for clustering.

Note that the **Appliances Energy Use** attribute takes values in the range
$[10,1080]$. However, for clustering, we will group these values into 4
"true" clusters: $c_0$ is for values in the range $[10,40]$, $c_1$ for
values $(40,60]$, $c_2$ for values $(60,100]$, and $c_3$ for values
$(100,1080]$.

---

# CSCI4390/6390: Expectation Maximization Clustering

Implement the Expectation-Maximization (EM) algorithm for clustering
(see Algorithm 13.3 in Chapter 13). Use the 'Appliances' attribute as
the true cluster label as described above, and use it for the purity-based clustering
evaluation (see below). Run with $k=4$ clusters. 

For initializing the clusters, you must implement the farthest point from
the means strategy described in class. That is, pick the first point at
random from the dataset and set it as $\mu_0$. Next, pick the point farthest
away from $\mu_0$ and set it as $\mu_1$. Next, pick the point that is
farthest away from both $\mu_0$ and $\mu_1$, the point that maximizes the
minimum distance to already selected means, as the next mean $\mu_3$.
Continue this way until you select $k$ initial means.

For practical purposes, you may want to use the [logexpsum
trick](https://blog.feedly.com/tricks-of-the-trade-logsumexp/) for
expectation step, where you compute the log probabilities so that you can
deal with very small probability values, otherwise, you may find that
weights of a point for the clusters are zero. That is, if all probabilities
are given as $\log P(Ci)$ and $\log P(xj | Ci)$, 
then we have
first compute $\log w_{ij} = \log P(xj | Ci) + \log P(Ci)$ (note: this is
only the numerator, we have to normalize as given below). But, to compute
the final $w_{ij}$, we have to use the logsumexp trick, since 
$$logsumexp(\log w_{1j}, \log w_{2j}, ..., \log w_{kj}) = \log\left(\sum_{a=1}^k
        \exp \log w_{aj}\right) = \log \left(\sum_{a=1}^k w_{aj}\right)$$
And therefore,
$$w_{ij} = \exp\Big( \log w_{ij} - logsumexp(\log w_{1j}, ..., \log w_{kj}) \Big)$$
You can therefore use scipy.special.logsumexp function on log probabilities.

As another practical point, you can get an error when inverting the covariance
matrix, so you should add a small ridge value $\lambda$ value along the
diagonal entries to make the matrix invertible. This can be considered
as a regularized estimate of the covariance matrix, i.e., $$\Sigma +
\lambda \mathbf{I}$$
Or just use scipy.stats.multivariate_normal.logpdf with *allow_singular* flag set to True.

Your program output should consist of the following information:

* The final mean for each cluster
* The final covariance matrix for each cluster
* Size of each cluster, after assigning  each point to the cluster with highest posterior probability $P(c_i | x_j)$.
* The 'purity score' for your clustering, computed as follows: Assume that $c_i$ 
   denotes the set of points assigned to cluster $i$ by the EM algorithm, and let $T_i$ 
   denote the true cluster id. Purity score is defined as:
   $$\frac{1}{n} \sum_{i=1}^k max_{j=1}^K \\{c_i \cap T_j\\} $$
   where $K$ is the true number of clusters, and $k$ is the input number
   of clusters to EM. See Eq(17.1) on pg 427 for more details on the purity measure.

Run your code at least 10 times with different random initial clusters (via farthest means strategy), 
and report the clustering with the best 'purity score'.


---

# CSCI6390: Kernel K-Means

In addition, implement the Kernel K-Means algorithm 13.2 on pg 341. 
Use only
the Gaussian kernel, but you'll have to choose the value of spread. 

Note that you must use the farthest point from existing means strategy in
*feature space* (via kernel matrix) to initialize the clusters. That is,
find the $k$ means in feature space, then assign points to closest mean
in feature space to compute initial random clusters.

Your code must output the following information:

* Size of each cluster
* The Purity for your clustering

Run your code at least 10 times with different random initial clusters (via farthest means strategy), 
and report the clustering with the best 'purity score'.

---

## What to submit

* For EM, write a script named as **Assign7.py**, which will be run as 
      
   Assign6.py FILENAME k EPS RIDGE MAXITER
   
 FILENAME is the datafile name, $k$ is the number of clusters to find,
 and EPS is the convergence threshold, RIDGE the $\lambda$ value for
 the ridge, and MAXITER is the maximum number of iterations to run (we
 need this since it may take a long time to converge for low EPS).
 Note that you should report the
 output for $k=4$, but your code should run for any input value of $k$.
 And you must output the purity for the given value of $k$ (which may
 not correspond to the true value $K=4$).

* For CSCI6390, for Kernel Kmeans, write a script **Assign7-KK.py**,
    which will be run as

   Assign7-KK.py FILENAME k EPS SPREAD

   The parameters have the same meaning as given above, but SPREAD is
   the spread parameter for the Gaussian kernel.

Note that computing the full kernel matrix for 19K+
points will be memory intensive, so if you do not have enough memory,
one option is for you to repeatedly compute the required kernel values.
Alternatively, you can show results on at least 5000 points. 
However, you have to select these points using **stratified sampling**,
so that you choose a proportional number of points from each cluster
label. You can use [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html) from scikit-learn for
stratified sampling if you wish.

* Submit a PDF file named Assign7.pdf that should include your output 
* (just cut and paste the output from python).
 **Failure the submit the PDF will result in lost points.** 

* Submit the scripts and pdf file via submitty

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

