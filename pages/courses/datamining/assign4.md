<!--
.. title: CSCI4390-6390 Assign4
.. slug: dm_assign4
.. date: 2021-10-14 12:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign4:  Linear Regression

**Due Date**: Oct 22, before midnight (11:59:59PM, Alofi Time; GMT-11)


You will use the 
[Appliances energy prediction data set](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction#).
You should ignore the first attribute, which is a date-time variable,
and you should also remove the last attribute, which is a duplicate of
the previous one. You will use all remaining attributes.
For Linear Regression, use the first attribute (after removing the
date-time variable), which denotes the
Appliances Energy Use, as the response variables, with the remaining
attributes as predictor variables.

After you read in the data, and before selecting the response and
independent variables, make sure to use the standard scaler to normalize
each attribute to have mean zero and variance one. You can use the sklearn
[StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
to do this (or do it by using the formula $(x_i-\mu_X)/\sigma_X$, where
$\mu_X$ and $\sigma_X$ are the mean and variance for a single
attribute $X$, and $x_i$ is one of the values of $X$. 

Part I should be done by both CSCI4390 and CSCI6390.

---

## Part I (Both CSCI4390 and CSCI6390): Linear Regression with Regularization

You will implement ridge regression algorithm using batch gradient descent 
to solve for $\mathbf{w}$. Use equation (23.35) to compute the gradient at
each step. Choose the appropriate step size value
$\eta$, and regularization constant $\alpha$, based on the validation set.

You should use the first 13735 points as training, the next 2000 points as
validation, and the last 4000 points for testing. 
The validation set will be used to find the best $\alpha$ and $\eta$
values. For each value of $\alpha$, first learn $\mathbf{w}$ on the
training set, and then compute the SSE value on the validation set.
The value that give the least validation SSE is the one to
choose. 

Once the best $\alpha$ and $\mathbf{w}$ have
been found, you should evaluate the model on the
testing data. In particular, you should compute the SSE value for the predictions on the test data.
You should also report the $R^2$ statistic on the test data, which is defined as: 
$$R^2=\frac{TSS−SSE}{TSS}$$
where TSS is the total scatter of the response variable 
$TSS = \sum_{i=1}^n ( y_i − \mu_Y)^2$

For initializing the $\mathbf{w}$ vector, you may use np.ones(), a vector of
all ones.

## Part II (CSCI6390): Kernel Regression

In addition, implement the kernel regression Algorithm 23.4 using Gaussian
Kernel. Choose the best $\alpha$ and spread parameter $\sigma^2$ for the
Gaussian Kernel using the validation set. Report the SSE value on the test
set for the best value of $\alpha$ and $\spread$. 

Since inverting a large kernel matrix can be computationally intensive, you
may use the first 1000 points for training, next 200 points for validation,
and the next 200 points for testing.

---

## What to submit

* Write a script named  **Assign4.py**, which will be run as
 **Assign4.py FILENAME ALPHA ETA EPS MAXITER**. FILENAME is the datafile name,  ALPHA is the
 approximation threshold $\alpha$ and ETA is the $\eta$ step size parameter.  
Further $EPS$ is the convergence threshold for the gradient descent
algorithm, and MAXITER is the maximum number of iterations to run in case
you do not reach the EPS convergence threshold.

Note that if you get "inf" errors, then lower the step size $\eta$.

* For part2, the script will be run as **Assign4-kernel.py FILENAME ALPHA
SPREAD**. Here SPREAD is the $\sigma^2$ spread parameter for the Gaussian
kernel.

* Submit a PDF file named Assign4.pdf that should include your answers.

* Submit the scripts and pdf file via submitty

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

