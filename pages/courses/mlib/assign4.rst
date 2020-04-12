.. title: CSCI4969-6969 Assign4 
.. slug: mlib_assign4
.. date: 2020-04-05 16:21:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text

Protein Structure Prediction: Simplified AlphaFold 
--------------------------------------------------
Due: April 16th, before midnight
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this assignment, you will implement a simplified version of the
AlphaFold protein structure method. In particular, we will predict only
the distance matrix, instead of the full 3D coordinate structure.

Data
----

For training, testing and validation we will make use of the `ProteinNet
Dataset <https://github.com/aqlaboratory/proteinnet>`_. In particular,
you can start with the smaller CASP7 set, and then try the larger CASP12
set. The CASP7 dataset has 34,557 structures (training_100). The CASP12
set has 104,059 structures.

The details of the ProteinNet data are mentioned at `ProteinNet Records
<https://github.com/aqlaboratory/proteinnet/blob/master/docs/proteinnet_records.md>`_.
Each "record" contains the sequence of the protein, followed by PSSM
info, secondary structure info, tertiary structure (atomic coords of the
$N$, :math:`C_{\alpha}`, and $C$ atoms per position), an a boolean mask that
indicates whether the atomic coords are present or not. Details of how
the dataset was created and the training/validation/testing splits can
be found in the `ProteinNet paper
<https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2932-0>`_.

The training data is further split into several subsets. The full data
is training_100 that has all structures (34,557), whereas training_30
has a subset of 10,333 structures. The "30" means that sequences with
over 30% identity are removed to reduce redundancy. You can start with
the training_30 subset, or sample it down even further while developing
your code. 

You can use the `pytorch parser
<https://github.com/OpenProtein/openprotein/blob/master/preprocessing.py>`_
to read the proteinnet data. 


Method
------

The input to your method will be the training, validation and testing
files from ProteinNet.   
Given a protein sequence $S$ of length $n$ from the training set, you will read the input features from the
one-hot and PSSM info, etc, to create the :math:`n \times n \times f`
tensor for the sequence $S$, where $f$ is the number of features per $\(i,j\)$
pair in $S$. For creating $f$, you can concatenate the features
(one-hot, PSSM, info-content, etc.) for
position $i$ and $j$, and you can also add their element-wise product
and absolute value of the difference. At least try concatenation. See if
the other alternatives improve the prediction.

You will next implement the residual block framework as described in the
`AlphaFold paper <https://www.nature.com/articles/s41586-019-1923-7>`_.
However, you need not train on a 220 layer network. Rather you will
train on several block groups, where each group (of 4 blocks) cycles
through the dilations of 1,2,4,and 8. You should make the "number of
block groups" an input parameter. So if we use 2 block groups, then your
network will be trained on 8 blocks with two cycles of dilations. Each
block should be made up of the different batch-norm, ELU, projections
and dilations as described. These layers/activations will make use of
the pytorch inbuilt functions, so you have to only define the
architecture and forward function.

We will train on
each :math:`64 \times 64` tile separately. 
You can create tiles by starting at a randomly chosen 
position $\(s,e\)$, and then generating all tiles with a stride of 64
for non-overlapping tiles (or 16 or
32 if you want to have overlaps between tiles); this also assumes
that the input tensor has been zero padded as appropriate. You should
restrict $s$ and $e$ to be within the first 64 entries (after
zero-padding) along each dimension, to generate tiles that cover the
entire protein. In particular, different epochs sould start at different
$(s,e)$ locations for the same protein,
That is, after predicting the
distances for the tile, you will compare with the true distances for
that tile only. You will first need to discretize the distances between
:math:`\text{2--22} A^\circ` into 64 equal bins, and another for greater than 22. Total 65
different distance symbols. The you can use cross-entropy loss on the
predicted probabilities and true distance symbols (as a variant you can
also experiment with direct distance prediction via squared-error
loss).

You can monitor the predictions on the validation set of any
hyperparameter tuning or early stopping in terms of loss.

For testing you should report the loss, but also the accuracy of contact
prediction. That is, a pair $\(i,j\)$ is in contact if the true distance
is below :math:`8A^\circ`. So for each test sequence, you should sum up the
probabilities in the bins corresponding to the "symbols" in the range
:math:`2\text{--}8A^\circ`, and if that is over 0.5 then you can predict that pair to be in
contact. You can then report the accuracy for short, medium and long
range contacts. Short is defined as :math:`5 \le |i-j| \le 12`, medium as
:math:`12 \le |i-j| \le 23` and long as :math:`|i-j| \ge 23`. In each
category, you should report the accuracy for the top $n$, $n/2$ and
$n/5$ predictions, where $n$ is the sequence length. Finally, you should
averge the accuracy in each range over all of the test protein and
report that number.

Besides the `alphafold code
<https://github.com/deepmind/deepmind-research/tree/master/alphafold_casp13>`_
You may find the following two open-source implementations of alphafold
of value in your own implementation: `ProSPr
<https://github.com/dellacortelab/prospr>`_ and `MiniFold
<https://github.com/EricAlcaide/MiniFold>`_.


Submission
~~~~~~~~~~

Submit **assign4.py** via submitty, along with an output file (txt/pdf) that
summarizes the results of your method in terms of training and testing
accuracy values.

Your code must **not** hardcode any filenames or directories, but rather
accept them from the command line input. Your code will be run as:

| assign4.py TRAIN VAL TEST NG
|

where TRAIN is the training file (e.g., training_30), VAL is the
validation file and TEST is the testing file. Here NG is an integer that
denotes the nubmer of block groups to train on.

