<!--
.. title: CSCI4390-6390 Assign8
.. slug: dm_assign8
.. date: 2021-11-11 12:00:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign8: Clustering: EM and K-Means

**Due Date**: Nov 22, before midnight (11:59:59PM)


You will use the 
[Codon Usage Dataset](https://archive.ics.uci.edu/ml/datasets/Codon+usage#).
You should use Column 1 as the true cluster label. Next ignore
Columns 2, 3, 4, and 5. Use the remaining 64 attributes as the 64
dimensional feature vector per point. Since Column 1 is the animal kingdom,
you are trying to group the points based on the DNA codon frequencies.
Also, there are some data errors on lines 488 and 5065 (if header is assumed
to be line 1). You should ignore
those lines after reading in the data (**do not modify the input file**).

---

# CSCI4390/6390: Expectation Maximization Clustering

Implement the Expectation-Maximization (EM) algorithm for clustering
(see Algorithm 13.3 in Chapter 13). Use Col 1 as the true cluster labels, so
there are 11 true clusters, and you should use $k=11$ to show results.

For initializing the clusters, select $k$ random data points as the cluster
centers. However, once you have chosen the centers, assign each point to the
closest center to compute the covariance matrix and the prior probabilities
of each cluster.

For practical purposes, you may want to use the [logexpsum
trick](https://blog.feedly.com/tricks-of-the-trade-logsumexp/) for
expectation step, where you compute the log probabilities so that you can
deal with very small probability values, otherwise, you may find that
weights of a point for the clusters are zero. That is, if all probabilities
are given as $\log P(Ci)$ and $\log P(xj | Ci)$, 
then we have
first compute $\log w_{ij}' = \log P(xj | Ci) + \log P(Ci)$ (note: this is
only the numerator, we have to normalize as given below). But, to compute
the final $w_{ij}$, we have to use the logsumexp trick, since 
$$logsumexp(\log w_{1j}', \log w_{2j}', ..., \log w_{kj}') = \log\left(\sum_{a=1}^k
        \exp \log w_{aj}'\right) = \log \left(\sum_{a=1}^k w_{aj}'\right)$$
And therefore,
$$w_{ij} = \exp\Big( \log w_{ij}' - logsumexp(\log w_{1j}', ..., \log w_{kj}') \Big)$$
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
* The Normalized Mutual Information (NMI) score for your clustering,
    computed using Eq. 17.8. You must implement this on your own. 

Run your code at least 10 times with different random initial clusters, 
and report the clustering with the best NMI score.


---

# CSCI6390 Only: K-Means

In addition, implement the basic K-Means algorithm 13.1 on pg 336. 

To initialize the clusters select $k$ random points as means.

Your code must output the following information:

* The mean and size of each cluster
* The NMI value for your clustering

Run your code at least 10 times with different random initial clusters, 
and report the clustering with the best NMI score.

---

## What to submit

* Submit your notebook named as **Assign8.ipynb** via submitty.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

