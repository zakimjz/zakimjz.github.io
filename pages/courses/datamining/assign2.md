<!--
.. title: CSCI4390-6390 Assign2
.. slug: dm_assign2
.. date: 2022-09-16 10:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign2: Dimensionality Reduction and High Dimensional Data

**Due Date**: Sep 23, before midnight (11:59:59PM)

We will the dataset [Online News Popularity](https://archive.ics.uci.edu/ml/datasets/online+news+popularity) from the UCI Machine Learning repository. This dataset has 61 attributes
and 39644 points. You will ignore the following attributes for this
assignment: 0-1, 4-6, 13-38, and 60 (counting from 0). So, you'll be left with 29 attributes that
you'll use. Complete the following tasks.

## Part I: Principal Components (2D for CSCI4390 and 3D for CSCI6390)

You have to use power-iteration to compute the first 2 (for CSCI4390) or
first 3 PCs (for CSCI6390), i.e., the eigenvectors as well as the
eigenvalues. The description below is for 2 PCs, but the same procedure
works for 3 PCs, by adding an additional column to the matrix of
eigenvectors.

Make sure to set the seed as np.random.seed(42), so everyone will get the
same results.

To compute the first two eigenvectors of the covariance matrix
$\mathbf{\Sigma}$ we will use a generalized power-iteration
method.

Let $\mathbf{X}_0$ be a $d \times 2$ (random) matrix with two
non-zero $d$-dimensional column vectors with unit length (CSCI6390 will have
a $d\times 3$ matrix).  We will
iteratively multiply $\mathbf{X}_0$ with $\mathbf{\Sigma}$ on the
left.

The first column will not be modified, but the second column will be
orthogonalized with respect to the first one by subtracting its
projection along the first column (see section 1.3.3 in chapter 1). That
is, let $\mathbf{a}$ and $\mathbf{b}$ denote the first and second
column of $\mathbf{X}_1$, where

$$\mathbf{X}_1 = \mathbf{\Sigma} \; \mathbf{X}_0$$

Then we orthogonalize $\mathbf{b}$ as follows:

$$\mathbf{b} = \mathbf{b} - \left({\mathbf{b}^T \mathbf{a} \over \mathbf{a}^T\mathbf{a}}\right) \mathbf{a}$$

After this $\mathbf{b}$
is guaranteed to be orthogonal to $\mathbf{a}$. This will yield the
matrix $\mathbf{X}_1$ with the two column vectors denoting the current
estimates for the first and second eigenvectors. CSCI6390: You have to
orthogonalize the third column with respect to the first two.

Before the next iteration, normalize each column to be unit length, and
repeat the whole process. That is, from $\mathbf{X}_1$ obtain
$\mathbf{X}_2$ and so on, until convergence.

To test for convergence, you can look at the difference 

$$\mathbf{X}_a - \mathbf{X}_{b}$$ 

If the difference is less
than some threshold $\epsilon$ then we stop.

### Scatter Plot of the Data in the 2D PC Basis

Once you have obtained the two eigenvectors: $\mathbf{u}_1$ and
$\mathbf{u}_2$, first print out both of them.

Next, project each of the original data points
$\mathbf{x}_i$ onto those two vectors, to obtain the new projected
points in 2D, and show the scatter plot.

Finally, output how much of the variance is captured by the first two PCs, and
what is the error in the approximation if we retain only these two
components.



## Part II: Points in High Dimensional Space

You will empirically verify what happens to the "center" of the space, and
what happens at the "boundary".

Randomly generate
 $n=1,000,000$ points in $d$ dimensions, sampled uniformly in the range
 $[-1,1]$ for each dimension, where $d$ will be varied from $d=2$ to $d=20$.

First, find and plot the fraction of points that lie in the largest inscribed
hypersphere within the outer hypercube, as a function of $d$. Describe the
trend.

Next, given $\epsilon=0.1$, find and plot the fraction of points that lie
within the $\epsilon$ width hypercube along the boundary. That is, let $H$
denote the outer hypercube that defines the data space, and let $H_\epsilon$ be
the hypercube each of whose dimensions ranges from $-1+\epsilon$ to
$1-\epsilon$. Plot the fraction of points in your sample that lie outside
$H_\epsilon$, as a function of $d$. Describe the trend.


---

## What to submit

* Submit your python notebook, that contains the solution and output for
    both parts, suitably annotated/commented. Name the notebook: assign2.ipynb.


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

