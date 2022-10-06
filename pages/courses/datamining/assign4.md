<!--
.. title: CSCI4390-6390 Assign4
.. slug: dm_assign4
.. date: 2022-10-5 12:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign4:  Linear Regression

**Due Date**: Oct 14, before midnight (11:59:59PM)

We will continue with the [Online News Popularity](https://archive.ics.uci.edu/ml/datasets/online+news+popularity)
dataset as in previous assignments. This dataset has 61 attributes and 39644
points. 
Ignore the following attributes for this assignment: 0-1,
4-6, 13-38. We will use all the remaining attributes, but with the last attribute
(60; shares) as the target variable. Thus you will have 29 independent
attributes and 1 dependent or target attribute. Your goal is to build a
regression model to predict the number of shares of a news article.

---

## Data Preprocessing

Set
np.random.seed(42) and then shuffle the points using np.random.shuffle.
Next, split the data into three parts after shuffling the points, by taking 
the first 31715 points as
training data, the next 3964 points as validation data, and the last 3965
points as the test data (that is, 80-10-10 split).

Since the attributes have different scales, you should next 
standardize the **training data** so that each independent attribute has mean zero and variance one. 
You can use the sklearn [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
to do this, or do it by using the formula $(x_i-\mu_X)/\sigma_X$, where
$\mu_X$ and $\sigma_X$ are the mean and standard deviation for the
attribute $X$, and $x_i$ is one of the values of $X$. There is no need to
standardize the target variable. Make a note of the training data mean and
standard deviation.

Then, standardize both the validation and test data independent
attributes using the **training mean and training std** for each attribute.

Finally, augment the training, validation and testing datasets by adding a
columns of ones as the first dimension. Make sure to keep the target
variable as separate from the independent variables for all three splits.

---

## Part I: Linear Regression via QR Factorization

Implement the linear regression algorithm via QR factorization,
namely Algorithm 23.1 on page 602 in Chapter 23.

You must implement QR factorization on your own, as described
in Section 23.3.1 (you cannot use numpy.linalg.qr or similar function).

Next,  using the $\mathbf{Q}$ and the $\mathbf{R}$ matrices, you must
solve for the augmented weight vector $\mathbf{w}$.
 **CSCI4390** can
use **numpy.linalg.inv** for your solution, but **CSCI6390** must implement backsolve via backsubstitution 
on their own without using the inv function. See Example 23.4 on how backsolve works.

After you have computed the weight vector $\mathbf{w}$,
you should compute the SSE value for the predictions and also the
$R^2$ statistic on the test data, where: 
$$R^2=\frac{TSS−SSE}{TSS}$$
where TSS is the total scatter of the response variable 
$TSS = \sum_{i=1}^n ( y_i − \mu_Y)^2$


## Part II: Linear Regression with Regularization

Implement ridge regression algorithm (Algo 23.3 on page 610), but using *batch* gradient descent 
to solve for $\mathbf{w}$, via equation (23.35). That is, instead of doing
lines 5-7, just use eq (23.35) to compute the gradient, and then update the
weight vector. Repeat until convergence.

Use $\eta=1e-6$, but choose the appropriate regularization constant $\alpha$, based on the validation set, as follows: 
For each value of $\alpha$, first learn $\mathbf{w}$ on the
*training set*, and then compute the SSE value on the *validation set*.
The value that give the least validation SSE is the one to
choose. 

Once the best $\alpha$ and corresponding $\mathbf{w}$ have
been found, you should evaluate the model on the
testing data. In particular, you should compute the SSE value for the predictions on the test data.
You should also report the $R^2$ statistic on the test data.

For the $\alpha$ value try powers of 10 (e.g., 0, 1, 10, 100, 1000, 10000,
etc), and then narrow down the range.

---

## What to submit

* Submit your python notebook, that contains the solution and output, 
suitably annotated/commented. Name the notebook: assign4.ipynb.


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

