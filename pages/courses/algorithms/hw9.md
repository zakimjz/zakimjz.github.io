<!--
.. title: HW9
.. slug: algo_hw9
.. date: 2021-04-16 13:26:01 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. has_math: True
.. type: text
-->

# **Due Date**: April 22, before midnight (11:59:59PM)

This assignment comprises both written questions and
implementation-based lab.

---

# HW9

Answer the following questions from the DPV book: i) Q6.1, ii) Q6.4, iii)
Q6.11, iv) Q6.19.


# Lab9: Edit Distance

Implement the edit distance algorithm described in Sec 6.3. Your code should
compute the i) edit distance, and ii) a corresponding optimal alignment (via a
"prev" array that keeps track of the minimum choice at each cell). 
You can use the numpy library if you need, but the code to implement edit
distance must be your own.

You can test you code on the simple example from the book chapter. Given
strings EXPONENTIAL and POLYNOMIAL, your output should be:

    edit distance = 6
    alignment:
    EXPONEN-TIAL
    --POLYNOMIAL

Note that is possible to have another alignment, but the distance remains 6.

As another test case, try the following two DNA strings:

    CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG
    CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA

The edit distance in this case is 41. When printing a long string, make sure
that no more than 80 characters are printed at one time. For the two strings
above your output should look like:

    edit distance: 41
    alignment:
    CATAAGC-TTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGT
    CGT-AGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCA--AGCTAT-TTTGTTGAGGGTGC-TGCTCAGGC

    TGAACAG-
    TGGATGGA


Finally, submit your output on the following two files. The first one 
[cox1-protein.fasta](http://www.cs.rpi.edu/~zaki/CS2300/data/cox1-protein.fasta)
contains the COX1 (cytochrome c oxidase subunit I) gene's protein sequence for Humans and Yeast, and the second
one
[cox1-dna.fasta](http://www.cs.rpi.edu/~zaki/CS2300/data/cox1-dna.fasta)
contains the COX1 gene's DNA sequence for Humans and Worms. These "fasta"
files have two sequences in each file. Each sequence begins with a header
string on one line beginning with the character ">". The lines that follow
should all be concatenated into one string, until the next ">" is seen or
end of file is encountered. For example, if a sample file is 
    
    >this is seq1
    ACGT
    AC
    >this is seq2
    TAGGGGT
    ACTT

Then the first sequence is ACGTAC, and the second is TAGGGGTACTT

# Bonus 

In addition to the edit distance, compute and print the total number of
distinct alignments that are optimal. 

---

## Grading

Use submitty to submit a PDF with the output and one .py script. The output
on the cox1-protein and cox1-dna sequences should be submitted.

---

## Policy on Academic Honesty

You are free to discuss how to tackle the assignment, but all coding
must be your own. Please do not copy or modify code from anyone else,
including code on the web. Any students caught violating the academic
honesty principle will get an automatic F grade on the course and will
be referred to the dean of students for disciplinary action.

