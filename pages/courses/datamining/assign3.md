<!--
.. title: CSCI4390-6390 Assign3
.. slug: dm_assign3
.. date: 2021-09-30 00:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign3: Kernel Discriminant Analysis

**Due Date**: Oct 8, before midnight (11:59:59PM, Alofi Time; GMT-11)


You will use the 
[Appliances energy prediction data set](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction#).
You should ignore the first attribute, which is a date-time variable,
and you should also remove the last attribute, which is a duplicate of
the previous one (note: do not modify the csv file, but rather ignore these
columns after reading in the csv in your code). 

For kernel discriminant, use the first attribute (after removing the
date-time variable), which denotes the
**Appliances Energy Use**, as the class variable, with the remaining
attributes as normal ones. However, you have to discretize the
class variable to obtain the class of each point as described next.

Note that the **Appliances Energy Use** attribute takes values in the
range $[10,1080]$. However, for discriminant analysis, we need only two
values, so for the purpose of this assignment you should consider energy
use less than or equal to 50 as class $c_1$, and energy use
higher than 50 as class $c_2$. You need to do this conversion to
create the binary class for each point.

---

## Both CSCI4390 and CSCI6390

You will implement the kernel discriminant analysis algorithm as described in
Algorithm 20.2 (Chapter 20, page 512) to find the kernel LD. Use the Gaussian kernel to
construct the kernel matrix, but you will have to play with the spread
parameter to find the best LD, e.g., the one that gives the best Fischer
objective value among the different spread parameters. You can find this by
grid-search, i.e., starting with a small value and increasing it to see
which spread value gives the highest objective value.

Once you have found the best spread parameter for the Gaussian kernel, then
project the points onto the kernel LD direction, and plot them. Use circles
for class $c_1$ and crosses for class $c_2$. Include the plot in your PDF
file.


## CSCI6390 Only: Linear Kernel

In addition to the kernel LDA algorithm, you should implement the linear
discriminant algorithm in Algorithm 20.1.

You need to find the LD dicrection, and then verify that it is the same as
the one obtained from the kernel discriminant algorithm using the linear
kernel. In other words, run kernel discriminant Algo 20.2 with linear kernel and
compute the direction, and this should match the output from Algo 20.1.

---

## What to submit

* Write a scripy named as **Assign3.py**, which will be run as 
 **Assign3.py FILENAME SPREAD**. FILENAME is the datafile name,  SPREAD is the
 spread parameter $\sigma^2$ for the Gaussian kernel.
 
Your script should print out the weight vector $\mathbf{a}$, which gives the
mixture weights for each of the feature points. You need to include the plot
in the PDF, and also provide which value of spread was used to obtain the
plot.

For the additional part for CSCI6390, show the LD direction $\mathbf{w}$
from the linear kernel in Algo 20.2, and the one from Algo 20.1.


* Submit a PDF file named Assign3.pdf that should include your answers
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

