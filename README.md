🔍 Binary Search Algorithm
A Python implementation of the Binary Search algorithm using NumPy, with execution time tracking.
Overview
Binary search is an efficient search algorithm that finds the position of a target value in a sorted array. Instead of checking every element, it repeatedly divides the search space in half — making it much faster than linear search.
How it works

Start with the middle element of the sorted array
If the target equals the middle → return the index
If the target is smaller → search the left half
If the target is larger → search the right half
Repeat until found or return None

Complexity
ComplexityBest CaseO(1)Average CaseO(log n)Worst CaseO(log n)SpaceO(1)
Technologies

Python 3.x
NumPy

Example Output
Searching for: 669
Found at index: 423
Time used to get the answer: 3.0000 μs
