<!--
.. title: HW4
.. slug: algo_hw4
.. date: 2021-02-19 20:07:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# **Due Date**: Feb 25, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW4

Answer the following questions from the DPV book i) Q1.33, ii) Q1.39,
iii) Q1.40, and iv) Q1.42.


# Lab4: Generating Large Primes for Cryptography

**Random Prime:** Both RSA and Diffie-Hellman (DH) schemes require large prime numbers as
keys. Given $n$, the number of bits, write a program to generate a
random $n$-bit prime number, using the method described in sec 1.3.1 in
the book. Basically, you will generate a random $n$-bit (odd) number and test
whether it is a prime using the MillerRabin method you implemented in
the previous lab. If the number is not a prime, repeat, until you
generate a prime. Your method should print out the $n$-bit prime number,
and the number of trials it took to generate one prime (note that the
number of trials is different from the $k$ value you use in MillerRabin,
which you can set to $k=10$.)

**Random Relative Prime:** RSA scheme also requires a random public key
$e$ chosen so that it must be relatively prime to $M=(p-1) \cdot (q-1)$, where
$p$ and $q$ are two random $n$-bit primes. You need to write a function
to generate two random $n$-bit primes using the random prime algorithm
above, and then you should generate $e$, a random (odd) number in the range $2$ to
$M-1$ that is relative prime to $M$. Think about how you can efficiently
generate such an $e$ and write a function to generate it. 

**Verification of $e$:** When you generate $e$, you must verify that it
is relatively prime to $M$ by checking whether their GCD is indeed $1$
via the Euclid algorithm in Fig 1.5.

---

## Grading

Use submitty to submit exactly one PDF and one .py script. 
The .py script must be implemented in Python3. 
You can hand write your solutions to the HW, take
pics, or you can type up your answers and convert to PDF.

The PDF file must contain your solutions to the HW, and the output from
the python script. The script output the following information:

'p',  number of bits in p, number of trials it took to generate $p$,
value of $p$

'q', number of bits in q, number of trials it took to generate $q$,
value of $q$

'e', number of bits in e, number of trials it took to generate $e$,
value of $e$

'M', the GCD of $e$ and $M$, vaule of $M$

Try you code for $n=256, 512$. Try $n=1024$ if you can, or larger!

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

