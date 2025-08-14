<!--
.. title: CSCI4390-6390 Assign7
.. slug: dm_assign7
.. date: 2024-11-09 12:23:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign7: Logistic Regression

**Due Date**: Nov 18, before midnight (11:59:59PM)

---
### Dataset

Download the [Steel Industry Energy Consumption
Dataset](https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption) from the UCI
Machine Learning repository. Extract the Steel_industry_data.csv datafile. You should parse and
store the data as a data matrix, focusing only on the 6 continuous
attributes (see datafile or link above for names/descriptions). Thus, your data matrix
will have 35040 points in 6 dimensions. However, in addition you should
record the last attribute (load type) for each point. We will use this as
the class label.

Use
[sklearn.train_test_split](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html),
using 42 as the random_state, to shuffle and create the training and
testing data, using 80-20 split (i.e., 80% of the data as training and the
remaining 20% as testing).

---

## Part I: Logistic Regression

Implement the multi-class logistic regression algorithm as described in
Algorithm 24.2 (Chapter 24, page 634). In line 6, instead of
initializing with zeros, use np.random.randn instead. This way you'll get
different initialized weights in each run, and thus you'll be able to
explore more. Also, you may cap the maximum iterations of the repeat-until
loop in addition to checking for convergence.

Your script should print out the weight vector(s), and also the final
accuracy value on the test data (see Eq 22.2). You should also compute the
F1-score (see Eq 22.7 in chapter 22).

You should use the scipy.special.softmax or scipy.special.log_softmax function rather than your own,
since it is more robust.

Also, the loops in line 8, 11, 15, and 18 run from 1 to $K-1$, but you can
just make it 1 to $K$, so that all class weight vectors are learned (the
pseudocode assumes that the last class the base class, and therefore its
weight vector is the zero vector). As such, both approaches are fine.

Finally, CSCI6390 students must implement a **mini-batch** version of the
logistic regression. That is, instead of using a single point to compute
the gradient as in eq (24.19), compute the gradient for a batch of points
at the same time (you can make batch size a parameter and try different
values), and the batch gradient will be the sum of the individual gradient
from each point. At the same time, line 10 will now iterate over the batch
of points, and update the class weights once per batch (as opposed to once
per point).

---

## Part II: Questions

Submit your solutions to the following questions:

* Chapter 24: Q2


---

## What to submit

* Submit your notebook named as **assign7.ipynb**. Include your
    paper-pencil answers as images in the notebook as well.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
