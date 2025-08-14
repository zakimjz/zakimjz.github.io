<!--
.. title: CSCI4949-6969 Assign5
.. slug: mlib_assign5
.. date: 2022-03-16 19:00:31 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->


# Assign5: Graph Neural Networks

**Due Date**: Mar 25th, before midnight (EST 11:59:59PM)

In this assignment, you will use two different graph neural networks (GNNs)
for graph property prediction: Graph Convolution Network (GCN) and Message
Passing Neural Network (MPNN).

You can use the starter code from the [graph classification tutorial](https://docs.dgl.ai/en/0.6.x/tutorials/blitz/5_graph_classification.html#sphx-glr-tutorials-blitz-5-graph-classification-py) on the
DGL site, but modify it to a regression task.


For training  the GNNs, you will use the
[dgl.data.QM9EdgeDataset](https://docs.dgl.ai/en/0.6.x/api/python/dgl.data.html#graph-prediction-datasets)
that contains 130,831 molecules (there are several QM9 datasets, but use the
"Edge" one). This dataset has multiple regression
targets, but we will predict only the "mu" target values. That is, this is a
graph regression problem, where each of the molecules has one mu value, and
our goal is to predict that real value. 

On the DCS cluster, it will not download the dataset automatically so you
should download it from <https://data.dgl.ai/dataset/qm9_edge.npz> and put
it under "./data" directory, and then load the data via
**data = QM9EdgeDataset(label_keys=['mu'], raw_dir="./data")** to extract only the "mu"
values as labels.

Each graph has both node features (**g.ndata['attr']**)
and edge features (**g.edata['edge_attr']**). The GCN model makes use only of the node features,
whereas the MPNN uses both node and edge features. The two models will
differ in the type of GNN layers they will use. GCN uses the regular
**dgl.nn.GraphConv** layers, whereas MPNN uses the
[dgllife.model.gnn.mpnn.MPNNGNN](https://lifesci.dgl.ai/api/model.gnn.html#module-dgllife.model.gnn.mpnn) layer. However, once the GNN is done, in
the forward function of each model, you
should do graph node pooling via **dgl.readout_nodes** to extract the final
node features. These should then be fed to a two layer FFN comprised of two
linear layers with ReLU and dropout in between. The first FFN linear layer
will map the graph feature to a hidden MLP layer, and the second will map
the hidden MLP layer to a single neuron output for regression.

To evaluate and compare the two models, namely GCN and MPNN, you should use
the nn.L1Loss, which is also called the Mean Absolute Error. You should
divide the input graphs into 80% training, 10% validation, and 10% testing,
at random. You can use **torch.utils.data.random_split** for this. 

Use the validation set to select the number of GNN layers, size of the
hidden layers, learning rate, which pooling operator to use (max, min, mean, etc.), and so on, 
for both models. Finally, report the
test performance, and compare which model is better. For example, you can
use 5-fold cross-validation, or use 5 different splits to evaluate both
models and compare which has better average performance.

# Implementation

You will have to install the [DGL](https://docs.dgl.ai/en/0.6.x/index.html) 
graph library, and the [DGL-LifeSci](https://lifesci.dgl.ai/index.html)
companion library (for MPNN model). This is straightforward on the Amazon
StudioLab machine, but instructions on how to install these on the DCS
cluster will be shared on CampusWire.

# Submission

Submit your jupyter notebook with both models, and the comparison output, via submitty. 

You should acknowledge the source of any code you use from the web.
