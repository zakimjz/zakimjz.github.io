<!--
.. title: CSCI4949-6969 Assign4
.. slug: mlib_assign4
.. date: 2022-02-25 19:00:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->


# Assign4: Protein Contextual Embeddings via BERT

**Due Date**: Mar 6, before midnight (EST 11:59:59PM)

In this assignment, you will implement the BERT embedding method for protein
sequences.

Your code should implement on your own the transformer approach with masked
language model for learning contextual embeddings for input sequences. You
can use the pytorch layer norm and feed forward layers, but you must
implement the multi-head attention on your own. The details of BERT training
can be found in [BERT](https://arxiv.org/abs/1810.04805), and those for the
transformer in [Transformer](https://arxiv.org/abs/1706.03762). You must
implement at least one transformer block, but you may play with the full
model too (12 layers!). You have to also implement the masked language
model.

For training  the BERT model, you will use the same large set of 524532 protein sequences
[uniprot-reviewed-lim_sequences.txt](http://www.cs.rpi.edu/~zaki/MLIB/data/uniprot-reviewed-lim_sequences.txt). This data is from the paper
[Learned
protein embeddings for machine learning](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6061698).
For prototyping the algorithm you can make use of the dataset of 1000 proteins
[small_uniprot.txt](http://www.cs.rpi.edu/~zaki/MLIB/data/small_uniprot.txt). 


One complication in BERT training is what tokenization to use. You can try
the basic character-level tokenization, i.e., each amino acid is a token,
i.e., kmer=1. On the training dataset, the max sequence length is 999, so
you should use a block size of 1000, with the first token being "CLS". 

If you are feeling ambitious, you an also try a kmer-3 tokenization, in
which case, each sequence can either be represented via a sliding window of
all kmers, or you can create three different sequences based on the starting
offset, and use non-overlapping kmers for pre-training.

# Evaluation

Once you have pre-trained the BERT model, you will evaluate it on the
protein family classification described in the paper [Continuous Distributed
Representation of Biological Sequences for Deep Proteomics and
Genomics](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0141287).
The dataset is available online at
<https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/JMFHTN>.
In particular, use the testing sequences in the file
"family_classification_sequences.csv". This file has 324018 sequences from
different protein families. The true class for these sequences is listed in
the "FamilyID" of the file "family_classification_metadata.tab". 

For each family, you should as positive class the sequences that have the
given family label, and then you should select an equal number of random
sequences from the whole dataset as negative class to train an MLP model for
binary classification. The MLP model will use the pre-trained BERT model to
learn a representation for each example sequence in the dataset.

Finally, you should also compare the benefit of BERT over ProtVec by using
the pre-trained word2vec based embeddings in the
"family_classification_protVec.csv"
file.  This file has the final embedding vector for each of the 324018
sequences, which can be used directly as input for a MLP model for
classification.


# Submission

Submit your jupyter notebooks (or python scripts) via submitty. 

The first notebook is for the BERT model.
The output of your code should the pre-trained BERT model for the
pre-training code.  

The second notebook is for the classification.
Next, you need to report the classification accuracy
using the pre-trained BERT model, as well as the prot2vec model on the
protein family classification dataset. Report the classification results
(specificity, sensitivity, and accuracy) for the first 20 families, 
as well as for the whole dataset, as shown in Table 2
in the paper.


You should acknowledge the source of any code you use from the web.
