<!--
.. title: CSCI4390-6390 Assign5
.. slug: dm_assign5
.. date: 2025-10-22 12:00:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign5: Density Clustering

**Due Date**: Oct 30, before midnight (11:59:59PM)

---
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

### DENCLUE Algorithm

You will implement the DENCLUE density-based clustering algorithm (Alg 15.2, pg 388), 
but slightly modified as noted below.

You will use mean-shift updates to compute the attractor for each point, as defined in the
FindAttactor function (lines 11-17). Use logsumexp if needed.


The first change from the pseudo-code is that we will not do any density-based filtering. 
Just compute the attractor for each point using mean-shift. Next, as you find the
attractor for point $\mathbf{x}_i$, first check whether a previously found attractor is
close to it, and add the point to that attractor's points. In other words, say
$\mathbf{a}_i$ is the attractor for $\mathbf{x}_i$. If $\mathbf{a}_i$ is close to a
previously found attractor $\mathbf{a}_k$, then add $\mathbf{x}_i$ to the point set for
$\mathbf{a}_k$. For the closeness check you should use 
$\|\mathbf{a}_i -\mathbf{a}_k \| \le \theta$
where $\theta$ is some distance threshold (that you'll have to choose).

Note that as you add points to a given attractor, say $\mathbf{a}_k$ above, make sure you
also update the attractor to be the mean of the two attractors, i.e., replace
$\mathbf{a}_k$ by the mean of $\mathbf{a}_k$ and $\mathbf{a}_i$, for the case above. To be
perfectly correct, you should do a running mean update of the attractors if points are
added to a previous attractor (this would also involve keep track of how many points have
been added to a given attractor's point set.)


Finally, run kmeans over the attractors to find 2 clusters (you can use sklearn's Kmeans
algorithm), and then for each attractor in
a cluster, its assigned points should get the same cluster label.

Note that this method does not use the number of clusters as input, so you
need to choose the width parameter $h$ and the distance threshold $\theta$ carefully
to find a good clustering.
Run your code using different values for both and report the clustering with the best NMI score.

Your program output should consist of the following information:

* Size of each cluster.
* The Normalized Mutual Information (NMI) score for your clustering.
    You can use [sklearn.metrics.normalized_mutual_info_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html) using 'geometric' as average_method.

Finally, plot the clusters in 2D using the PCA projections. Note the cluster centers as
well.


---

## What to submit

* Submit your notebook named as **assign5.ipynb** via submitty. Document AI tools use via
  the prompts use and the modifications to those prompts to make things work.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
