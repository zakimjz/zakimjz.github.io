<!--
.. title: CSCI4390-6390 Assign3
.. slug: dm_assign3
.. date: 2023-10-9 13:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign3: Logistic Regression and Neural Networks

**Due Date**: Oct 20, before midnight

Download the [Wine Quality
Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality) from the UCI
Machine Learning repository. We will use winequality-white.csv as the
*training dataset* and winequality-red.csv as the *testing* dataset.
The white wine dataset has 4898 points, and the red wine data has 1599
points. There are 12 attributes in total, with the last attribute "quality"
denoting the integer valued target variable. 

---

## Part I: Logistic Regression

Implement the multi-class logistic regression algorithm as described in
Algorithm 24.2 (Chapter 24, page 634). 

Your script should print out the weight vector(s), and also the final
accuracy value on the test data (see Eq 22.2). You should also compute the
F1-score (see Eq 22.7 in chapter 22).

You should use the scipy.special.softmax function rather than your own,
since it is more robust.

---
## Part II: Neural Networks from Scratch

Implement the deep multi-layer perceptron (MLP) algorithm in
Algorithm 25.2 (Chapter 25, page 668). You should use ReLU activation
for all hidden layers, and softmax for the output layer. See section
25.1.1 for the derivative of the activation functions, and end of section
25.4.3 for derivative of the multiclass cross-entropy function.

Train your network on white wine data, and then test on red wine data.
You must try different number of hidden layers, and their sizes. Report
results for the configuration that gives the best F1 score values.

CSCI6390: Your implementation must additionally support linear
activation function for the output layer (keep ReLU for the hidden layers).
Also, you must support the case when there is no hidden layer; this latter
case will correspond to linear regression when output is linear, and 
logistic regression when output is softmax.

In addition to reporting the results for different number of hidden layers
(and their sizes), also report the results when there are no hidden layers
but using softmax output (similar to multi-class logistic regression), and
for the case when there is no hidden layer but using linear output (treating
it like linear regression).

---

## What to submit

* Submit your python notebook, that contains the solution and output,
suitably annotated/commented. Name the notebook: **assign3.ipynb**.


* Submit the notebook file via submitty. Your code must be self-contained,
    and must not hard code file names. You can assume the data files lie in
    the local dir.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.

