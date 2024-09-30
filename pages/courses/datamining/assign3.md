<!--
.. title: CSCI4390-6390 Assign3
.. slug: dm_assign3
.. date: 2021-09-29 12:00:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign5: EM Clustering

**Due Date**: Oct 7 (Mon), before midnight (11:59:59PM)

---

Implement the Expectation-Maximization (EM) algorithm for clustering
(see Algorithm 13.3 in Chapter 13).

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


### Dataset

Download the [Steel Industry Energy Consumption
Dataset](https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption) from the UCI
Machine Learning repository. Extract the Steel_industry_data.csv datafile. You should parse and
store the data as a data matrix, focusing only on the 6 continuous
attributes (see datafile or link above for names/descriptions). Thus, your data matrix
will have 35040 points in 6 dimensions. However, in addition you should
record the last attribute (load type) for each point. We will use this as
the ground truth load type for
computing the NMI metric for the clustering (see below).


Apply your algorithm on the energy dataset from above, using $k=3$ clusters.
Your output should comprise the following:

* The final mean for each cluster
* The final covariance matrix for each cluster
* Size of each cluster, after assigning  each point to the cluster with highest posterior probability $P(c_i | x_j)$.
* The Normalized Mutual Information (NMI) score for your clustering.
    CSCI4390 can use *sklearn.metrics.normalized_mutual_info_score**, but
    CSCI6390 must implement this based on Eq. 17.8 in the book.

Run your code several times (due to the different random initial center
selections),  and report the clustering with the best NMI score. Also, you
may want to rescale the data attributes so they are in the same range. You
can use sklearn.preprocessing functions StandardScaler or MinMaxScaler for
normalizing the data.

If the number of data points is too large for you, you may sample down, and
use a **random** subset of the points, but no smaller than 3000 points.
However, try to run on the whole dataset if you can.

---
## Part II. Paper/Pencil Exercises

Submit your solutions to the following questions:

* Chapter 13: Q1, Q2, in addition CSCI6390 students must also do Q3

You can write out the solutions on paper, take an image and attach it so it
displays in your notebook. For example, you can call "from IPython.display import Image", and then use
Image("IMG_NAME").


---

## What to submit

* Submit your notebook named as **Assign3.ipynb** via submitty.

The notebook
should be self-contained, i.e., it should include all output from all the
parts, including figures. It should not hardcode file paths.

For the paper-pencil questions, embed the image in your notebook, and also
submit the image file along with the notebook file.

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
