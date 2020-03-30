.. title: CSCI4969-6969 Assign2 
.. slug: mlib_assign2
.. date: 2020-03-30 09:21:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text

Protein Secondary Structure Prediction 
--------------------------------------
Due date: Mon 24th Feb, before midnight

In this assignment, we will use the word embeddings for ngrams (from
assign1) to predict the secondary structure for each position in a
protein sequence.

The http://www.cs.rpi.edu/~zaki/MLIB/assignments/train_SS.txt (training
dataset) comprises 5365 protein sequences of length at most 700, along
with the secondary structure (SS) label at each residue position. Each
line in the file contains a protein sequence, followed by a space,
followed by the label sequence (there is a one-to-one correspondence
between an amino acid and the SS label). 

Likewise the http://www.cs.rpi.edu/~zaki/MLIB/assignments/test_SS.txt
(test dataset) comprises 514 sequences, along with the true labels, in
the format. Obviously, during testing, you cannot look at the labels,
but you can use the labels to assess how well your model performs.

The data is from the paper https://arxiv.org/pdf/1403.1347.pdf (Deep
Supervised and Convolutional Generative Stochastic Network for Protein
Secondary Structure Prediction). The training sequences are from the
cullPDB server, and the testing are from the harder cb513 dataset.

The SS labels belong to an alphabet of size 8, denoting 8 different
types of secondary structures, namely: 'L', 'B', 'E', 'G', 'I', 'H',
'S', 'T'. There correspond to 3-helix(G), 4-helix (H), 5-helix (I),
residue in isolated beta-bridge (B), extended strand in beta-ladder (E),
H-bonded turn (T), bend (S), and loop (L).

Your task is the implement approach IV, as described in
http://www.cs.rpi.edu/~zaki/MLIB/lecture8.pdf. That is, train the
word2vec model with ngram size $n$ and embedding dimensionality $d$.
Store the embeddings in a file as done in assign1. Next, define a
context size $w$, and for each position $i$ in the input sequence
extract the vector embedding for the ngram centered at position $i$.
Next extract the embeddings for the $\pm w$ ngrams surrounding the
center ngram as the context embeddings.

From the center word embeddings, say $v_i$ and the context word
embeddings $v_j$ for :math:`j \in i \pm w`, create two types of
representations: 1) add or average them to obtain a $d$ dimensional
vector which will be used as input to an MLP that predicts the 8 types
of labels. 2) concatenate the vectors to obtain a :math:`d \times (2w+1)`
dimensional input vector for an MLP.

Test various combinations of ngrams including $n=1,3,5$, and context
windows $w=1,2,3,...$. Report the best prediction accuracy on the test
set.

If you are feeling ambitious, then also include a comparison with an RNN
or LSTM based model.

Submssion
~~~~~~~~~

Submit your code via submitty as a python script or notebook, named **assign2.py** or **assign2.ipynb**.

You should include the various prediction accuracy values on the test
data with various values of the parameters, and your best results.

*Update: Everyone should also evaluate the classification accuracy
on the pretrained 100d embeddings from the ProtVec paper. This will
allow you to compare your embeddings vs those from the paper.*

You can download the file **protVec_100d_3grams.csv** from the data site:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/JMFHTN
