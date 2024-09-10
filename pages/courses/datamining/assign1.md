.. title: CSCI4390-6390 Assign1
.. slug: dm_assign1
.. date: 2024-09-06 13:51:00 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text


# Assign1

**Due Date**: Sep 17th (Tue), before midnight (11:59:59PM EDT)

Download the [Steel Industry Energy Consumption
Dataset](https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption) from the UCI
Machine Learning repository. Extract the Steel_industry_data.csv datafile. You should parse and
store the data as a data matrix, focusing only on the 6 continuous
attributes (see datafile or link above for names/descriptions). Thus, your data matrix
will have 35040 points in 6 dimensions.

You must submit a self-contained jupyter notebook, with all of your **code
and output**. You must use NumPy, with well known/inbuilt libraries for data
input (e.g., pandas). Plots must be in inline mode (i.e., embedded) in the
notebook, using matplotlib.

## Part I: Basic Stats

### a. Mean

Compute the sample mean vector $\mathbf{\mu}$ for the data matrix using the
column view in $\mathbf{R}^n$. That is, project the attribute vectors $X_j$
onto the ones vector $\mathbf{1}$. Use matrix operations instead of a for
loop. Verify the answer using the numpy mean function.

### b. Variance

Compute the sample variance for each attribute $\sigma_j^2$ (for all
$j=1,2,...,d$) using the column view. That is, use the avg. squared norm of
the centered attribute vectors $\bar{X}_j$. Verify the answers using the
numpy var function.

Next, compute the total variance $var(\mathbf{D})$ (see Eq. (1.8)), and
verify that the sum of all the attribute variances equals the total
variance.


###c. Covariance matrix

Compute the sample covariance matrix  $\mathbf{\Sigma}$ as **inner
products** between the attributes of the centered data matrix (see Eq.
(2.38) in chapter 2). Use matrix operations. This is the column view.

Next, compute the sample covariance matrix as sum of the **outer products**
between the centered points (see Eq. (2.39)).  This is the row view.

Print the matrix from both the approaches. You can verify your output using
numpy cov function (make sure to set rowvar as False and bias as True).


###d. Correlation matrix

Compute the correlation matrix for this dataset using the formula for the
cosine between centered attribute vectors (see Eq. (2.30)), i.e., dot
products between normalized and centered attribute vectors; use matrix
operations.

Output which attribute pairs are i) the most correlated, ii) the most
anti-correlated, and iii) the least correlated or uncorrelated?
Create the scatter plots for these three interesting pairs and visually
confirm the trends, i.e., describe how each of the three cases results in a
particular type of plot.


## Part II: Eigenvectors and Principal Components

Compute the first two eigenvectors of the covariance matrix
$\mathbf{\Sigma}$ using the power-iteration method.

Let $\mathbf{X}_0$ be a $d \times 2$ (random) matrix with two non-zero
$d$-dimensional column vectors, and let $\mathbf{X}_t$ be the current
estimate for the eigenvectors, where $t$ is the step number.

We will iteratively orthogonalize,
normalize, and left multiply with $\mathbf{\Sigma}$. That is, first
orthogonalize the second column with respect to the first one by
subtracting its projection along the first column (see section 1.3.3 in
chapter 1). After orthogonalizing, normalize both columns to be unit
length, and then do the left multiplication

$$\mathbf{X}_{t+1} = \mathbf{\Sigma} \; \mathbf{X}_t$$

The matrix $\mathbf{X}_t$ will contain the first two eigenvectors after
convergence.

To get the eigenvalues, compute the ratio of the values in a column
after versus before the update (for, say, the max valued element).
These denote the current estimates for each of the
corresponding eigenvalues, $\lambda_1$ and $\lambda_2$ (store these
estimates for plotting below).
Next, orthogonalize and normalize the vectors,
and repeat the above steps until convergence.

To test for convergence, compute the Frobenius norm between
$\mathbf{X}_{t+1}$ and $\mathbf{X}_t$. If the difference is less than some
threshold $\epsilon$ (say $10^{-6}$) then stop. Both matrices are assumed to be
orthogonalized and normalized.


Once you have obtained the two eigenvectors $\mathbf{u}_1$ and
$\mathbf{u}_2$,
print out $\mathbf{u}_1$ and $\mathbf{u}_2$, and $\lambda_1$ and
$\lambda_2$.
You can verify your answer using numpy linalg.eigh function (note that this
function prints them from smallest to largest, so you should reverse the
order; and note that the eigenvectors are columns, not rows).

Next, plot the graphs for the estimates of $\lambda_1$ and $\lambda_2$
as a function of $t$.
Furthermore, (scalar) project each of the original data points $\mathbf{x}_i$ onto
those two vectors, and plot these projected points in the two new dimensions (you should try to use matrix operations for this).


Finally, compute the variance of the projected points along $\mathbf{u}_1$
and $\mathbf{u}_2$. What is their relationship to $\lambda_1$ and
$\lambda_2$.

## Part III. Paper/Pencil Exercises

Submit your solutions to the following questions:
* Chapter 2: Q9, Q12
* Chapter 7: Q1, Q2

**CSCI6390 Only**: In addition do: Chapter 2, Q10; Chapter 7, Q6.

You can write out the solutions on paper, take an image and attach it so it
displays in your notebook. For example, you can call "from IPython.display import Image", and then use 
Image("<IMG_NAME>"). 

## Submission

Submit your notebook via submitty, named **assign1.ipynb**. The notebook
should be self-contained, i.e., it should include all output from all the
parts, including figures. It should not hardcode file paths, but rather
assume that the csv datafile is in the current directory, so only the csv
filename should be used. Do not submit the datafile.

For the paper-pencil questions, embed the image in your notebook, and also
submit the image file along with the notebook file.

If you decide to consult ChatGPT (or other similar AI tools), you must
declare this in your notebook, with a brief text description of your
successes and failures, e.g., what prompts you tried, what worked, what did
not work, how you fixed it, etc. Include this as a markdown cell in your
notebook.

For those not that familiar with python or NumPy, you may search online for
tutorials, e.g. [Python tutorial](https://docs.python.org/3/tutorial) or
[NumPy](https://numpy.org/doc/stable).

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating
the academic honesty principle (e.g., code similarity, or failure to
disclose AI tools) will get an automatic F grade on the course and will be
referred to the dean of students for disciplinary action.
