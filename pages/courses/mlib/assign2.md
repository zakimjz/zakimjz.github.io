<!--
.. title: CSCI4969-6969 Assign2
.. slug: mlib_assign2
.. date: 2022-02-02 13:00:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign2: Transcription Factor Binding via LSTMs and CNNs

**Due Date**: Feb 9, before midnight (EST 11:59:59PM)

This assignment follows up on the assignment 1: {{% doc %}} mlib_assign1 {{% /doc %}}.
The input data and task remain the same, but you'll try out the LSTM and CNN
models.

## Deep Learning Models

In this assignment you'll write two models, namely an LSTM and a CNN, to the 
predict the binding sites for the JUND transcription factor protein.  
You'll compute the weighted loss, and include accessibility information in
your model, as before.

## Dataset
See description in assign 1.

## LSTM Details

For the LSTM model, use the encoder followed by a two layer MLP approach.
That is, pass the input sequence (batch) through the LSTM and use the last
hidden layer as the representation or embedding vector for the sequence. You
can choose the dimensionality of the hidden layer. Next, use this vector as
input to a two fully connected MLP layers -- the first connects the input
vector to the hidden
layer (again you can choose the size of the hidden layer), and the second
connects the hidden to the output neuron. Use dropout and relu as
appropriate.

Keep in mind that for the input to the [LSTM module](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html#torch.nn.LSTM) in pytorch use batch_first=True. This means that the batch dimension comes first, so the input is $(B \times 101 \times 4)$, which is how the input data is structured.
Make note of the output of the LSTM layer so that you store the last hidden
layer as the representation, to be used as input to the MLP layers.

Also, before feeding the output of the
hidden layer to the output layer, you must concatenate the accessibility
value. So if you are using hidden dimension of 128, then after concatenating
the accessibility value, it will become a 129d vector, which should be fed
to the final output layer of size 1, since we have a binary class/label.

You should use
[binary_cross_entropy_with_logits](https://pytorch.org/docs/stable/generated/torch.nn.functional.binary_cross_entropy_with_logits.html) with weight set to the weights per
input element.

You need to train the model on the training data, and use the validation
data to select how many epochs you want to use and to choose the hidden
dimension. Use the weighted prediction accuracy as the evaluation metric.
That is, sum of the weights of the correct predictions divided by the total
weight across all the input elements. Finally, report the weighted accuracy
on the test data.

## CNN Details

For the CNN model, you have to use the [1D convolution
module](https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html#torch.nn.Conv1d).
The in_channels will be 4, one per DNA base. You can decide what number of
out_channels and kernel size you want to use. Note the dimensions of the
input required for the 1D convolution -- $(B \times 4 \times L)$. That is
the input sequence has to be $4\times 101$ and not $101\times 4$ as in the
data. So you should use **torch.swapaxes** function to swap the last two
axes (not the batch axis) in the forward function.

After the Conv1d, you can apply a relu activation, do dropout, and then try
a maxpooling layer (1d). You can try more than one convolution layer too.

Finally, flatten out the last convolution layer and use as input to a two
layer MLP with the same setup as done for the LSTM above. 

## What to submit

* Upload your jupyter notebooks on [submitty](https://submitty.cs.rpi.edu/courses/s22/csci4969/gradeable/Assign2), one for the LSTM and another for the CNN.
* The notebook must have output values for the final test accuracy. You can
    also show the training/val losses and accuracy values.
* Do not submit the data file or directories. 
