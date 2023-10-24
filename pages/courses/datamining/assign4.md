<!--
.. title: CSCI4390-6390 Assign4
.. slug: dm_assign4
.. date: 2023-10-23 13:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign4: Decision Trees

**Due Date**: Oct 30, before midnight (11:59:59pm)

Download the [Wine Quality
Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality) from the UCI
Machine Learning repository. We will use winequality-white.csv as the
*training dataset* and winequality-red.csv as the *testing* dataset.
The white wine dataset has 4898 points, and the red wine data has 1599
points. There are 12 attributes in total, with the last attribute "quality"
denoting the integer valued target variable. 

---

Implement the decision tree algorithm as described in
Algorithm 19.1 (Chapter 19, page 488). 

Your script should print out the actual decision tree, and also the final
accuracy value on the test data. That is, you must first construct the
decision tree using the training dataset, and then apply the decisions to
each point in the test set to classify it. 

For evaluating the best splits use the information gain based on the entropy
before and after the split. Note that CSCI6390 students should also
implement the information gain based on the gini index approach (see also
below for reporting best model).

Since we do not have any categorical
attributes, you only have to focus on numeric attributes. Further, for
the numeric attributes, you can implement the information gain computation
on the different splits using your method of choice. An efficient
implementation is given in Algo 19.2 on pg 492, but you can implement a
simpler approach, as long as it is correct.

Your code should take as input the dataset, the minimum node size $\eta$ and
the minimum purity $\pi$, and it should print out the decision tree with
each child indented and aligned, as noted next. Try different values of
$\eta$ and $\pi$ and show the tree that results in the highest accuracy on
the test set. For CSCI6390, report the best tree resulting from both entropy
and using gini (also note which gives better test accuracy).

For printing the decision tree, please use the format below, which gives an
example of a tree generated on the [Iris
Dataset](https://archive.ics.uci.edu/dataset/53/iris) which has 150 points
from three types of Iris flowers. The decision tree, with $\eta=5$ and
$\pi=0.98$, should be printed in the following format (for Iris, the
file 'iris.data' contains the dataset, and the file 'iris.names' the
attribute names):
```
 1. petal length <= 2.45, size=150
 2.  | leaf: class=Iris-setosa, p=1.0, size=50
 3.  | petal width <= 1.75, size=100
 4.  |  | petal length <= 4.95, size=54
 5.  |  |  | petal width <= 1.65, size=48
 6.  |  |  |  | leaf: class=Iris-versicolor, p=1.0, size=47
 7.  |  |  |  | leaf: class=Iris-virginica, p=1.0, size=1
 8.  |  |  | petal width <= 1.55, size=6
 9.  |  |  |  | leaf: class=Iris-virginica, p=1.0, size=3
10.  |  |  |  | leaf: class=Iris-versicolor, p=0.6666666666666666, size=3
11.  |  | petal length <= 4.85, size=46
12.  |  |  | leaf: class=Iris-virginica, p=0.6666666666666666, size=3
13.  |  |  | leaf: class=Iris-virginica, p=1.0, size=43
```
Don't print the line numbers. They are there just to make the references
below clear. 

Here the root decision, 'petal length <= 2.45' is on line 1. It prints the
attribute name and the split value 2.45, as well as the size of the dataset
at this point.

The root has two children -- the left child, when the root decision is true,
is given on line 2, which happens to be a leaf, so we print the majority
class in that leaf node (Iris-setosa), the fraction of points in the
majority class (p=1.0), and the size of the node (50). The right child, when
the root decision is false, is on line 3. This is not a leaf, and will be
split further, using the decision 'petal length <= 1.75'

The children node for 'petal length <= 1.75' are shown on lines 4 and 11.
Line 4 is when the decision is true and line 11 is when the decision is
false. Thus, we can see that the two children of a node are either consecutive (if one
of both of them are leaves), or they are linked by the vertical lines. Thus,
the nested structure represents the entire tree, with all leaf nodes showing
the "class" of that region.

---

## What to submit

* Submit your python notebook, that contains the solution and output,
suitably annotated/commented. Name the notebook: **assign4.ipynb**.


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

