<!--
.. title: HW3
.. slug: algo_hw3
.. date: 2021-02-12 09:50:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# **Due Date**: Feb 18, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW3

Answer the following questions from the DPV book i) Q1.17, ii) Q1.19,
iii) Q 1.23, and iv) given that $x^{86} \equiv 6 \mod 29$, find $x$.


# Lab3: Primality Testing


You will compare the two randomized primality testing algorithms -- the
basic one in Fig 1.8, and the Miller-Rabin algorithm.
Both these methods require modular exponentiation, so you **must** also
implement the *modexp* algorithm in Fig 1.4.

Implement the randomized primality algorithm in Fig 1.8 in the book. 

Next, implement the Miller-Rabin primality test, which is informally
described in the gray box just before sec 1.3.1 in the book, and whose pseudo-code is
given below:

```python
MillerRabin(N, K):
    Pick positive intgers a1, a2, ..., aK < N at random
    Find u, t, such that N-1 = u * 2^t
    for i = 1, 2, ..., K
        z = ai^u mod N
        if z = 1 mod N 
            mark that ai passes the test
        else
            # repeated squaring, keep track of previous value of z,
            # find first occurrence of 1 if any
            for j = 1, 2, .., t
                compute z^2 mod N
                # ai passes the test iff squared value is 1 and prev value is N-1
                # else ai fails the test
            #ai also fails the test if no 1 is encountered above
    if all a1, a2, ..., aK pass the test
        return yes
    else
        return no
```

###Carmichael numbers

Test your code on the following Carmichael numbers:
```python
Carmichael = [
    561,
    6601,
    67902031,
    8956911601,
    438253965870337,
    999987515379253441,
    1745094470986967126132341,
    844154128953833755776750022681,
    365376903642671522645639268043801,
    1334733877147062382486934807105197899496002201113849920496510541601,
    2887148238050771212671429597130393991977609459279722700926516024197432303799152733116328983144639225941977803110929349655578418949441740933805615113979999421542416933972905423711002751042080134966731755152859226962916775325475044445856101949404200039904432116776619949629539250452698719329070373564032273701278453899126120309244841494728976885406024976768122077071687938121709811322297802059565867
]
```

Except for 561, these numbers are difficult for the basic primality
testing code, but will be marked as non-prime by MillerRabin for
reasonable values of $K$. On the contrary, some numbers like
999987515379253441 are still incorrectly marked as prime by the basic
test, even for $K=1000$!

Your script should test all of the numbers above, except for the last
one, which will cause "maximum recursion exceed" error for
the recursive version of *modexp*. Your script should print whether the
given Carmichael number is prime or not, and it must also print 
the fraction of choices of $a_i$ (out of the $K$)
that pass Fermat's test for each method. Try different value of $K$,
such as $K=10, 20, 50, 100, 1000$.

**Bonus:** To run the last number in the list above you'll have to
implement a non-recursive version of *modexp*, which will earn bonus
points.

---

## Grading

Use submitty to submit exactly one PDF and one .py script. 
The .py script must be implemented in Python3. 
You can hand write your solutions to the HW, take
pics, or you can type up your answers and convert to PDF.

The PDF file must contain your solutions to the HW, and the output from
the python script. The script output should be whether each Carmichael
number is prime or not, and the fraction of choices of $a_i$ that pass
the test (even if the number is eventually identified as non-prime).

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

