<!--
.. title: CSCI4390-6390 Assign5
.. slug: dm_assign5
.. date: 2022-10-14 12:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign5: Support Vector Regression

**Due Date**: Oct 24, before midnight (11:59:59PM)


We will continue with the [Online News Popularity](https://archive.ics.uci.edu/ml/datasets/online+news+popularity)
dataset as in previous assignments. This dataset has 61 attributes and 39644
points. 
Ignore the following attributes for this assignment: 0-1,
4-6, 13-38. We will use all the remaining attributes, but with the last attribute
(60; shares) as the target variable. Thus you will have 29 independent
attributes and 1 dependent or target attribute. Your goal is to build a
classification model to predict the number of shares of a news article
binned into two classes: low (negative) vs. high (positive) shares.

First, follow the same data preprocessing steps outlined in {{% doc %}} dm_assign4
{{% /doc %}}, except that you should split the data into three parts after shuffling the points, by taking 
the first 1000 points as
training data, the next 1000 points as validation data, and the next 1000
points as the test data. You can ignore the remaining points.

For the target classes, first clamp the highest number of shares at 6000,
i.e., if the target variable has more than 6000 shares, then set it to 6000.
Next, define the positive class (+1) as those posts with 2000 or more shares, and
the negative class (-1) as those with fewer than 2000 shares.

## SVM

You will implement the dual SVM Algorithm 21.1 (Chapter 21, page 540), using
hinge loss.

You must implement two kernels, namely, both linear and Gaussian.
You must select the best $C$ value using the validation set, and the same
goes for the spread parameter $\sigma^2$ for the Gaussian kernel.

Report the test accuracy for the different kernels, and the best value of
the hyperparameters.

#### CSCI6390

In addition, you must also implement the inhomogeneous polynomial kernel. 
You need to select the best degree and $C$ value.

Report the test accuracy and the best hyperparameters used.

---

## Exam I Questions

Submit your solutions to exam I question Q5, and in addition CSCI6390
should submit their solutions to Q8.


---

## What to submit

* Submit your python notebook, that contains the solution and output, 
suitably annotated/commented. Name the notebook: **assign5.ipynb**.


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

