<!--
.. title: HW5
.. slug: algo_hw5
.. date: 2021-03-04 21:28:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# **Due Date**: Mar 11, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW5

Answer the following questions from the DPV book i) Q2.27-a,b,c, ii) Q2.32-a,b,c
iii) Show the output at each recursive step of the FFT algorithm in Fig
2.9, for the input $A = \[2,5,4,2,0,0,0,0\]$, and $\omega =
\frac{1}{\sqrt{2}}(1 + i)$.


# Lab5: Multiplying Large Polynomials

**Basic Algorithm:** Implement the basic quadratic time algorithm (Alg1 in Lecture11-PDF),
which is a simplified version of the description at the beginning of sec
2.6 in the book (before sec 2.6.1). 

Your code must take as input the "maximum degree" $d$ for the polynomial
$A$, and you must generate $d$ random coefficients in the range 1--10,
which will denote the coefficients $\[a_0, a_1, a_2, ..., a_{d-1}\]$, so
in fact the degree of the polynomial will be $d-1$. Likewise, generate
$d$ random coefficients for the polynomial $B$, to make up the
coefficients $\[b_0, b_1, b_2, ..., b_{d-1}\]$. 

You code must output the coefficients for the polynomial $C = A\cdot B$,
and also the time it takes.

**FFT-Based Algorithm:** 
Implement the FFT algorithm in Fig 2.9. Use the python **cmath** library
to deal with complex numbers. Now, use the following
pseudo-code to multiply the two polynomials $A$, $B$:
```python
n = power of 2 equal to or larger than 2d-1
angle = 2. * cmath.pi/n  # primitive root's angle
w = cmath.cos(angle) + cmath.sin(angle) * 1j #primitive n-th root of unity
A = [a_0, a_1, a_2, ...., a_{d-1}, 0, 0, ..., 0] #zero-pad to length n
B = [b_0, b_1, b_2, ...., b_{d-1}, 0, 0, ..., 0] #zero-pad to length n

# Evaluation
fft_A = FFT(A, w)
fft_B = FFT(B, w)

# Multiplication
fft_C = fft_A[i] * fft_B[i] # elementwise multiplication

# Interpolation
C = 1/n * FFT(fft_C, w**-1)
```
You code must output the coefficients for the polynomial $C = A\cdot B$,
and also the time it takes. When implementing the FFT, you'll find it
useful to check whether $\omega = 1$ by using the *cmath.isclose()*
function, since it may not be exactly 1.

**Bonus**: Implement the recursive divide-and-conquer algorithm, Alg2,
for polynomial multiplication that we discussed in Lecture11-PDF (using
the two-way split and using three subproblems).
Compare the output with the basic method for correctness, and report the
running time. Is it faster or slower than the basic method?

---

## Grading

Use submitty to submit exactly one PDF and one .py script. 
The PDF file must contain your solutions to the HW, and the output from
the python script. 

You must compare the output of the two algorithms to check for
correctness of your implementation of the FFT-based approach. You should
compare the running time for the two approaches for the following values
of $d=100, 1000, 10000$. You can also try larger values.

In the PDF include the output of the two algorithms for only $d=100$.
But you must include your running time for all the values of $d$.
Include the time for both the basic and FFT-based method, and the
divide-and-conquer method if you implement that.


---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

