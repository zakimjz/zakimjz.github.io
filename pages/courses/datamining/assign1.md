.. title: CSCI4390-6390 Assign1
.. slug: dm_assign1
.. date: 2024-09-07 08:51:00 UTC-04:00
.. tags:
.. category:
.. link:
.. description:
.. has_math: True
.. type: text

# Assign1: Interesting Projections

**Due Date**: Sep 15th (Mon), before midnight (11:59:59PM EDT)

## Data Download the [Breast Cancer Wisconsin (Diagnostic)

Dataset](<https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic>)
from the UCI Machine Learning repository. You should parse and store the data
as a data matrix. The ID variable will not be used, and the Diagnosis variable
will be used only as labels for plotting. The remaining 30 continuous
attributes will comprise the data matrix, which is $n=569$ points in $d=30$
dimensional space.

## Jupyter Notebook

You must submit a self-contained jupyter notebook, with all
of your **code and output**. You must use NumPy, with well known/inbuilt
libraries for data input (e.g., pandas). Plots must be in inline mode (i.e.,
embedded) in the notebook, using matplotlib.

## Random Projections

Your task is to find two orthogonal (and unit) projection vectors,
$\mathbf{u}_1$ and $\mathbf{u}_2$, that best approximate the data matrix,
where the goal is to minimize the mean squared error when the data is
approximated by the two orthogonal vectors. Do this via the following steps.

### a. Scale and Center the Data Matrix

Use sklearn's MinMaxScaler to make sure all attributes are between 0 and 1.
Next, center the data matrix by subtracting the mean vector from each point.

### b. Compute Total Variance

From now on we will assume that the data matrix $\mathbf{D}$ **is centered**.

Compute and print the total variance $var(\mathbf{D})$ (see Eq. (1.8)).

### c. Find Best Projection Vector

We will use a randomized approach to finding the best unit projection vector
$\mathbf{u}_1$ that has the least mean squared error (MSE):

$$MSE(\mathbf{u}_1) = \sum_{i=1}^n \|\| \mathbf{x}_i - \mathbf{p_i} \|\|^2 $$

where $\mathbf{p}_i$ is the projection of $\mathbf{x}_i$ onto $\mathbf{u}_1$.

To find $\mathbf{u}_1$ you should write a function to generate random vectors
in $d$-dim space, say using the numpy.random.randn function. For each such
random vector, make it into a unit vector (divide by its norm). Next, compute
its MSE value. Try many such random vectors (say 10,000 or 100,000) and store
the best one.

### d. Find Second Best Vector

Next, we will find another unit vector $\mathbf{u}_2$ that is **orthogonal** to
$\mathbf{u}_1$, and that still minimizes the MSE, but with respect to
$\mathbf{u}_2$.

This function is similar to that for part c. The only difference is that each
time you generate a random vector $\mathbf{u}_2$, make sure to make it
orthogonal to $\mathbf{u}_1$ (project onto $\mathbf{u}_1$ and then subtract
that from $\mathbf{u}_2$), and then convert it into a unit vector.

### e. Project Data and Plot

Now that we have found $\mathbf{u}_1$ and $\mathbf{u}_2$, we will project the
entire centered data matrix onto each one of them to obtain a projected $n
\times 2$ dataset. Plot this as a scatter plot, but make sure to label the
malignant samples as red and the benign points as green.

Finally, print the fraction of total variance captured by your two new
dimensions. The latter is the sum of the projected variances in each direction.

### f. Improving Directions

If you are interested in improving the initial random directions $\mathbf{u}_1$
and $\mathbf{u}_2$, as extra credit you may use local search. The idea is that
we can start with the best direction so far, say $\mathbf{u}_1$, and to
generate the new random directions, we perturb this vector slightly (again you
can use numpy.random.randn, but scale the values to the smaller, say in the
range (0,0.1) or (0,0.01), etc.) to generate new random directions. The idea is to search
"around" the best previous direction found. If this yields a better direction,
use that as the new best estimate, and than repeat the whole process for a few
rounds of local search. The same applies to finding the second direction.

If your local search gives better results, plot the projected points in that
space and note the fraction of total variance captured.

## Submission

Submit your notebook via submitty, named **assign1.ipynb**. The notebook should
be self-contained, i.e., it should include all output from all the parts,
including figures. It should not hardcode file paths, but rather assume that
the datafile is in the current directory, so only the input filename
(wdbc.data) should be used. Do not submit the datafile.

If you decide to consult CoPilot (or other similar AI tools), you must record
in your notebook tool and the prompts you used. Include the prompts as markdown
cells in your notebook (for each part/instance).

For those not that familiar with python or NumPy, you may search online for
tutorials, e.g. [Python tutorial](https://docs.python.org/3/tutorial) or
[NumPy](https://numpy.org/doc/stable).

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating the
academic honesty principle (e.g., code similarity, or failure to disclose AI
tools) will get an automatic F grade on the course and will be referred to the
dean of students for disciplinary action.
