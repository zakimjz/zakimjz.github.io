<!--
.. title: HW6
.. slug: algo_hw6
.. date: 2021-03-12 21:28:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# **Due Date**: Mar 18, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW6

Answer the following questions from the DPV book i) Q3.4 ii) Q3.6, iii)
Q3.9., iv) Q3.11.


# Lab6: Strongly Connected Components

Implement the strongly connected components algorithm described on page
94 in the book. You'll have to increase the recursion limit to make this
work for the graphs below. You are only allowed to use basic python data
structures (e.g., dict, set, list), and should *not* use any graph
packages (e.g., networkx, igraph, etc.).

You should run your code on these two graphs: 
[graph1](http://www.cs.rpi.edu/~zaki/CS2300/data/scc_graph100.txt) 
and 
[graph2](http://www.cs.rpi.edu/~zaki/CS2300/data/scc_graph1000.txt) 
These files list out all the directed edges, one per line.

Your code must print the SCCs in decreasing order of length. Also, for
two SCCs with the same number of nodes, the one with the lowest id
vertex should come first. These SCCs must therefore be numbered from 0
to M, where M is the number of SCCs. Print them out in the following
format:

    SCC_ID LEN SET_OF_NODES_IN_SCC(in sorted order)

Once you have printed the SCCs, you must also print the edges that
comprise the DAG structure over the SCCs. The edges must be printed in
sorted order (in increasing order). The edges will use the SCC_IDs from
above to denote the DAG nodes.

**Bonus**: Implement a non-recursive version of dfs method to handle large graphs, and test it on
[graph3](http://www.cs.rpi.edu/~zaki/CS2300/data/scc_graph10000.txt) 

Submit the output on the bonus graph as for the above two graphs.

---

## Grading

Use submitty to submit exactly one PDF and one .py script. 
The PDF file must contain your solutions to the HW, and the output from
the python script. 

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

