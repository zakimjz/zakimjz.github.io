.. title: CSCI4969-6969 Assign3 
.. slug: mlib_assign3
.. date: 2020-03-30 09:21:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text

Attention for Secondary Structure Prediction 
--------------------------------------------
Due: March 6th, before midnight

In this assignment, you will implement one transformer block, i.e.,
applying attention over the input protein sequence to predict the
secondary structure at each position.

We will use the same dataset as for Assign2. Namely, the
http://ww.cs.rpi.edu/~zaki/MLIB/train_SS.txt (training dataset)
comprises 5365 protein sequences, along with the secondary structure
(SS) label at each residue position. Each line in the file contains a
protein sequence, followed by a space, followed by the label sequence
(there is a one-to-one correspondence between an amino acid and the SS
label). Likewise the http://ww.cs.rpi.edu/~zaki/MLIB/test_SS.txt (test
dataset) comprises 514 sequences, along with the true labels, in the
above format. 

Given an input sequence $x_1, x_2, ..., x_n$, where each $x_i$ is a
$d$-dimensional vector (e.g., pretrained vector, or a one-hot vector)
over a suitable vocabulary (e.g., single amino acids, or ngram words of
size 3, 5, etc), you will predict the corresponding SS label for that
position.

You are required to implement the transformer block that considers the
pair-wise attention scores between the center word, and other words
within a block $w$. For this, you should use the key $K$, query
$Q$, and value $V$ representations (in a lower dimensional subspace)
that rely on the corresponding projection matrices $W^K, W^Q, W^V$.
You must write the code that computes the attention and then the final
value representation for each word, which will then be mapped back to
the original dimensionality $d$, via another matrix $W^O$. 

After the attention update, we can then pass the word vectors through a
feed-forward network (FFN with relu activation), followed by a softmax
output layer for each position in the input. You will then measure the
cross-entropy loss per position, and sum them to compute the final loss
for the given input sequence.

Note that the parameters $W^K, W^Q, W^V, W^O$ and the parameters for
the FFN and softmax are all shared!

Note that the input is given as an amino acid sequence, so depending on
the word (or ngram) size, you first have to convert it into a sequence
of words using a sliding window, so you can look up the vector
representation. Second, the block size $w$ is like the context size,
in that you should be looking at the attention between the center words,
and $w$ words to the left and $w$ to the right.

Once you have implemented the basic attention module, you may play with
more advanced variations like multiple attention layers, residual
connections, and layer normalization.

Submission
~~~~~~~~~~

Submit **assign3.py** via submitty, along with an output file that
summarizes the results of your method in terms of training and testing
accuracy values.
