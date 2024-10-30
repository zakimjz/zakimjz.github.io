<!--
.. title: CSCI4390-6390 Assign6
.. slug: dm_assign6
.. date: 2024-10-30 12:23:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign6: Linear Regression

**Due Date**: Nov 8, before midnight (11:59:59PM)

---
### Dataset

Download the [Steel Industry Energy Consumption
Dataset](https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption)
from the UCI Machine Learning repository. Extract the
Steel_industry_data.csv datafile. You should parse and store the data as a
data matrix, focusing only on the 6 continuous attributes (see datafile or
link above for names/descriptions). However, we will treat the tCO2
attribute as the target variable. So the other 5 continuous attributes will
be the independent attributes.

Use
[sklearn.train_test_split](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html),
using 42 as the random_state, to shuffle and create the training and
testing data, using 80-20 split (i.e., 80% of the data as training and the
remaining 20% as testing).

---

## Part I: Linear Regression via Projections

Implement the linear regression algorithm via QR factorization, namely
Algorithm 23.1 on page 602 in Chapter 23. Make sure you augment
$\mathbf{X}$ by adding a columns of ones as the first dimension.

You must implement QR factorization on your own, as described in Section
23.3.1 (you cannot use numpy.linalg.qr or similar function, though you may
use it to verify your results).

Next, using the $\mathbf{Q}$ and the $\mathbf{R}$ matrices, you must solve
for the augmented weight vector $\mathbf{w}$. **CSCI4390** can use
**numpy.linalg.inv** for your solution, but **CSCI6390** must implement
backsolve via backsubstitution on their own without using the inv function.
See Example 23.4 on how backsolve works.

After you have computed the weight vector $\mathbf{w}$, print it, and then
compute the SSE value and the $R^2$ statistic, where:
$$R^2=\frac{TSS-SSE}{TSS}$$
where TSS is the total scatter of the response variable
$TSS = \sum_{i=1}^n ( y_i - \mu_Y)^2$


---

## Part II: Questions

Submit your solutions to the following questions:

* Chapter 20: Q1, Q2
* Chapter 23: Q1, Q2, in addition CSCI6390 must do Q3


---

## What to submit

* Submit your notebook named as **assign6.ipynb**. Include your
    paper-pencil answers as images in the notebook as well.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
