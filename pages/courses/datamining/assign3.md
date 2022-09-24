<!--
.. title: CSCI4390-6390 Assign3
.. slug: dm_assign3
.. date: 2020-9-23 18:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign3: Non-Linear Dimensionality Reduction: Kernel PCA

**Due Date**: Oct 9, before midnight (11:59:59PM)


We will the [Online News
Popularity](https://archive.ics.uci.edu/ml/datasets/online+news+popularity)
dataset as in previous assignments. This dataset has 61 attributes and 39644
points. Ignore the following attributes for this assignment: 0-1,
4-6, 13-38, and 60 (counting from 0). So, you'll be left with 29 attributes
that you'll use. Since 39644 is too many points, use only the first 5000
points for this assignment. Complete the following tasks.


Implement the Kernel PCA (KPCA) algorithm as described in
Algorithm 7.2 (Chapter 7, page 208; look at [book errata](https://dataminingbook.info/errata/) for the typo on line 7 of the algo -- the denominator should have i from 1 to $n$ and not $d$). You need to compute the kernel and
then center it, followed by extracting the dominant eigenvectors, which
will give you the components of the directions in feature space. Next
you will project and visualize the data. To compute the principal
components (PCs) from the kernel matrix, you may use the inbuilt numpy
function eigh.

Using the linear kernel (i.e., polynomial kernel with degree $q=1$ and
$c=0$; in other words $K(\mathbf{x},\mathbf{y}) = \mathbf{x}^T\mathbf{y}$),
how many dimensions are required to capture $\alpha=0.95$ fraction of the
total variance? For the same linear kernel, compute the projected points
along the first two kernel PCs, and create a scatter plot of the projected
points.

Next, use the covariance matrix for the original data to compute the
regular principal components, i.e., for the covariance matrix. Project
the data onto the first two PCs. How do the eigenvalues and the
projection compare with that obtained via Kernel PCA with linear kernel?

Finally, use the gaussian kernel and repeat the exercise for kernel PCA.
Project the points onto the first two PCs and plot the scatter plot. 
Try different values and submit your plot for
the value that makes most sense to you (observe the projected plots for
various spread values and then decide).

**CSCI6390 Only**: In addition to the above, use an inhomogeneous quadratic
kernel and examine how many components it takes to capture $0.95$ fraction
of the variance. Choose the appropriate $c$ value. Plot the data onto the
first two quadratic PCs. Finally, out of the three kernels -- linear,
inhomogeneous quadratic, gaussian -- which results in the best 2D
approximation? Why?

---

## What to submit

* Submit your python notebook, that contains the solution and output, 
suitably annotated/commented. Name the notebook: assign3.ipynb.


* Submit the notebook file via submitty. Your code must be self-contained,
    and must not hard code file names. You can assume the data file lies in
    the local dir.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.
