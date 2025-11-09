<!--
.. title: CSCI4390-6390 Assign6
.. slug: dm_assign6
.. date: 2024-11-08 12:23:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign6: Support Vector Classification

**Due Date**: Nov 18, before midnight (11:59:59PM)

---
### Dataset

Download the [Breast Cancer Wisconsin (Diagnostic)
Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) from
the UCI Machine Learning repository. You should parse and store the data as a data matrix.
The ID variable will not be used, and the Diagnosis variable will be used as class labels
for the classification task.
The remaining 30 continuous attributes will comprise the data matrix, which
is $n=569$ points in $d=30$ dimensional space. 

Use sklearn's MinMaxScaler to make sure all attributes are between 0 and 1. Code the
malign class as $+1$ and the benign class as $-1$. Then, augment the dataset by adding a
column of ones.
Next, use
[sklearn.train_test_split](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html),
using 42 as the random_state, setting shuffle to True and test_size to 100, to create the 
testing data, and the remaining data. Next apply the same process but this time with
test_size as 69 to create the validation set and training set. You will then have training set with 400 points, validation with 69 points, and
testing with 100 points.


## Jupyter Notebook

You must submit a self-contained jupyter notebook named as **assign6.ipynb**, with all of your **code and output**.
You must use NumPy, with well known/inbuilt libraries for data input (e.g., pandas). Plots
must be in inline mode (i.e., embedded) in the notebook, using matplotlib.


---

## SVM

You will implement the dual SVM Algorithm 21.1 (Chapter 21, page 540), using
hinge loss.

You must implement two kernels, namely, both linear and Gaussian.
You must select the best $C$ value using the validation set, and the same
goes for the spread parameter $\sigma^2$ for the Gaussian kernel. That is, choose values
that give the best accuracy on the validation set.

Report the test accuracy for the different kernels, and the best value of
the hyperparameters, that should be selected based on the validation
accuracy. Accuracy is defined as the number of correct predictions over the number of
points in a given dataset (e.g., validation set or testing set).

Finally, for each kernel, please project the test data onto 2D, and show the
predictions (red for malign, green for benign, and blue for incorrect) for each test
point.

#### CSCI6390

In addition, you must also implement the inhomogeneous polynomial kernel.
You need to select the best degree and $C$ value.

Report the test accuracy and the best hyperparameters used based on the
validation accuracy. Also plot the predictions for each point in 2D.


---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared, along with the prompts used. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
