.. title: CSCI4390-6390 Assign1
.. slug: dm_assign1
.. date: 2026-09-03 08:51:00 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text

**Due Date**: Sep 14th (Mon), before midnight (11:59:59PM EDT)

## Data

Download the [Segmentation Dataset](http://www.cs.rpi.edu/~zaki/DMCOURSE/data/segmentation.csv). This data is from the UCI Machine Learning repository [ImageSegmentation Dataset](https://archive.ics.uci.edu/dataset/50/image+segmentation), but it has been converted into a csv format (you can look at the UCI files for the attribute explanations). You should parse and store the csv file
as a data matrix. The first variable is the class variable, which is categorical, and will be used only as labels for plotting in Part I, and as a supervision signal in Part II. The remaining 19 continuous
attributes will comprise the data matrix, which comprises $n=2100$ points in $d=19$ dimensional space.

## Jupyter Notebook

You must submit a self-contained jupyter notebook, with all
of your **code and output**. You must use NumPy, with well known/inbuilt
libraries for data input (e.g., pandas). Plots must be in inline mode (i.e.,
embedded) in the notebook, using matplotlib. If you use AI to assist with the assignment,
you must clearly document the tool used, and the prompts used for each part of the
assignment. 
Include the prompts as markdown
cells in your notebook (for each part/instance).
However, I strongly encourage you to do this assignment without the help of AI
if you really want to learn, and understand the concepts.

## Part I. Random Projections

Your first task is to find two orthogonal (and unit) projection vectors,
$\mathbf{a}_1$ and $\mathbf{a}_2$, that best approximate the data matrix,
where the goal is to minimize the mean squared error when the data is
approximated by the two orthogonal vectors. Do this via the following steps.

### a. Scale and Center the Data Matrix (10 points)

Use [sklearn's MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) to make sure all attributes are between 0 and 1.
Next, center the data matrix by subtracting the mean vector from each point.

### b. Compute Total Variance (10 points)

From now on we will assume that the data matrix $\mathbf{D}$ **is centered**.

Compute and print the total variance $var(\mathbf{D})$ (see Eq. (1.8)).

### c. Find Best Projection Vector (20 points)

We will use a randomized approach to find the best unit projection vector
$\mathbf{a}_1$ that has the least mean squared error (MSE):

$$MSE = \frac{1}{n} \sum_{i=1}^n \|\| \mathbf{x}_i - \mathbf{p_i} \|\|^2 $$

where $\mathbf{p}_i$ is the projection of $\mathbf{x}_i$ onto $\mathbf{a}_1$.

To find $\mathbf{a}_1$ you should write a function to generate random vectors
in $d$-dim space, say using the numpy.random.randn function. For each such
random vector, make it into a unit vector (divide by its norm). Next, compute
its MSE value. Try many such random vectors (say 10,000 or 100,000) and store
the best one.

### d. Find Second Best Vector (20 points)

Next, we will find another unit vector $\mathbf{a}_2$ that is **orthogonal** to
$\mathbf{a}_1$, and that still minimizes the MSE, but with respect to
$\mathbf{a}_2$.

This function is similar to that for part c. The only difference is that each
time you generate a random vector $\mathbf{a}_2$, make sure to make it
orthogonal to $\mathbf{a}_1$ (project onto $\mathbf{a}_1$ and then subtract
that from $\mathbf{a}_2$), and then convert it into a unit vector.

### e. Project Data and Plot (15 points)

Now that we have found $\mathbf{a}_1$ and $\mathbf{a}_2$, we will project the
entire centered data matrix onto each one of them to obtain a projected $n
\times 2$ dataset. That is, retain only the scalar projections of each centered point onto
the direction $\mathbf{a}_1$ and onto the direction $\mathbf{a}_2$, respectively. 
Plot this as a scatter plot, but make sure to label the
samples using different colors for each of the seven classes.

Finally, print the fraction of total variance captured by your two new
dimensions. The latter is the sum of the projected variances in each direction.


### f. Extra Credit: Improving Directions (10 points)

If you are interested in improving the initial random directions $\mathbf{a}_1$
and $\mathbf{a}_2$, as extra credit you may use local search. The idea is that
we can start with the best direction so far, say $\mathbf{a}_1$, and to
generate the new random directions, we perturb this vector slightly (again you
can use numpy.random.randn, but scale the values to the smaller, say in the
range (0,0.01), etc.) to generate new random directions. The idea is to search
"around" the best previous direction found. If this yields a better direction,
use that as the new best estimate, and than repeat the whole process for a few
rounds of local search. The same applies to finding the second direction.

If your local search gives better results, plot the projected points in that
space and note the fraction of total variance captured.


## Part II. Separating Directions (25 points)

We will use a randomized approach to find the best unit projection vector
$\mathbf{b}_1$ that has the maximum separation between the classes (SEP):

$$SEP = \frac{\sum_{i=1}^{k-1} \sum_{j-i_1}^k (m_i - m_j)^2}{\sum_{i=1}^k s_i^2} $$

where $m_i$ is the mean, and $s_i^2$ the variance for class $i$ along the direction
$\mathbf{b}_1$, and $k$ is the number of classes.

To find $\mathbf{b}_1$ you should write a function to generate random vectors
in $d$-dim space, say using the numpy.random.randn function. For each such
random vector, make it into a unit vector (divide by its norm). Next, compute
its SEP value. Try many such random vectors (say 10,000 or 100,000) and store
the best one.


Next, we will find another unit vector $\mathbf{b}_2$ that is **orthogonal** to
$\mathbf{a}_1$, and that still maximizes the SEP, but with respect to
$\mathbf{b}_2$. We just have to make sure that each
time you generate a random vector $\mathbf{b}_2$, make sure to make it
orthogonal to $\mathbf{b}_1$, and then convert it into a unit vector.

Now that we have found $\mathbf{b}_1$ and $\mathbf{b}_2$, we will project the
entire centered data matrix onto each one of them to obtain a projected $n
\times 2$ dataset. That is, retain only the scalar projections of each centered point onto
the direction $\mathbf{b}_1$ and onto the direction $\mathbf{b}_2$, respectively. 
Plot this as a scatter plot, but make sure to label the
samples using different colors for each of the seven classes.
How does this plot compare to the one that minimizes the MSE?

## Submission

Submit your notebook via submitty, named **assign1.ipynb**. The notebook should
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
