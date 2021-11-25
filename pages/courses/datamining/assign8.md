<!--
.. title: CSCI4390-6390 Assign8
.. slug: dm_assign8
.. date: 2021-11-24 19:00:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign8: Spectral Clustering

**Due Date**: Dec 6, before midnight (11:59:59PM, Alofi Time; GMT-11)


You will use the 
[Appliances energy prediction data set](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction#).
You should ignore the first attribute, which is a date-time variable,
and you should also remove the last attribute, which is a duplicate of
the previous one. Also, the first attribute (after removing the
date-time variable), which denotes the
**Appliances Energy Use**, will NOT be used for clustering; instead we
will use it as the cluster label to assess the performance of the
clustering methods. Thus, ignoring "date", "Appliances", and "rv2", 
the remaining attributes will be used as the data for clustering.

Note that the **Appliances Energy Use** attribute takes values in the range
$[10,1080]$. However, for clustering, we will group these values into 4
"true" clusters: $c_0$ is for values in the range $[10,40]$, $c_1$ for
values $(40,60]$, $c_2$ for values $(60,100]$, and $c_3$ for values
$(100,1080]$.

---

# CSCI4390/6390: Spectral Clustering

Implement the spectral clustering algorithm 16.1 on page 406.
Use the 'Appliances' attribute as
the true cluster label as described above, and use it for the clustering
evaluation. 

For the adjacency matrix use the Gaussian kernel. Choose spread value that
works well.

Show results on 1000 points, sampled from each class via **stratified sampling**,
so that you choose a proportional number of points from each cluster
label. You can use [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html) from scikit-learn for
stratified sampling.

Your program output should consist of the following information:

* The cluster sizes
* The 'F-measure' for your clustering (computed via Eq(17.4) on pg 429).

Run your code at least 10 times with different random 1000 sampled points, 
and report the clustering with the best F-score.

---

## What to submit

* Write a script named as **Assign8.py**, which will be run as 
      
   Assign7.py FILENAME k n spread obj
   
 FILENAME is the datafile name, $k$ is the number of clusters to find, and
 $n$ is the number of data points to use (default=1000), $spread$ is
 the spread value for Gaussian kernel ($\sigma^2$), and finally $obj$ is the spectral clustering
 objective -- one of 'ratio', 'asymmetric' or 'symmetric', where the latter
 two refer to the type of Laplacian for normalized cut objective.

 Note that you should report the
 output for $k=4$, but your code should run for any input value of $k$.

* Submit a PDF file named Assign8.pdf that should include your output. 
 **Failure the submit the PDF will result in lost points.** 

* Submit the scripts and pdf file via submitty

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

