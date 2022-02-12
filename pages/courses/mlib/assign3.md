<!--
.. title: CSCI4949-6969 Assign3
.. slug: mlib_assign3
.. date: 2022-02-11 019:00:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->


# Assign3: Protein Embeddings

**Due Date**: Feb 21, before midnight (EST 11:59:59PM)

In this assignment, you will implement the ProtVec embedding method
described in the paper
[Continuous Distributed Representation of Biological Sequences for Deep
Proteomics and Genomics](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0141287)

Your code should implement the negative sampling approach to train the
embeddings. For training  the model, you can first use a small set of 1000 proteins
[small_uniprot.txt](http://www.cs.rpi.edu/~zaki/MLIB/data/small_uniprot.txt). 
Once your model is finalized you should train
it on the large set of 524532 protein sequences
[uniprot-reviewed-lim_sequences.txt](http://www.cs.rpi.edu/~zaki/MLIB/data/uniprot-reviewed-lim_sequences.txt). This data is from the paper
[Learned
protein embeddings for machine learning](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6061698).

You should compare with the default values used in the paper, namely
embedding dimensionality $d=100$, window size $w=25$, and k-mer/n-gram size $k=3$, and the number of negative samples per positive example $q=5$. 

Here is the pseudo code for the overall method:

```python
   create the vocab, probability distribution, and word to index (and reverse mappings) for each k-mer in each sequence at each of the offsets: 0, 1, 2.

   write a function to return a batch of positive and negative pairs from all of the sequences/offsets.
   for the negative sampling use the cumsum approach to sample random words 

   define NN model:
       init function:
           define the two embeddings layers (T, C)

       forward function:
           input is a batch of target_words, and context_words 
           look up their embeddings
           compute the dot product between corresponding pairs
           output should be the probability of that pair being a positive pair (via sigmoid),
           or leave it as logits

   Next is the boilerplate code for training:
   net = model(parameters)
   send net to GPU
   loss_func = BCE loss (with logits)
   optimizer = optim.Adam

   for e in epochs
       for target_words, context_words, labels in batches
          send batch data to the GPU
          net.zero_grad
          preds = net (target_words, contex_words)
          loss = loss_func(preds, labels)
          loss.backward
          optimizer.step

      print total loss per epoch

   save embeddings
   visualize embeddings via t-SNE
```

# Submission

Submit your jupyter notebook (or python script) via submitty. 

The output of your code should be a file that contain the embedding of
each word. The first line should have only two values:

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

After learning the representations, we will use the trained
vectors for some downstream tasks in future assignments.
For this assignment you should visualize your embeddings using [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html).

BTW, you should acknowledge the source of any code you use from the web.
