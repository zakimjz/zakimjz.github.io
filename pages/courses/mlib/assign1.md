<!--
.. title: CSCI4969-6969 Assign1
.. slug: mlib_assign1
.. date: 2022-01-25 13:23:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign1: Transcription Factor Binding via MLP

**Due Date**: Feb 1, before midnight (EST 11:59:59PM)

Transcription Factors (TFs) are proteins that bind to the DNA and help
regulate gene transcription. The TFs have to recognize some "motif" on the
DNA upstream from the gene, and DNA accessibility also plays a role.


## MLP model

In this assignment you'll modify write an MLP model the predict whether a
segments of the human chromosome 22 (Chr22) contain the binding sites for the JUND
TF.  You can modify the mlp notebook I shared with you to work on this
problem. You need to have at least one hidden layer. You have to compute a
weighted loss, and include accessibility information in your model, as
described below.

## Dataset
The data comprises 101 length segments from Chr22, with each position a
one-hot vector denoting one of the four bases (A, C, G, T). Thus, each
element of the input is 2d with size $101 \times 4$. Each such element has
a target label $0$ or $1$, indicating whether the TF binds to that segment or not. 
The data also includes a weight per input element, since there are only a
few binding sites (0.42%), so that you'd obtain an accuracy of 99.58% just
by predicting there are no binding sites. This means you have to use the
weights to discount the losses for label $0$ and enhance the losses for
label $1$ items. 
Finally, there is an array of values, one per input element, that also
indicates the chromosome accessibility for that segment.

The data is split into training, validation and testing sets. Each set
contains the following files:

* shard-0-X.joblib: the set of 101 x 4 input elements
* shard-0-y.joblib: the true labels: 0 or 1
* shard-0-w.joblib: weight per input element
* shard-0-a.joblib: accessibility value per input element

You can read these files by using **joblib.load** function, which will
populate a numpy array. For example

    X = joblib.load('shard-0-X.joblib')

will results in a numpy array X, which you can then convert to torch tensor,
and so on.

You can download the data as [TF_data.zip](https://www.cs.rpi.edu/~zaki/MLIB/data/TF_data.zip). Unzip it to create the train, valid, test directories.

## Details

First, you must write a dataset class that can load the data from the
different directories (train_dataset, valid_dataset, test_dataset).
Your class will have the following structure:

```python
from torch.utils.data import Dataset

class JUND_Dataset(Dataset):
    def __init__(self, data_dir):
        '''load X, y, w, a from data_dir'''        
        super(JUND_Dataset, self).__init__()
        
        # load X, y, w, a from given data_dir
        # convert them into torch tensors
        
    def __len__(self):
        '''return len of dataset'''
    
    def __getitem__(self, idx):
        '''return X, y, w, and a values at index idx'''
```

Once you have created the dataset class it can be passed to the DataLoader
class to get batches like we did for MNIST.


For the MLP model, the only difference is that the 2d input ($101\times 4$)
will have to be flattened into 404d vector. Then pass it to the hidden
layer, and apply relu activation. 
You can also try to add in a dropout layer at this point.
However, before feeding the output of the
hidden layer to the output layer, you must concatenate the accessibility
value. So if you are using hidden dimension of 128, then after concatenating
the accessibility value, it will become a 129d vector, which should be fed
to the final output layer of size 1, since we have a binary class/label.

The only other issue is the loss function. You should use
[binary_cross_entropy_with_logits](https://pytorch.org/docs/stable/generated/torch.nn.functional.binary_cross_entropy_with_logits.html) with weight set to the weights per
input element. Check out the documentation for details.

You need to train the model on the training data, and use the validation
data to select how many epochs you want to use and to choose the hidden
dimension. Use the weighted prediction accuracy as the evaluation metric.
That is, sum of the weights of the correct predictions divided by the total
weight across all the input elements. Finally, report the weighted accuracy
on the test data.

## What to submit

* Upload your jupyter notebook on [submitty](https://submitty.cs.rpi.edu/courses/s22/csci4969/gradeable/Assign1)

* The notebook must have output values for the final test accuracy.

