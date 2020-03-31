.. title: CSCI4969-6969 Machine Learning in Bioinformatics 
.. slug: mlib
.. date: 2020-03-30 09:21:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

This course focuses on machine learning algorithms for analyzing
biological data. The course will introduce the main topics in this area,
such as analysis of genome sequences, protein structures, gene networks,
and so on. We will cover some of the traditional algorithms for these
tasks, but the main focus is on the role of deep learning and data
mining in computational biology and bioinformatics.

**Class Hours**: 10-11:50AM TF, Low 3039. *Office Hours*: 12-1PM TF

**Syllabus**: :doc:`mlib_syllabus`

**Campuswire**: https://campuswire.com/c/GD5DDE12E/

**Submitty**: https://submitty.cs.rpi.edu/s20/csci4969


Assignments
-----------

**Assign1**: :doc:`mlib_assign1`

**Assign2**: :doc:`mlib_assign2`

**Assign3**: :doc:`mlib_assign3`


Class schedule
--------------

+-----------------+---------------------------------+----------+------------------------------------------------------------------+
| Date            | Topic                           | Readings | Lecture Notes                                                    |
+=================+=================================+==========+==================================================================+
|  Jan 14         |  Introduction I                 | R1       | `Intro <http://www.cs.rpi.edu/~zaki/MLIB/intro.ppt>`_            |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Jan 17         |  Introduction II                | R1,P1    | `lecture1 <http://www.cs.rpi.edu/~zaki/MLIB/lecture1.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Jan 21         |  Linear and Logistic Regression | R2,R3,P2 | `lecture2 <http://www.cs.rpi.edu/~zaki/MLIB/lecture2.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Jan 24         |  Word Embeddings                | P2       | `lecture3 <http://www.cs.rpi.edu/~zaki/MLIB/lecture3.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Jan 28         | Word2Vec                        | R4       | `lecture4 <http://www.cs.rpi.edu/~zaki/MLIB/lecture3.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Jan 31         | Neural Networks I               | R4       | `lecture5 <http://www.cs.rpi.edu/~zaki/MLIB/lecture5.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 4          | MLPs                            | R4       | `lecture6 <http://www.cs.rpi.edu/~zaki/MLIB/lecture6.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 7          | RNNs and LSTMs                  | R5       | `lecture7 <http://www.cs.rpi.edu/~zaki/MLIB/lecture7.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 11         | Seq2Seq Models                  |          | `lecture8 <http://www.cs.rpi.edu/~zaki/MLIB/lecture8.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 14         | Transformer and Attention       | P4,P5    | `lecture9 <http://www.cs.rpi.edu/~zaki/MLIB/lecture9.pdf>`_      |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 18         | NO CLASS (Mon Schedule)         |          |                                                                  |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 21         | BERT                            | P3,P5    | `lecture10 <http://www.cs.rpi.edu/~zaki/MLIB/lecture10.pdf>`_    |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 25         | CNNs                            | R5       | `lecture11 <http://www.cs.rpi.edu/~zaki/MLIB/lecture11.pdf>`_    |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Feb 28         | Seondary Structure Prediction   | P6       | `lecture12 <http://www.cs.rpi.edu/~zaki/MLIB/lecture12.pdf>`_    |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Mar 3          | Secondary Structure Prediction  | P6       | `lecture13 <http://www.cs.rpi.edu/~zaki/MLIB/lecture13.pdf>`_    |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Mar 6          | Embeddings with Structure       | P7       | `lecture14 <http://www.cs.rpi.edu/~zaki/MLIB/lecture14.pdf>`_    |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Mar 10--Mar 20 | NO CLASS (Spring Break)         |          |                                                                  |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Mar 24         | 3D Strcture Prediction          | P8       | `lecture15 <http://www.cs.rpi.edu/~zaki/MLIB/lecture15.pdf>`_,   |
|                 |                                 |          | `video-mar24 <http://www.cs.rpi.edu/~zaki/MLIB/mlib-mar24.mkv>`_ |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Mar 27         | 3D Structure Prediction         | P8       | `lecture16 <http://www.cs.rpi.edu/~zaki/MLIB/lecture16.pdf>`_,   |
|                 |                                 |          | `video-mar27 <http://www.cs.rpi.edu/~zaki/MLIB/mlib-mar24.mkv>`_ |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+
|  Mar 31         | 3D Structure Prediction         | P9       | `lecture17 <http://www.cs.rpi.edu/~zaki/MLIB/lecture17.pdf>`_,   |
|                 |                                 |          | `video-mar31 <http://www.cs.rpi.edu/~zaki/MLIB/mlib-mar31.mkv>`_ |
+-----------------+---------------------------------+----------+------------------------------------------------------------------+


Papers
------

See https://github.com/hussius/deeplearning-biology for a list of papers on deep learning in computational biology.

The papers we will read appear below. They are referred to as Px in the
course schedule above.

1. P1: Deep learning: new computational modelling techniques for genomics, https://www-nature-com.libproxy.rpi.edu/articles/s41576-019-0122-6
2. P2: Continuous Distributed Representation of Biological Sequences for Deep Proteomics and Genomics, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0141287
3. P3: Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences, http://biorxiv.org/lookup/doi/10.1101/622803
4. P4: Attention is all you need, https://arxiv.org/abs/1706.03762
5. P5: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, https://arxiv.org/abs/1810.04805
6. P6: DeepPrime2Sec: Deep Learning for Protein Secondary Structure Prediction from the Primary Sequences, https://www.biorxiv.org/content/10.1101/705426v1 
7. P7: Learning protein sequence embeddings using information from structure, https://arxiv.org/abs/1902.08661 
8. P8: End-to-end differentiable learning of protein structure, https://www.biorxiv.org/content/10.1101/265231v2
9. P9: Improved protein structure prediction using potentials from deep learning,  https://www.nature.com/articles/s41586-019-1923-7, https://deepmind.com/research/open-source/alphafold_casp13


Readings
--------

These readings are referenced as Rx in the course schedule above.

* R1: Cells and Genomes, http://www.cs.rpi.edu/~zaki/MLIB/protected, (look at AJLMRRW-chap1.pdf)
* R2: Linear Regression, http://www.cs.rpi.edu/~zaki/MLIB/linear-regression.pdf
* R3: Logistic Regression, http://www.cs.rpi.edu/~zaki/MLIB/logistic-regression.pdf
* R4: Neural Networks, http://www.cs.rpi.edu/~zaki/MLIB/neural-networks.pdf
* R5: Deep Learning (RNNs, LSTMs, CNNs), http://www.cs.rpi.edu/~zaki/MLIB/deep-learning.pdf

