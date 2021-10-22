<!--
.. title: CSCI4390-6390 Assign5
.. slug: dm_assign5
.. date: 2021-10-22 12:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign5: Support Vector Machines

**Due Date**: Oct 29, before midnight (11:59:59PM, Alofi Time; GMT-11)


You will use the 
[Appliances energy prediction data set](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction#).
You should ignore the first attribute, which is a date-time variable,
and you should also remove the last attribute, which is a duplicate of
the previous one. Use the first attribute (after removing the
date-time variable), which denotes the
**Appliances Energy Use**, as the response variable, with the remaining
attributes as predictor variables. 

Note that the **Appliances Energy Use** attribute takes values in the
range $[10,1080]$. However, for binary classification, we need only two
values, so for the purpose of this assignment you should consider energy
use less than or equal to 50 as the positive class (1), and energy use
higher than 50 as negative class (-1). 

You should use the first 5000 points as the training, the next 2000 points
for validation, and the next 5000 points for testing.

You will implement the dual SVM Algorithm 21.1 (Chapter 21, page 540).
You must implement the hinge loss case.

##CSCI4390 and CSCI6390

You must implement two kernels, namely, both linear and Gaussian.
You must select the best $C$ value using the validation set, and the same
goes for the spread parameter $\sigma^2$ for the Gaussian kernel.

##CSCI6390

You must also implement the polynomial kernel. You need to select the best degree and $C$ value.

---

## What to submit

* Write a script named as **Assign5.py**, which will be run as 
      
   Assign6.py FILENAME C EPS MAXITER KERNEL KERNEL_PARAM
   
 FILENAME is the datafile name,  
 C is the regularization constant, EPS is the convergence
 threshold, MAXITER is the max number of iterations to perform (in case
 you do not get convergence within EPS), KERNEL is one of the strings
 "linear", "gaussian" or "polynomial", and finally KERNEL_PARAM is
 either a float that represents the spread $\sigma^2$ for gaussian
 kernel (see Eq 5.10 on pg 147), or it is the degree $q$ for the polynomial kernel
 (use $c=1$ for the kernel constant). Note that polynomial kernel
 is only for CSCI6390.

Note that you must shuffle the
points/indexes in line 11 so that you get different permutations for the
stochastic gradient ascent in each iteration. This results in better
performance than using the fixed order.

Your script should print out the number of support vectors on the training set
(those points that are exact support vectors, with $0 < \alpha < C$),
and the final
accuracy value on the test data.
For the linear kernel you must also print
the weight vector and bias.

Note that accuracy is defined as the fraction of correct class label
predictions. So for each test point, you should predict its class as the
sign of the hyperplane equation (see Eq 21.37).
 Divide the number of correct predictions by the test data
size to get the accuracy. Report the best accuracy for each kernel on the
test data.

You can compare your results with those obtained from 
[sklearn SVM implementation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html).

* Submit a PDF file named Assign5.pdf that should include your answers
 to each of the questions (just cut and paste the output from python).
 **Failure the submit the PDF will result in lost points.** 

* Submit the scripts and pdf file via submitty

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

