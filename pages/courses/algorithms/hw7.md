<!--
.. title: HW7
.. slug: algo_hw7
.. date: 2021-03-19 14:26:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# **Due Date**: Mar 25, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW7

Answer the following questions from the DPV book i) Q4.4 ii) Q4.5, iii)
Q4.9 (consider the cases both with and without negative cycles), iv)
Q4.12.


# Lab7: Dijkstra's Algorithm and Binary Heap Priority Queue

Implement Dijkstra's algorithm described in Fig 4.8. You must implement
your own binary heap priority queue for supporting the deletemin and
decreasekey operations required in the algorithm. You cannot use any
other python module or data structure other than array, list, set or
dict. Note that you must use the **prev** values to peint the actual shortest
paths along with the length.

Before you implement the binary heap version of the priority queue, you
can test the correctness of the Dijkstra implementation using the basic
array based priority queue. 

To next implement the binary heap, you can
use an array-based implementation of the binary tree (indexed from
0 as usual), there the root is at position $0$ always, and for any
position $i$, its parent node is at position $(i-1)//2$, and its
children are at positions $2i+1$ (left) and $2i+2$ (right). See Figure
4.16 (and question 4.16) for more details on this array-based
implementation of the priority queue. However, you can also implement a
non-array based implementation of binary heap if you choose (e.g., via
dict, etc., which will be less efficient than the array based
implementation).

You should run your code on the following graph: 
[graph1](http://www.cs.rpi.edu/~zaki/CS2300/data/dijk_graph20.txt) 
Each line in the file is a source-target-weight triple separated by
spaces. You should treat all nodes and weights as integers. 
Submit the output for source vertex 0.

Given a source node $s$, your code should print out the length of the
shortest path from $s$ to each node $u$ and (one of) the actual shortest
paths from $s$ to $u$. So given the graph:

    0 1 4
    0 2 2
    1 2 3
    1 3 2
    1 4 3
    2 1 1
    2 2 4
    2 3 5
    4 3 1

For source node $0$, the output should be as follows:

    0 0 [0]
    1 3 [0, 2, 1]
    2 2 [0, 2]
    3 5 [0, 2, 1, 3]
    4 6 [0, 2, 1, 4]

Which shows the node, length of shortest path, and actual shortest path per line.

---

## Grading

Use submitty to submit a PDF and txt and one .py script. 
The .py file should take the file name and source vertex id from the
command line.

The PDF file must contain your solutions to the HW, and the output from
the python script can be submitted in the txt file. Show
your output for the source vertex 0. 

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

