<!--
.. title: CSCI4969-6969 Capstone2 
.. slug: mlib_capstone2
.. date: 2022-04-10 14:21:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Capstone Project (Part II): AlphaFold2 -- 3D Structure Prediction

**Due Date**: April 25th, before midnight

This is a group assignment, comprising part II of the final/capstone project for the course.
You'll be in the same group as for part I. Each student must detail their
role, as described below.

In this part (II) of the assignment you will predict the full 3D
coordinates for the protein backbone $C_\alpha$ atoms. It is thus a
simplified version of Alphafold2.


# Data

For training, testing and validation we will make use of the 
[SidechainNet Data](https://github.com/jonathanking/sidechainnet), just like
we did in {{% doc %}} mlib_assign6 {{% /doc %}}.
The input to your method will be the training, validation and testing
files from SidechainNet. Use the one-hot sequence and PSSM features as
inputs, and the coordinates of the $C_\alpha$ atoms are the target output.


# Method

You will next implement the Structure Prediction module (Fig 3d) comprising the 
Invariant Point Attention (IPA) and Backbone Update
methods described in the
[AlphaFold2 paper](https://www.nature.com/articles/s41586-021-03819-2), and
in the [supplementary information PDF](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_MOESM1_ESM.pdf).

You will combine the structure prediction module with the Evoformer truck
from part I for an end-to-end 3D coordinate prediction method. The loss to
be used is the FAPE loss (Frame Aligned Point Error) combined with the
torsion angle loss.

For testing you should report the loss, but also the accuracy of the 3D
$C_\alpha$ backbone prediction, i.e., the score for the true vs predicted 3D structure.

# Submission

Submit you notebook (or python script) via submitty, along with an output file (txt/pdf) that
summarizes the results of your method in terms of training and testing
values. If submitting a notebook, results can be part of the
notebook. You should report test loss, and 3D score for CASP7, but ideally
for CASP12.

Your script/notebook must include a statement on the top about which group
member contributed to which portion of the code as well as ideas. Insert
comments in the code as well attributing different portions to different
members, or jointly done. Also, all code used from online sources must be
acknowledged.

You may want to use multiple GPUs to speed up your training, using the DCS
cluster.
