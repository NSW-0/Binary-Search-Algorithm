# 🔍 Binary Search Algorithm

A Python implementation of the **Binary Search algorithm** using NumPy, with execution time tracking.

## Overview
Binary search is an efficient search algorithm that finds the position of a target value in a **sorted array**. Instead of checking every element, it repeatedly divides the search space in half — making it much faster than linear search.

## How it works
1. Start with the middle element of the sorted array
2. If the target equals the middle → return the index
3. If the target is smaller → search the left half
4. If the target is larger → search the right half
5. Repeat until found or return `None`

## Complexity
| | Complexity |
|--|--|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |
| Space | O(1) |

## Technologies
- Python 3.x
- NumPy

## Example Output
```
Searching for: 669
Found at index: 423
Time used to get the answer: 3.0000 μs
```
