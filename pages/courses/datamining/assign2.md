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

# Assign2: High Dimensional Data and Linear Regression

**Due Date**: Sep 28 (Thurs), before midnight (11:59:59PM)


## Part I a): Points in High Dimensional Space

You will empirically verify what happens to the "center" of the space, and
what happens at the "boundary".

Randomly generate
 $n=100,000$ points in $d$ dimensions, sampled uniformly in the range
 $[-1,1]$ for each dimension, where $d$ will be varied from $d=2$ to
 $d=20$. That is, these points will be within the length $l=2$ hypercube in
 $d$ dimensions.

First, find and plot the fraction of points that lie in the largest inscribed
hypersphere within the above hypercube, as a function of $d$. Describe the
trend.

Next, given $\epsilon=0.1$, find and plot the fraction of points that lie
within the $\epsilon$ width region along the boundary of the  hypercube, 
as a function of $d$. Describe the trend.

If you want replicable results, you can set the random seed as np.random.seed(42).

## Part I b): High Dimensional Normal Distribution

You will empirically verify what happens to the high dimensional normal
distribution in terms of the distance of points from the center.

Randomly sample $n=10,000$ points from the standard multivariate normal
distribution in $d$ dimensions, where $d=10, 50, 100, 500$. You may use
**np.random.multivariate_normal** to generate this sample.

Plot the histogram of distances of points to the center of the space in $d$
dimensions. Verify that for all $d$, the means distance of points to the center in $d$
dimensions is $\sqrt{d}$ and the standard deviation is $1/\sqrt{2}$.



## Part II: Linear Regression via QR Factorization

Download the [Wine Quality
Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality) from the UCI
Machine Learning repository. Extract the winequality-red.csv datafile that
records 12 attributes about 1599 instances of red wine. You should parse and
store the data as a data matrix, using the last "quality"
attribute as the dependent or target variable $Y$, and first 11 attributes as the
independent attributes/variables, $\mathbf{X}$. 

Implement the linear regression algorithm via QR factorization,
namely Algorithm 23.1 on page 602 in Chapter 23. Make sure you augment
$\mathbf{X}$ by adding a
columns of ones as the first dimension.

You must implement QR factorization on your own, as described
in Section 23.3.1 (you cannot use numpy.linalg.qr or similar function,
though you may use it to verify your results).

Next, using the $\mathbf{Q}$ and the $\mathbf{R}$ matrices, you must
solve for the augmented weight vector $\mathbf{w}$.
 **CSCI4390** can
use **numpy.linalg.inv** for your solution, but **CSCI6390** must implement backsolve via backsubstitution 
on their own without using the inv function. See Example 23.4 on how backsolve works.

After you have computed the weight vector $\mathbf{w}$, print it, and then 
compute the SSE value and the $R^2$ statistic, where: 
$$R^2=\frac{TSS-SSE}{TSS}$$
where TSS is the total scatter of the response variable 
$TSS = \sum_{i=1}^n ( y_i - \mu_Y)^2$


---

## What to submit

* You must submit a jupyter notebook, with all of your **code
and output**. You must use NumPy, with well known/inbuilt libraries for data
input (e.g., pandas). Plots must be in inline mode (i.e., embedded) in the
notebook, using matplotlib. Name the notebook: assign2.ipynb.


* Your code must be self-contained,
    and must not hard code file names. You can assume the data file lies in
    the local dir.

If you decide to consult ChatGPT (or other similar AI tools), you must
declare this, and submit a separate text/doc/PDF file documenting your
successes and failures, e.g., what prompts you tried, what worked, what did
not work, how you fixed it, etc. Name this file
**declaration.[txt/pdf/doc]**, choosing the correct extension.


---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
