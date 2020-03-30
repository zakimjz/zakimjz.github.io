.. title: CSCI4949-6969 Assign1
.. slug: mlib_assign1
.. date: 2020-03-30 09:21:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text



Assign1: ProtVec 
----------------

**Due Date**: Feb 4th, before midnight

In this assignment, you will implement the ProtVec embedding method
described in
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0141287
(Continuous Distributed Representation of Biological Sequences for Deep
Proteomics and Genomics).

You will use http://www.pytorch.org (pytorch) for the implementation, and
your code should implement the negative sampling approach to train the
embeddings.

For training  the model, you can first use a small set of 1000 proteins
http://www.cs.rpi.edu/~zaki/MLIB/assignments/small_uniprot.txt. Once your model is finalized you should train
it on the large set of 524532 protein sequences
http://www.cs.rpi.edu/~zaki/MLIB/assignments/uniprot-reviewed-lim_sequences.txt. This data is from the paper
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6061698/ (Learned
protein embeddings for machine learning)

You will be asked to compare the embeddings for different values of the
dimensionality $d$, different context size $w$, and different n-gram
sizes $n$. For example $d=50, 100, 300$, $w=5, 7, 25$, and
$n=1,2,3,4,5$.

You should compare with the default values used in the paper, namely
$d=100$, $w=25$, and $n=3$. In your implementation these should be
variables that take their values from the command line (see below; you
should also make the number of negative samples a parameter).

Here is the pseudo code for the overall structure of the script:

.. code-block:: python
   :number-lines:

   create the vocab, probability distribution, and word to index (and reverse mappings) for each ngram in each sequence at each of the offsets from 0 to ngram-1

   write a function to return a batch of positive and negative pairs from all of the sequences/offsets.
   for the negative sampling use the cumsum approach described in class 

   define NN model:
       init function:
           define the two embeddings layers (U,V)

       forward function:
           input is a batch of center_words, and context_words 
           look up their embeddings
           compute the dot product between corresponding pairs
           output should be the probability of that pair being a positive pair (via sigmoid)

   Next is the boilerplate code for training:
   net = model(parameters)
   send net to GPU
   loss_func = BCEloss
   optimizer = optim.SGD or optim.Adam

   for e in epochs
       for center_words, context_words, labels in batches
          convert center_words, context_words, labels to tensors
          send all three to the GPU
          net.zero_grad
          preds = net (center_words, contex_words)
          loss = loss_func(preds, labels)
          loss.backward
          optimizer.step

      print total loss per epoch

   save embeddings in required format


Submission
~~~~~~~~~~

Submit your code via submitty. Name your python script:
**assign1.py**.

Your script will be run as follows:

assign1.py FILENAME EMBED_DIM CONTEXT_SZ NGRAM_SIZE NEG_SAMPLES

Here FILENAME is the name of the sequence file, EMBED_DIM the
dimensionality to use for the embedding vectors, CONTEXT_SZ is the size
of the context to consider, NGRAM_SZ is the size of the ngrams, and
NEG_SAMPLES is the number of negative samples to consider for each
positive pair.

Note that CONTEXT_SZ will always be an odd number greater than 1, so
CONTEXT_SZ=3 means that you look at the center word and plus/minus one
word, CONTEXT_SZ=25 means center word plus/minus 12 words, and so on.

The output of your code should be a file that contain the embbedding of
each work. The first line should have only two values:

V d

where V is the Vocab size, and d the EMBED_DIM

Next, each line should contain:

WORD EMBEDDING_VECTOR

where WORD is a word from your vocab (not the index), and its embedding
vector. For example, if there are only two words in your vocab (say AA
and BB), and you are doing 3-dim embeddings, then the output file will
be:

2 3

AA -1 -0.3 5

BB 2 0.5 -1

After learning the representations, you will be asked to use the trained
vectors for a downstream task such as sequence classification or
secondary structure prediction. *The details of the tasks will be posted
for Assign2*

Note that you are allowed to use/modify existing implementations of
word2vec in pytorch on the web, but you should understand what is being
done, so that you are able to code more complex models later. You should
acknowledge the source of any code you use.
