<!--
.. title: HW2
.. slug: algo_hw2
.. date: 2021-02-05 21:20:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

#**Due Date**: Feb 11, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW2

Answer the following questions from the DPV book: 
Q1.9, Q1.11, Q1.12, Q1.18, Q1.31


# Lab2: Integer Multiplication


You will compare the two algorithms for integer multiplication. 

Implement the recursive algorithm in Fig 1.1 in the book. You can use bit shift
operations for multiplying and dividing by two, but can use regular
integer addition.
For this method, try not to use recursion, which can cause
"maximum number of recursive calls exceeded" error. Replace the
recursion by a for loop. 

Next, implement the divide-and-conquer algorithm in Fig 2.1. 
There is an error in the book for Fig 2.1; use the correction noted at:
http://cseweb.ucsd.edu/~dasgupta/book/errata.pdf
You can use
bit-wise operations for division and shifting, and also for
splitting the input numbers into 2 parts. Use regular
additions/subtractions on integers for the rest. It is best to leave
this as a recursive method, however see below for a trick to speed up
the code via memoization.

Compare the two methods in terms of running time on $d$ digit numbers
(in base 10), for $d=100, 1000, 10000$. Try larger values if you can (or
smaller values if the code takes too much time). List the average running time of
the two methods as a function of $d$ on random pairs of $d$ digit
numbers. You can generate random $d$ digit integers using the python
**random** library (e.g., using *randint*).

###Speeding up recursive code via memoization

In python, you can speedup recursive calls via memoization, using a
decorator. First define the memoize class follows:

```python
class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result
```

Next, just add the decorator before your recursive multiply function, as
follows:
```python
@memoize
def multiply(x, y):
    '''YOUR CODE HERE'''
```


---

## Grading

Use submitty to submit exactly one PDF and one .py script.

The PDF file must contain your solutions to the HW, and the output from
the python script. You can hand write your solutions to the HW, take
pics, or you can type up your answers and convert to PDF.

The .py script must be implemented in Python3. 

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

