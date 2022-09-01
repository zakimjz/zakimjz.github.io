.. title: CSCI4390-6390 Assign1
.. slug: dm_assign1
.. date: 2022-08-31 13:51:00 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text


#Assign1: Data Exploration 

**Due Date**: Sep 9th (Friday), before midnight (11:59:59PM; EDT)

Download the [Online News Popularity](https://archive.ics.uci.edu/ml/datasets/online+news+popularity) dataset
from the UCI Machine Learning repository. This dataset has 61 attributes
and 39797 points. You will ignore the following attributes for this
assignment: 0-1, and 13-38. So, you'll be left with 33 attributes that
you'll use. Complete the following tasks.

## Mean vector and total variance

Compute the mean vector $\mathbf{\mu}$ for the data
matrix, and then compute the total variance $var(\mathbf{D})$; see
Eq. (1.8) for the latter.

## Covariance matrix (inner and outer product form)

Compute the sample covariance matrix  $\mathbf{\Sigma}$  as **inner
products** between the attributes of the centered data matrix (see Eq.
(2.38) in chapter 2). Next compute the sample covariance matrix as sum
of the **outer products** between the centered points (see Eq. (2.39)).

## Correlation matrix as pair-wise cosines

Compute the correlation matrix for this dataset using the formula for
the cosine between centered attribute vectors (see Eq. (2.30)). 

Output which attribute pairs are i) the most correlated, ii) the most
anti-correlated, and iii) the least correlated?


## Visualization
Create the scatter plots for the three interesting pairs using
matplotlib and visually confirm the trends, i.e., describe how each of
the three cases results in a particular type of plot.

## (CSCI 6390 Only) Change of basis 

Create a new orthogonal basis for the dataset as follows: Keep the first
dimension as is as the new first dimension. For the second dimension, remove
its projection along the first dimension to obtain the new second dimension.
For the third dimension, first remove its projection along the new first
dimension, and then take the resulting vector and remove its projection
along the new second dimension to obtain the new third dimension. Proceed in
this way by taking each dimension and subtract its projection along all
previous (new) dimensions to obtain the new dimension. This will give you a
new orthogonal basis for the data. 

Finally, compute the total variance in the new basis and compare it with the
total variance in the original basis. What happens? Why?


## Submission

Submit your code via submitty. Name your jupyter notebook:
**assign1.ipynb**. You must use Python 3 (only versions 3.9 or 3.10).

You may assume that the input CSV data file *OnlineNewsPopularity.csv*
resides in the local directory of the notebook. You **MUST NOT**
hard code the file path, rather use "./OnlineNewsPopularity.csv" as the
filename, and do not change or manipulate the input file in any way. All
feature subset selection must take place inside the notebook. This
way the TAs can run your notebook with ease.

The notebook should contain the executed output of each cell and plots, and
you must add comment blocks corresponding to the
different subtasks (e.g., mean vector and total variance, covariance matrix,
etc), so the TAs can quickly check the results. 


The output of the different blocks should comprise the mean vector,
total variance, covariance matrix via inner and via outer product,
correlation matrix, and the scatter plots (using **matplotlib**). Your
observations on which attributes are most, least, and anti-correlated must
appear as comment blocks in the notebook.

CSCI6390 students must also
show the code for change of basis, and the output for the total variance in
the new space, and their answer as a comment block.


Note that you are allowed to use built-in NumPy/Python functions/libraries (e.g., [csv](https://docs.python.org/3/library/csv.html)) for reading and
parsing the input file, but you should NOT use any of the built-in functions
like **cov** for this assignment. You may however verify your answers by
comparing to the results from the built-in methods.

### Tutorial on Python and NumPy

For those not that familiar with python or NumPy, you may search online
for tutorials, e.g. https://docs.python.org/3/tutorial/ or
https://numpy.org/doc/stable/


### Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.
