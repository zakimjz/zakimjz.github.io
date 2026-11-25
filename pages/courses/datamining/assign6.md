<!--
.. title: CSCI4390-6390 Assign6
.. slug: dm_assign6
.. date: 2026-11-24 9:23:01 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text
-->

# Assign6: Support Vector Classification

**Due Date**: Nov 8, before midnight (11:59:59PM)

---

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
Then, augment the dataset by adding a column of ones.

Next, use
[sklearn.train_test_split](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html),
using 42 as the random_state, to shuffle and create the training and
testing data, using 80-20 split (i.e., 80% of the data as training and the
remaining 20% as testing). Make sure to split both the data and the corresponding labels.

Furthermore, split the training dataset again in 80% for actual training, and 20% for
validation dataset. Use random_state of 42 for the train_test_split function to create
this split too.

In the end you should have 1344 training points, 336 validation points, and 420 testing points.

Use sklearn's MinMaxScaler to make sure all attributes are between 0 and 1. Since there
are 7 classes in this dataset, you'll have to create 7 different SVM models, one per
class, where the targeted class is coded as $+1$ and all the other classes as $-1$. This
is called one-vs-rest classification, which will result in 7 different, independent
hyperplanes.


## Jupyter Notebook

You must submit a self-contained jupyter notebook, with all of your **code and output**.
You must use NumPy, with well known/inbuilt libraries for data input (e.g., pandas). 
If you use AI
to assist with the assignment, you must clearly document the tool used, and the prompts
used for each part of the assignment. Include the prompts as markdown cells in your
notebook (for each part/instance). 


---

## SVM

You will implement the dual SVM Algorithm 21.1 (Chapter 21, page 540), using
hinge loss. One difference is that instead of initializing the $\alpha_i$ values to $0$,
please use some small random numbers for different initial starting values.

You must implement two kernels, namely, linear and Gaussian. While you'll use the training
set to train the SVM model, you must select the best $C$ value using only the validation set, 
and the same goes for the spread parameter $\sigma^2$ for the Gaussian kernel. That is, choose values
that give the best F1 on the validation set. In other words, for each value of C that you
want to try, train the SVM using that value of C on the training set. Then evaluate its
performance on the validation set. Keep the C that has the best F1 score on the validation
set, along with the corresponding $\alpha_i$ values. Then use those $\alpha_i$'s on the
testing set to compute the final test performance, as noted below.

Once the best hyperparameters have been found for each class, 
report the test F1 and accuracy for the different kernels, and the best value of
the hyperparameters.

Finally, note the macro-F1 score, namely, the average of all the F1 scores for all seven
classes (from the best models for each class). 

Repeat this for the linear kernel and the Gaussian kernel.


#### CSCI6390

In addition, you must also implement the inhomogeneous polynomial kernel.
You need to select the best degree (try 2 and 3) and $C$ values based on the validation F1 score.

Report the test accuracy and the best hyperparameters used based on the
validation accuracy, and report the macroF1 score.


---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared, along with the prompts used. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
