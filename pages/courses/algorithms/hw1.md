<!--
.. title: CSCI2300 HW1
.. slug: algo_hw1
.. date: 2021-01-28 21:20:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

#**Due Date**: Feb 4, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW1

Answer the following questions. DPV refers to the algorithms book.

Q1. Consider the following pseudo-code:
```python
   def star(n):
      print('**')
      if n == 0: 
         return
      for i in range(n):
         star(i)
```
Let $T(n)$ be the number of times the function above prints a star when
called with input $n \ge 0$. Give an exact solution for $T(n)$ in terms
of $n$ only.

Q2. Give solutions for DPV Q0.1, parts g, i, l, p

Q3. Solve DPV Q0.3 a, b, c


# Lab1: Fibonacci Series


You will compare the two algorithms to generate the $n$-th Fibonacci
number. 

The first algorithm one should implement the recursive algorithm
**fib1** on Page 3 of the textbook, and the second one should implement
the iterative algorithm **fib2** on Page 4.

You should measure the time it takes for each of these versions (use for
example, the time module in python) to calculate the $n$-th Fibonacci
number for the following values of $n$: 1, 5, 10, 15, 20, 25, 30, 35, 40,
41, 42, 43. Create a table of all your results and plot (using for example,
the matplotlib library) the time taken to compute the Fibonacci numbers
using fib1 and fib2, with $n$ on the $x$-axis and time on the $y$-axis.

Next, verify that fib2 is indeed quadratic time. Run fib2 and record the
time on the following values of $n$: $2^{10}$, $2^{12}$, $2^{14}$, $2^{16}$,
$2^{18}$, $2^{19}$, $2^{20}$ Plot the time of fib2 versus $n$. If it takes more than
excessive time on your machine to compute the large values, then drop the last few values
above.

For this part you can appreciate the fact that Python has native arbitrary precision integer arithmetic. Otherwise, the values of $F(n)$ would easily exceed the 64 bit word size and cause overflow.

--- 

## Optional

Optionally, implement **fib3**, the repeated squaring matrix
power based algorithm we discussed in class. Compare its time versus
fib2.

---

## Grading

Use submitty to submit exactly one PDF and one .py script.

The PDF file must contain your solutions to the HW, and all of the
output from the python script.
You can hand write your solutions to the HW, take pics and convert to
PDF, or you can type up your answers.

The .py script must be implemented in Python3. 

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

