<!--
.. title: HW8
.. slug: algo_hw8
.. date: 2021-03-25 23:26:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# **Due Date**: April 1, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW8

Answer the following questions from the DPV book i) Q5.2 ii) Q5.3, iii)
Q5.5, iv) Q5.18.


# Lab8: Kruskal's Algorithm and Union-Find Data Structure

Implement Kruskal's algorithm described in Fig 5.4. You must implement your own
union-find data structure for supporting the find and union operations as
described in section 5.1.4.  You should also implement the path compression for
find.  You cannot use any other python module or data structure other than
list, set or dict. 


You should run your code on the following three *undirected* graphs (zipped): 
[graphs.zip; right click and save as](http://www.cs.rpi.edu/~zaki/CS2300/data/graphs.zip). 
Each line in a file is a source-target-weight triple separated by
spaces. You should treat all nodes and weights as integers. 
Submit the output for source vertex 0.

Your code shoud print out the weight of the MST and the maximum rank of the
root node, and the maximum height of the root node in the final MST. Compare
the time, rank, and height with and without path compression.

---

## Grading

Use submitty to submit a PDF and one .py script.  

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

