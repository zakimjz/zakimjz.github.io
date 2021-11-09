<!--
.. title: CSCI4390-6390 Assign6
.. slug: dm_assign6
.. date: 2021-11-08 12:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign6: Bayes Classifier 

**Due Date**: Oct 15, before midnight (11:59:59PM, Alofi Time; GMT-11)


You will use the 
[Appliances energy prediction data set](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction#).
You should ignore the first attribute, which is a date-time variable,
and you should also remove the last attribute, which is a duplicate of
the previous one. Use the first attribute (after removing the
date-time variable), which denotes the
**Appliances Energy Use**, as the response variable, with the remaining
attributes as predictor variables. 

Note that the **Appliances Energy Use** attribute takes values in the
range $[10,1080]$. However, for multiclass classification, we will convert
these into four classes as follows: energy use less than or equal to 40
is class $c_0$, energy use greater than 40 but less than or equal to 60
is class $c_1$, energy use greater than 60 but less than or equal to 100
is class $c_2$, and finally energy use higher than 100 is class $c_3$.
Also, don't use any data scaling.

You should use the first 14735 points as the training, and the last 5000 points for testing.

##CSCI4390

Implement both the full Bayes classifier in Algo 18.1, and the naive Bayes
classifier in Algo 18.2. 

##CSCI6390

Implement both the full Bayes classifier in Algo 18.1, and the naive Bayes
classifier in Algo 18.2. However, you have to implement a mixed numeric and
categorical version, as described below.

First, discretize the attributes 'T5' and 'T_out' so that they are treated as categorical.
If value is less than or equal to 5, treat the temperature as 'L'; if value
is greater than or equal to 5 and less than 9, then treat is as 'M'; if
value is greater than 9, then treat it as 'H'. You can also code them as 0,
1, and 2, but these must be considered categorical values.

Next, treat the other 24 attributes as numeric from which you can compute the
mean and covariance matrices. 

For the 2 categorical attributes ('T5', 'T_out') you need to
estimate the joint probability as a pair of values for full Bayes, and as product of
individual attribute value probabilities for naive Bayes. 

Finally, you may assume
that the categorical attributes are independent from the numeric ones so
that the joint probability of a point can be computed as the product of the
probabilities of the numeric and categorical parts.

## Both CSCI4390 and 6390

Estimate parameters using the training data, and
report the accuracy of the testing set. You must report total accuracy, and
the class-specific accuracy and recall values -- see Eq 22.3 and 22.4 for
the later two. Report these values for the full and naive Bayes
methods.


---

## What to submit

* Write a script named as **Assign6.py**, which will be run as 
      
   Assign6.py FILENAME
   
 FILENAME is the datafile name.

* Submit a PDF file named Assign6.pdf that should include your answers
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

