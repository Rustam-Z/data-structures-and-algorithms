# Computer Algorithms

By Rustam Zokirov • September 19, 2021

## Contents
- [Introduction](#Introduction)
- [Data Abstraction](#Data-Abstraction)
- [Asymptotic Notations](#Asymptotic-Notations)
    - [Practice](#Practice)

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

