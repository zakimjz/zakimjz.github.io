<!--
.. title: CSCI4390-6390 Assign7
.. slug: dm_assign7
.. date: 2022-11-08 20:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign7: RNNs

**Due Date**: Nov 15, before midnight

We will use the [Spoken Arabic
Digits](https://archive.ics.uci.edu/ml/datasets/Spoken+Arabic+Digit)
dataset. This dataset comprises a training and testing dataset. Each dataset
records different utterances of digits from 0 to 9 in Arabic. For each
digit, 13 features are measured at each time point, though different digits
have different number of time points for each sequence. That is, each person
has a $\tau \times 13$ sequence for a given digit. Different persons are
separated by a blank row in the data files. For a given person, each row is
a feature vector of length 13, and the next $\tau$ rows (until the next
blank or end of file) represent the sequence for that person. 

Also, in the training data the first 660 persons all utter '0', the next 660
utter '1', and so on, until digit '9'. Thus, for each sequence there is only one output label,
namely the digit being pronounced. 

In the testing data, the format is the same, except each digit has 220
persons, so the first 220 persons utter '0', next 220 utter '1', and so on.
See [Spoken Arabic Digit Documentation](https://archive.ics.uci.edu/ml/machine-learning-databases/00195/documentation.html) for more details.

Your task is to implement the RNN algorithm 26.1 (on page 679) from scratch
in numpy, though you should use the scipy.special.softmax function rather than your own,
since it is more robust.

There is one deviation from Algo 26.1. Since there is only one class label
per input sequence, there is only one final output from time $\tau$, as
discussed at beginning of lecture 20. Therefore, you should adjust the
forward and backwards steps in lines 13, 18, and 19, as required.

You should use cross-entropy loss to predict the digit being spoken. The
output layer should use softmax, whereas the hidden layers should use ReLU. 

Note that sequences are of different lengths, but is easier to just process them one
by one (batch size of one). There is no need to try to pad them to be of the same max length, as
long as you only do the forward and backward steps only for the actual sequence
length $\tau$.

Train
on the testing set, and report both the training accuracy and average
cross-entropy loss, and then finally report the testing accuracy and loss.

---

## What to submit

* Submit your python notebook, that contains the solution and output,
suitably annotated/commented. Name the notebook: **assign7.ipynb**.


* Submit the notebook file via submitty. Your code must be self-contained,
    and must not hard code file names. You can assume the data files lie in
    the local dir.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

