<!--
.. title: CSCI4969-6969 Capstone1 
.. slug: mlib_capstone1
.. date: 2022-04-10 14:21:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Capstone Project (Part I): AlphaFold2 -- Evoformer

**Due Date**: April 18th, before midnight

This is a group assignment, comprising part I of the final/capstone project for the course.
A group is made up of two persons.  Each student must detail their
role, as described below.

Send me via email your group information by monday
(11th April, before midnight). Talk to students during class or via email to
create groups.

The capstone project comprises implementing AlphaFold2 in two parts.
In part I, you will implement the Evoformer Trunk for the AlphaFold2 
protein structure method. The output from Evoformer will be used to predict
the distance matrix and the dihedral angles. In part II of the assignment
you will predict the full 3D coordinate structure for the $C_\alpha$ atoms.


# Data

For training, testing and validation we will make use of the 
[SidechainNet Data](https://github.com/jonathanking/sidechainnet), just like
we did in {{% doc %}} mlib_assign6 {{% /doc %}}.
The input to your method will be the training, validation and testing
files from SidechainNet. Use the one-hot sequence and PSSM features as
inputs. 


# Method

You will next implement the Evoformer trunk framework as described in the
[AlphaFold2 paper](https://www.nature.com/articles/s41586-021-03819-2) --
(Fig 3a).
In particular, the actual details of the various algorithms are available
in the 60-page [supplementary information PDF](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_MOESM1_ESM.pdf). You should consult this as you implement the method.

You will train on crops of length $256$. As done in Assign6, you will discretize the distances between
$2-22 A^\circ$ into 64 equal bins.
Then you can use cross-entropy loss on the
predicted probabilities and true distance symbols. 
The second head will directly predict the phi,psi angles per
position, discretized into 1296 bins.

You can monitor the predictions on the validation set for
hyperparameter tuning.

For testing you should report the loss, but also the accuracy of contact
prediction, broken into short, medium, long contacts as defined in Assign6.
Compare the precision results versus Alphafold1.

# Submission

Submit you notebook (or python script) via submitty, along with an output file (txt/pdf) that
summarizes the results of your method in terms of training and testing
accuracy values. If submitting a notebook, results can be part of the
notebook. You should report test loss, and contact map accuracy for CASP7
(if interested,  do CASP12 too). You also need to report the comparison between Alphafold2 vs. Alphafold1.

Your script/notebook must include a statement on the top about which group
member contributed to which portion of the code as well as ideas. Insert
comments in the code as well attributing different portions to different
members, or jointly done. Also, all code used from online sources must be
acknowledged.


You may want to use multiple GPUs to speed up your training, using the DCS
cluster.
