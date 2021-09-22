# Computer Algorithms

By Rustam Zokirov • September 19, 2021

## Contents
- [Introduction](#introduction)
- [Data Abstraction](#data-abstraction)
- [Asymptotic Notations](#asymptotic-notations)
    - [Practice](#practice)

## Introduction
- A **computer algorithm** is 
    - a detailed step-by-step method
    - for solving a problem
    - by using a computer
- **Properties**
    - Finiteness (should be terminated)
    - Unambiguous (must be clear)
    - Definiteness of sequence (by order)
    - Input /Output defined
    - Feasibility (must be possible to implement)
- **Problem solving strategies**
    - Divide & Conquer
    - Greedy Method (making the most possible solution)
    - Branch & Bound 
    - Backtracking
    - Dynamic Programming
    - Brute Force (checking all possibilities)
    - Randomized  


## Data Abstraction
- Abstact Data Type - each ADT has set of *values* and *operations*
- Encapsulation: hide implementation details
    - A data structure is the physical implementation of an ADT
- **Data items have both *logical* and *physical* form**
    - Logical form: definition of the data item within an ADT. 
    - Physical form: implementation of the data item within a data structure
- Abstract Data Types
    - Lists, Trees
    - Stacks, Queues
    - Priority Queue, Union-Find
    - Dictionary
- **ADT Specification**
    - Specification formally define the behavior of a software system or a module (*in terms of Inputs and Outputs*)
    - A specification of an operation consists of:
        - Calling prototype
        - Preconditions
        - Postconditions
    - The calling prototype includes 
        - name of the operation
        - parameters and their types
        - return value and its types
    - The preconditions are statements 
        - assumed to be true when the operation is called
    - The postconditions are statements 
        - assumed to be true when the operation returns.


## Asymptotic Notations
- Running time of an algorithm as a function of input size **n for large n**
- O (worst, upper bound), Ω (best, lower bound), Θ (average, tight bound)
- “Running time is O(f(n))” -> Worst case is O(f(n))
- “Running time is Ω(f(n))” -> Best case is Ω(f(n))

### Practice
```
Big O
__________________________________________________________________
a. f(n) = 5n^3 + n^2 + 6n + 2
5n^3 + n^2 + 6n + 2 <= 5n^3 + n^2 + 6n + n      n >= 2
                    <= 5n^3 + n^2 + 7n  
                    <= 5n^3 + n^2 + n^2         n^2 >= 7n, n >= 7
                    <= 5n^3 + 2n^2 
                    <= 5n^3 + n^3               n^3 >= 2n^2, n >= 2
                    <= 6n^3
                    = O(n^3)
                    [c=6, n>=7]

b. f(n) = 6n^2 + 3n + 2^n
2^n + 6n^2 + 3n <= 2^n + 6n^2 + n^2             n^2 >= 6n, n >= 6
                <= 2^n + 7n^2
                <= 2^n + 2^n                    2^n >= n^2, n >= 4 
                <= 2*2^n 
                = O(2^n)
                [c=2, n=6]

Big Ω
__________________________________________________________________
a. 5n^3 + n^2 + 3n + 2
5n^3+ n^2 + 3n + 2 >= 5n^3      n0 >= 1
                    = Ω(n^3)
                    [c=5, n0>=1]

b. 4*2^n + 3n
4*2^n + 3n >= 4*2^n     n0 >= 1
            = Ω(2^n)
            [c=4, n0 >= 1]

Big Θ (average)
__________________________________________________________________
a. f(n) = 27*n^2 + 16n
27*n^2+16n <= 27*n^2+n^2    n^2 >= 16n, n >= 16
           <= 28*n^2
            = O(n^2)
            [c1=28, n0=16]

27*n^2+16n >= 27*n^2        n0 >= 1
            = Ω(n^2)
            [c2=27, n0>=1]

Overall, [c1=28, c2=27, n0>=16]

b. f(n) = 3*2^n + 4n^2 + 5n + 2
3*2^n+4n^2+5n+2 <= 3*2^n+4n^2+5n+n      n >= 2
                <= 3*2^n+4n^2+6n
                <= 3*2^n+4n^2+n^2       n^2 >= 6n, n >= 6
                <= 3*2^n+5n^2
                <= 3*2^n+2^n            2^n >= n^2, n >= 4
                <= 4*2^n
                = O(2^n)
                [c1=4, n0>=6]

3*2^n + 4n^2 + 5n + 2 >= 3*2^n      n0 >= 1
                      = Ω(2^n)
                      [c2=3, n0>=1]

Overall, [c1=4, c2=3, n0>=6]

Extra 
__________________________________________________________________
f(n) = 5n^3 + 2 and g(n)= n^2

a. g(n) = o f(n)
n^2 = o(5n^3 + 2)
n^2 = o(n^3) TRUE

b. f(n) = O g(n)
5n^3 + 2 = O(n^2) FALSE, it should be at least O(n^3), O(n^4)
```
