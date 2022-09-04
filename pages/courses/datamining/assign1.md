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
and 39644 points. You will ignore the following attributes for this
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
anti-correlated, and iii) the least correlated? You must print the "actual" names of these columns as well as the dimension index. For example, dimension 0 is named "n_tokens_title". The names and descriptions are given on the UCI dataset link above.


## Visualization
Create the scatter plots for the three interesting pairs using
matplotlib and visually confirm the trends, i.e., describe how each of
the three cases results in a particular type of plot. Based on the attribute
description, do the results make sense? Why or why not?

## (CSCI 6390 Only) Change of basis 

Create a new orthogonal basis for the dataset as follows: 
First, set the seed as **np.random.seed(42)** so that everyone will get the
same answer. Next, generate a new orthonormal basis for the data as follows:
First, generate a random $d$-dimensional vector using
*np.random.random_sample*, and set it as the new first dimension $U_0$ after
making it a unit vector. 
For the second dimension, generate a random $d$-dimensional vector and remove
its projection along $U_0$, and make it a unit vector to obtain the new second dimension, $U_1$.
For the third dimension, first generate a random $d$-dimensional vector and
remove its projections along $U_0$ and then $U_1$, and then make it a unit
vector, which gives you $U_2$. In general, for the $i$-th new dimension
$U_i$, first generate a random $d$-dimensional vector and then
subtract its projection along all previous dimensions $U_j$, where $j < i$, and then make it a unit vector. This will give you a new orthogonal (and normal) basis for the data. This procedure is called the Gram-Schmidt Orthogonalization. 

Finally, you have to project the original data into the new space to obtain
the coordinates of each point. This can be done by creating a matrix $U$
whose columns are $U_0, U_1, U_2, ..., U_d$, and then simply multiplying the
original data $D$ by $U$, i.e., new data $D' = D U$.


Finally, compute the total variance of $D'$ in the new basis and compare it with the
total variance of $D$ in the original basis. What happens? 


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
for tutorials, e.g. [Python Tutorial](https://docs.python.org/3/tutorial/) or
[NumPy Doc](https://numpy.org/doc/stable/).


### Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.
