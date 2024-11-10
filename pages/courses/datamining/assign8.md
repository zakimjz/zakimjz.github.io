<!--
.. title: CSCI4390-6390 Assign8
.. slug: dm_assign8
.. date: 2024-11-09 12:23:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign8: Support Vector Classification

**Due Date**: Nov 25, before midnight (11:59:59PM)

---
### Dataset

Download the [Steel Industry Energy Consumption
Dataset](https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption) from the UCI
Machine Learning repository. Extract the Steel_industry_data.csv datafile. You should parse and
store the data as a data matrix, focusing only on the 6 continuous
attributes (see datafile or link above for names/descriptions). Thus, your data matrix
will have 35040 points in 6 dimensions. However, in addition you should
record the last attribute (load type) for each point. We will use this as
the class label. However, instead of three classes, we will use 'Light
Load' as the positive class (+1) and the other two classes (combined) as the negative
class (-1), so that we get a binary classification task.

First usr random seed 42, and np.random.permutation to permute the points,
and  select only the first 2000 points as the initial dataset. Next,
Use
[sklearn.train_test_split](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html),
using 42 as the random_state, to create the training and
testing data, using 80-20 split (i.e., 80% of the data as training and the
remaining 20% as testing). So the training set will have 1600 points and
testing points 400 points.



---

## Part I: SVM

You will implement the dual SVM Algorithm 21.1 (Chapter 21, page 540), using
hinge loss.

You must implement two kernels, namely, both linear and Gaussian.
You must select the best $C$ value using the validation set, and the same
goes for the spread parameter $\sigma^2$ for the Gaussian kernel.

Report the test accuracy for the different kernels, and the best value of
the hyperparameters, that should be selected based on the validation
accuracy.

Accuracy is defined as the number of correct predictions over the number of
points in a given dataset (e.g., validation set or testing set).


#### CSCI6390

In addition, you must also implement the inhomogeneous polynomial kernel.
You need to select the best degree and $C$ value.

Report the test accuracy and the best hyperparameters used based on the
validation accuracy.


---

## Part II: Questions

Submit your solutions to the following questions:

* Chapter 21: Q1, Q2
* Chapter 25: Q1


---

## What to submit

* Submit your notebook named as **assign8.ipynb**. Include your
    paper-pencil answers as images in the notebook as well.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
