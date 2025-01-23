# Activity Selection Problem (ASP)

## The problem
Given a sequence of **activities** $a_1, a_2, \ldots, a_n$, each defined by start and finish time $[s_i, f_i)$, find the largest number of mutually (pairwise) **compatible** activities. Two activities are said to be compatible if their intervals don't overlap.
$$
[s_i,f_i) \cup [s_j,f_j) = \emptyset
$$

## Input
The expected input is a file with one line for each activity. Each line contains start and finish values
