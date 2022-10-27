<!--
.. title: CSCI4390-6390 Assign6
.. slug: dm_assign6
.. date: 2022-10-25 20:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign6: Logistic Regression

**Due Date**: Nov 1, before midnight


We will use a new dataset this time: [Fashion
MNIST](https://www.kaggle.com/datasets/zalando-research/fashionmnist). It
has 60K images that are $28\times 28 = 784$ dimensional, and which belong to
10 classes. The data has already been converted into csv format, where the
first column denotes the class, and the remaining 784 attributes are the
pixel values (1-255). You will use the 60K examples fashion-mnist_train.csv
file for training, and the 10K examples fashion-mnist_test.csv for testing.

Since the data is large, you should first set the random seed to 42, and
then shuffle the points in the training and test sets. Select the first
10000 points after shuffling the train.csv file as the training data, and
the first 5000 points after shuffling test.csv files as the testing data.

You will implement the multi-class logistic regression algorithm as described in
Algorithm 24.2 (Chapter 24, page 634). 

Your script should print out the weight vector(s), and also the final
accuracy value on the test data (see Eq 22.2). You should also compute the F1-score (see
Eq 22.7 in chapter 22).

You should use the scipy.special.softmax function rather than your own,
since it is more robust.


**CSCI6390**: There may be an extra component which is TBD.

---

## What to submit

* Submit your python notebook, that contains the solution and output,
suitably annotated/commented. Name the notebook: **assign6.ipynb**.


* Submit the notebook file via submitty. Your code must be self-contained,
    and must not hard code file names. You can assume the data files lie in
    the local dir.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

