<!--
.. title: CSCI4390-6390 Assign3
.. slug: dm_assign3
.. date: 2025-10-02 12:00:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# Assign3: Pattern Mining

**Due Date**: Oct 9, before midnight (11:59:59PM)

---

# Closed Itemset Mining

Implement the CHARM closed itemset mining algorithm (Algorithm 9.2 on page 251 in the book). 
For example, given the dataset:

``` text
A B D E
B C E
A B D E
A B C E
A B C D E
B C D
```

You can assume that each line has a transaction -- a set of items, separated
by spaces. For minimum support of 3, the set of closed itemsets should be printed out
in the format:

``` text
A,B,D,E - 3
A,B,E - 4
B,D - 4
B,C,E - 3
B,C - 4
B,E - 5
B - 6
Number of closed itemsets: 7
```

Show the frequent closed itemsets on the
[Reuters Newswire Data](http://www.cs.rpi.edu/~zaki/DMCOURSE/data/ModApte_words.txt) dataset, using
minimum support of 50. The dataset is a list of words, one per line, with
each line representing a transaction. Here the words are the items.

Next plot the running time as a function of minimum support
from 50 down to 15 or 10 (or the smallest value more than 10 you can run), decreasing the minimum support by 5 each time. Also plot the number of closed frequent itemsets as a function of the same minimum support values.

---

## What to submit

* Submit your notebook named as **assign3.ipynb** via submitty.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding must be
your own. Any AI tool use must be declared. Any students caught violating the
academic honesty principle (e.g., code similarity, or failure to disclose AI
tools) will get an automatic F grade on the course and will be referred to the
dean of students for disciplinary action.
