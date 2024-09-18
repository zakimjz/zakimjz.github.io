<!--
.. title: CSCI4390-6390 Assign2
.. slug: dm_assign2
.. date: 2022-09-17 10:23:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign2: High Dimensional Data

**Due Date**: Sep 27, before midnight (11:59:59PM)

## Part I: High Dimensional Data

### Diagonals in High Dimensions

Your goal is the compute the probability distribution for the random
variable $X$ that represents the angle (in degrees) between any two
diagonals in high dimensions.

Assume that there are $d$ primary dimensions (the standard axes in
cartesian coordinates), with each of them ranging from -1 to 1.  There
are $2^{d}$ additional half-diagonals in this space, one for each
corner of the $d$-dimensional hypercube.

Randomly generate
 $n=100,000$ pairs of
half-diagonals in the $d$-dimensional hypercube (random $d$-dimensional
vectors with elements +1 or -1), and compute the angle
between them (in degrees).

Plot the probability distribution for three different
values of $d$, as follows $d={10,100,1000}$, that is,
plot of the angle versus the probability of observing that
angle in the sample of $n$ points for a given value of $d$. What is
the min, max, range, mean and variance of $X$ for each value of
$d$?


**CSCI6390**:  In addition, what would expect analytically? In other
words, derive formulas for what should happen to angle between
half-diagonals as $d \to \infty$. Does the probability distribution conform to this trend?
Explain why or why not?

### High Dimensional Normal Distribution

Empirically verify what happens to the high dimensional normal
distribution in terms of the distance of points from the center.

Randomly sample $n=10,000$ points from the standard multivariate normal
distribution in $d$ dimensions, where $d=10, 50, 100, 500$. You may use
**np.random.multivariate_normal** to generate this sample.

Plot the histogram of distances of points to the center of the space in $d$
dimensions. For each $d$, compute the mean distance of points to the center in $d$
dimensions, and also compute the standard deviation. How do these conform
to the theory?

## Part II: Frequent Patterns

Implement the dEclat mining algorithm 8.4 on page 231. For example,
given the dataset:
```
A B D E
B C E
A B D E
A B C E
A B C D E
B C D
```
You can assume that each line has a transaction -- a set of items, separated
by spaces. For minimum support of 3, the set of frequent itemsets should be printed out
in the format:
```
A - 4
B - 6
D - 4
E - 5
C - 4
A B - 4
A D - 3
A E - 4
A B D - 3
A B E - 4
A B D E - 3
A D E - 3
B D - 4
B E - 5
B C - 4
B D E - 3
B E C - 3
D E - 3
E C - 3
Number of frequent itemsets 19
```

Print the frequent itemsets on the
[chess.txt](http://www.cs.rpi.edu/~zaki/DMCOURSE/data/chess.txt) dataset, using
minimum support 3025.

## Part III. Paper/Pencil Exercises

Submit your solutions to the following questions:

* Chapter 6: Q4, Q8, in addition CSCI6390 students must also do Q7
* Chapter 8: Q1a, Q2, in addition CSCI6390 students must also do Q9

You can write out the solutions on paper, take an image and attach it so it
displays in your notebook. For example, you can call "from IPython.display import Image", and then use
Image("IMG_NAME").



---

## What to submit

* You must submit a jupyter notebook, with all of your **code
and output**. You must use NumPy, with well known/inbuilt libraries for data
input (e.g., pandas). Plots must be in inline mode (i.e., embedded) in the
notebook, using matplotlib. Name the notebook: assign2.ipynb.


* Your code must be self-contained,
    and must not hard code file names. You can assume the data file lies in
    the local dir.

* For the paper-pencil questions, embed the image in your notebook, and also
submit the image file along with the notebook file.


If you decide to consult ChatGPT (or other similar AI tools), you must
declare this, and submit comments in the notebook documenting your
successes and failures, e.g., what prompts you tried, what worked, what did
not work, how you fixed it, etc.


---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
