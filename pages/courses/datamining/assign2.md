.. title: CSCI4390-6390 Assign2
.. slug: dm_assign2
.. date: 2024-09-15 13:51:00 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text

# Assign1

**Due Date**: Sep 22nd (Mon), before midnight (11:59:59PM EDT)

## Data

Download the [Breast Cancer Wisconsin (Diagnostic)
Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) from
the UCI Machine Learning repository. You should parse and store the data as a data matrix.
The ID variable will not be used, and the Diagnosis variable will be used only as labels
for plotting. The remaining 30 continuous attributes will comprise the data matrix, which
is $n=569$ points in $d=30$ dimensional space.

## Jupyter Notebook

You must submit a self-contained jupyter notebook, with all of your **code and output**.
You must use NumPy, with well known/inbuilt libraries for data input (e.g., pandas). Plots
must be in inline mode (i.e., embedded) in the notebook, using matplotlib.

## Eigenvectors and Principal Components

Compute the first two eigenvectors of the covariance matrix $\mathbf{\Sigma}$ using the
power-iteration method.

Let $\mathbf{X}_0$ be a $d \times 2$ (random) matrix with two non-zero $d$-dimensional
column vectors, and let $\mathbf{X}_t$ be the current estimate for the eigenvectors, where
$t$ is the step number.

We will iteratively orthogonalize, normalize, and left multiply with $\mathbf{\Sigma}$.
That is, first orthogonalize the second column with respect to the first one by
subtracting its projection along the first column (see section 1.3.3 in chapter 1). After
orthogonalizing, normalize both columns to be unit length, and then do the left
multiplication

$$\mathbf{X}_{t+1} = \mathbf{\Sigma} \; \mathbf{X}_t$$

The matrix $\mathbf{X}_t$ will contain the first two eigenvectors after convergence.

To get the eigenvalues, compute the ratio of the values in a column after versus before
the update (for, say, the max valued element). These denote the current estimates for each
of the corresponding eigenvalues, $\lambda_1$ and $\lambda_2$ (store these estimates for
plotting below).

To test for convergence, compute the Frobenius norm between $\mathbf{X}_{t+1}$ and
$\mathbf{X}_t$; this can be computed using **np.linalg.norm** for the difference between
these two matrices. If the difference is less than some threshold $\epsilon$ (say
$10^{-6}$) then stop. Both matrices are assumed to be orthogonalized and normalized.

### a. Eigenvectors and Eigenvalues

Once you have obtained the two eigenvectors $\mathbf{u}_1$ and $\mathbf{u}_2$, print out
$\mathbf{u}_1$ and $\mathbf{u}_2$, and $\lambda_1$ and $\lambda_2$. You can verify your
answer using numpy linalg.eigh function (note that this function prints them from smallest
to largest, so you should reverse the order; and note that the eigenvectors are columns,
not rows).

### b. Project Data and Plot

First, plot the graphs for the estimates of $\lambda_1$ and $\lambda_2$ as a function of
$t$.

Next, since we have found the optimal $\mathbf{u}_1$ and $\mathbf{u}_2$, we will project
the entire centered data matrix onto each one of them to obtain a projected $n \times 2$
dataset. Plot this as a scatter plot, but make sure to label the malignant samples as red
and the benign points as green.

Finally, i) compute the variance of the projected points along $\mathbf{u}_1$ and
$\mathbf{u}_2$, ii) What is their relationship to $\lambda_1$ and $\lambda_2$, and iii)
What fraction of the total variance is captured by the two eigenvectors.

## Submission

Submit your notebook via submitty, named **assign2.ipynb**. The notebook should be
self-contained, i.e., it should include all output from all the parts, including figures.
It should not hardcode file paths, but rather assume that the datafile is in the current
directory, so only the input filename (wdbc.data) should be used. Do not submit the
datafile.

If you decide to consult CoPilot (or other similar AI tools), you must record in your
notebook tool and the prompts you used. Include the prompts as markdown cells in your
notebook (for each part/instance).

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be your own. Any
AI tool use must be declared. Any students caught violating the academic honesty principle
(e.g., code similarity, or failure to disclose AI tools) will get an automatic F grade on
the course and will be referred to the dean of students for disciplinary action.
