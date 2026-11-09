.. title: CSCI4390-6390 Assign5
.. slug: dm_assign5
.. date: 2026-11-09 08:51:00 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text

**Due Date**: Nov 18th (Wed), before midnight (11:59:59PM EST)

## Data

Download the [Segmentation
Dataset](http://www.cs.rpi.edu/~zaki/DMCOURSE/data/segmentation.csv). If chrome does not
download this file when you click, please right click and use "save link as" to download
it. This data is from the UCI Machine Learning repository [ImageSegmentation
Dataset](https://archive.ics.uci.edu/dataset/50/image+segmentation), but it has been
converted into a csv format (you can look at the UCI files for the attribute
explanations). You should parse and store the csv file as a data matrix. The first
variable is the class variable, which is categorical, and will be used as the target
variable $Y$. The remaining 19 continuous attributes will comprise the data matrix, which
comprises $n=2100$ points ($\mathbf{x}$) in $d=19$ dimensional space.

#### Preprocessing
First, use [sklearn's
MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
to make sure all attributes are between 0 and 1.

Next, use
[sklearn.train_test_split](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html),
using 42 as the random_state, to shuffle and create the training and
testing data, using 80-20 split (i.e., 80% of the data as training and the
remaining 20% as testing). Make sure to split both the data and the corresponding labels.



## Jupyter Notebook

You must submit a self-contained jupyter notebook, with all of your **code and output**.
You must use NumPy, with well known/inbuilt libraries for data input (e.g., pandas). Plots
must be in inline mode (i.e., embedded) in the notebook, using matplotlib. If you use AI
to assist with the assignment, you must clearly document the tool used, and the prompts
used for each part of the assignment. Include the prompts as markdown cells in your
notebook (for each part/instance). 

## Multi-class Logistic Regression


Implement the multi-class logistic regression algorithm as described in
Algorithm 24.2 (Chapter 24, page 634), i.e., stochastic gradient ascent (SGA). 
In line 6, instead of
initializing with zeros, use np.random.randn instead. This way you'll get
different initialized weights in each run, and thus you'll be able to
explore more. Also, you may cap the maximum iterations of the repeat-until
loop in addition to checking for convergence.

You should use the scipy.special.softmax or scipy.special.log_softmax function rather than your own,
since it is more robust.

Also, the loops in line 8, 11, 15, and 18 run from 1 to $K-1$, but you can
just make it 1 to $K$, so that all class weight vectors are learned (the
pseudocode assumes that the last class the base class, and therefore its
weight vector is the zero vector). As such, both approaches are fine.

Your script should print out the learned weight vector(s), and plot the training loss.
Finally, compute the F1 score and accuracy of your model on the test data. That is, predict the class
for each point, by assigning it to the max probability class, and then compute the
macro-F1 score and the accuracy. You may use the sklearn's f1_score and accuracy_score
functions to compute these.

**CSCI6390** In addition, implement a **mini-batch** version of the
logistic regression. That is, instead of using a single point to compute
the gradient as in eq (24.19), compute the gradient for a batch of points
at the same time (you can make batch size a parameter and try different
values), and the batch gradient will be the sum of the individual gradient
from each point. At the same time, line 10 will now iterate over the batch
of points, and update the class weights once per batch (as opposed to once
per point). Plot the training loss, and also the test F1 and accuracy for the mini-batch
version. How does it compare to SGA?


## Submission

Submit your notebook via submitty, named **assign5.ipynb**. The notebook should
be self-contained, i.e., it should include all output from all the parts,
including figures. It should not hardcode file paths, but rather assume that
the datafile is in the current directory, so only the input filename
(segmentation.csv) should be used. Do not submit the datafile.


## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating the
academic honesty principle (e.g., code similarity, or failure to disclose AI
tools) will get an automatic F grade on the course and will be referred to the
dean of students for disciplinary action.
