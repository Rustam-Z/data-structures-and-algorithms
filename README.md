# Data Structures
Lecture notes on Data Structures `SOC-2010`

By Rustam Zokirov

## Content:
- [Introduction to Data Strutures](#introduction-to-data-strutures)
    - [Introduction](#introduction)
    - [Abstract Data Type](#abstract-data-type)
    - [Asymptotic Notations (O, Ω, Θ)](#asymptotic-notations)

- [Searching techniques](#searching-techniques)
    - [Linear Search](#linear-search)
    - [Binary Search](#binary-search)

- [Sorting techniques](#sorting-techniques)

- [Linked list](#linked-list)
    - [Insertion at beginning](#insertion-at-beginning-in-linked-list)
    - [Insertion at the end](#insertion-at-the-end-in-linked-list)
    - [Insertion at particular position](#insertion-at-particular-position)
    - [Deleting the first Node](#deleting-the-first-node-from-a-linked-list)
    - [Deleting the last Node](#deleting-the-last-node-from-a-linked-list)
    - [Deleting the specific node in a Linked List](#deleting-the-specific-node-in-a-linked-list)

- [Circular linked list](#circular-linked-list)
    - [Insertion at beginning](#Insertion-at-Beginning-in-Circular-Linked-List)
    - [Insertion at the end](#Insertion-at-the-End-in-Circular-Linked-List)
    - [Insertion at particular position](#Insertion-at-Particular-Position-in-Circular-Linked-List)
    - [Deletion a node](#Deletion-a-node-in-Circular-Linked-List)

- [Doubly linked list](#doubly-linked-list)

- [Stacks](#stacks)
    - [Array representation of stacks](#Array-representation-of-stacks)
    - [Linked representation of stack](#Linked-representation-of-stack)
    - [Infix to Postfix](#Infix-to-Postfix)
    - [Evaluation of Postfix expression](#Evaluation-of-Postfix-expression)
    - [Infix to Prefix](#infix-to-prefix)
    - [Evaluation of Prefix expression](#Evaluation-of-prefix-expression)

- [Queue](#queue)
    - [Linear Queue](#Linear-Queue)
    - [Circular Queue](#Circular-Queue)
    - [Double Ended Queue](#Double-Ended-Queue)
    - [Priority Queue](#Priority-Queue)

## Introduction to Data Strutures
### Introduction
- Data structure usually refers to an *data organization*, *management*, and *storage* in main memory that enables efficiently access and modification.

- The **cost** of a solution is the amount of resources that the solution needs.

- A data structure requires:
    - Space for each data item it stores
    - Time to perform each basic operation
    - Programming effort

- How to select a data structure?
    - Identify the problem
    - Analyze the problem
    - Quantify the resources
    - Select the data structure

- <img src="images/01.png" width=500>

- Operations on DS: 
    - Traversing, Searching, Inserting, Deleting, Sorting, Merging.

- An algorithm must possess several properties:
    - It must be correct (must produce desired output).
    - It is composed of a series of concrete steps.
    - There can be no ambiguity.
    - It must be composed of a finite number of steps.
    - It must terminate.

- To summarize:
    - **Problem** - a function of inputs and mapping them to outputs.
    - **Algorithm** - a step-by-step set of operations to solve a specific problem or a set of problems.
    - **Program** - a specific sequences of inctructions in a prog. lang., and it may contain the implementation of many algorithms.

### Abstract Data Type
- https://youtu.be/n0e27Cpc88E

- An ADT describes a set of objects sharing the same properties and behaviors.
    - The *properties* of an ADT are its data.
    - The *behaviors* of an ADT are its operations or functions.

- Abstraction is the method of hiding the unwanted information.

- Encapsulation is a method to hide the data in a single entity or unit along with a method to protect information from outside. Encapsulation can be implemented using by access modifier i.e. private, protected and public.

### Asymptotic Notations
- Asymptotic complexity 
    - Running time of an algorithm as a function of input size `n` for large `n`
    - "Functions do more work for more input"
    - Drop all constants: `3n, 5n, 100n => n`
    - Ignore lower order terms: n<sup>3</sup> + n<sup>2</sup> + n + 5 => n<sup>3</sup>
    - Ignore the base of logs: `log(2) => ln(2)`

- f(n) = O(n<sup>2</sup>) => describes how f(n) grows in comparison to  n<sup>2</sup>

- Big-O notation, Ω (Omega) notation, Θ (Big-Theta) notation

- <img src="images/03.png" width=400>

- <a href="https://youtu.be/vsgrJrphEHo"><img src="images/04.png" width=600></a>

- <img src="images/05.png" width=600>

- **O (Big-O) notation** (worst time, upper bound, maximum complexity)
    - `0 <= f(n) <= c*g(n) for all n >= n0`
    ```
    f(n) = 3n + 2, g(n) = n, f(n) = Og(n)

    3n + 2 <= Cn
    3n + 2 <= 4n
    n >= 2

    c = 4, n >= 2
    ```
    - n<sup>3</sup> = O(n<sup>2</sup>) False
    - n<sup>2</sup> = O(n<sup>3</sup>) True

- **Ω (Omega) notation**  (best amount of time, lower bound) 
    - `0 <= c*g(n) <= f(n) for all n >=n0`
     ```
    f(n) = 3n + 2, g(n) = n, f(n) = Ωg(n)

    3n + 2 <= Cn
    3n + 2 <= n
    2n >= -2
    n >= -1

    c = 1, n >= 1
    ```

- **Θ (Big-theta) notation** (average case, lower & upper sandwich)
    - `0 <= c1*g(n) <= f(n) <= c2*g(n)`
    ```
    f(n) = 3n + 2, g(n) = n, f(n) = Θg(n)
    
    C1*n <= 3n + 2 <= C2*n

    3n + 2 <= C2*n            c1*n <= 3n + 2
    3n + 2 <= 4n              3n + 2 >= n
    n >= 2                    n >= -1

    c2 = 4, n >= 2            c1 = 1, n >= 1
    n >=2 // We must take greater number, which is true for both
    ```

## Searching Techniques
- Searching is an operation which finds the location of a given element in a list.

- The search is said to be successful or unsuccessful depending on whether the element that is to be searched is found or not.

### Linear Search
- **Problem**: Given an array `arr[]` of `n` elements, write a function to search a given element `x` in `arr[]`.

-  In this type of search, a sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.
<br><img src="images/06.gif" width=400>

- Pseudocode:
    ```
    procedure linear_search (list, value)

        for each item in the list
            if match item == value
                return the item's location
            end if
        end for

    end procedure
    ```

- <a href="codes/01_linear_search.cpp">Linear search in C++</a> | <a href="codes/01_linear_search.py">Linear search in Python</a>
    ```python
    # If x is present then return its location,
    # otherwise return -1

    def search(arr, n, x):

        for i in range(0, n):
            if (arr[i] == x):
                return i
        return -1

    # Driver Code
    arr = [2, 3, 4, 10, 40]
    x = 10
    n = len(arr)

    # Function call
    result = search(arr, n, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
    ```

- Analysis:
    - Best case `O(1)`
    - Average `O(n)`
    - Worst `O(n)`

### Binary Search
- Binary search method is very fast and efficient. Array must be sorted! <br><img src="images/07.png" width=500>

- In this method:
    - To search an element we compare it with the element present at the center of the list. If it matches then the search is successful.
    - Otherwise , the list is divided into two halves:
        - One from 0th element to the center element (first half)
        - Another from center element to the last element (second half)
    - The searching will now proceed in either of the two halves depending upon whether the element is greater or smaller than the center element.
    - If the element is smaller than the center element then the searching will be done in the first half, otherwise in the second half.

- Pseudocode:
    ```
    Procedure binary_search
        A ← sorted array
        n ← size of array
        x ← value to be searched

        Set lowerBound = 1
        Set upperBound = n 

        while x not found
            if upperBound < lowerBound 
                EXIT: x does not exists.
        
            set midPoint = lowerBound + ( upperBound - lowerBound ) / 2
            
            if A[midPoint] < x
                set lowerBound = midPoint + 1
                
            if A[midPoint] > x
                set upperBound = midPoint - 1 

            if A[midPoint] = x 
                EXIT: x found at location midPoint
        end while
    
    end procedure
    ```

- <a href="codes/02_binary_search.cpp">Binary search in C++</a> | <a href="codes/02_binary_search.py">Recursive binary search in Python</a> | <a href="codes/02_binary_search_iter.py">Iterative binary search in Python</a>
    ```python
    # Binary search in Python
    ```

- Analysis:
    - Best-case `O(1)` 
    - Average `O(log n)` 
    - Worst-case `O(log n)`


## Sorting Techniques
Coming soon ...


## Linked List
- Array Limitations:
    - Fixed size
    - Physically stored in consecutive memory locations
    - To insert or delete items, may need to shift data

- Variations of linked list: linear linked list, circular linked list, double linked list

- *head* pointer "defines" the linked list (it is not a node) <br><img src="images/08.png" width=600>

- Advantages of Linked Lists:
    - The items do NOT have to be stored in consecutive memory locations.
        - So, can insert and delete items without shifting data.
        - Can increase the size of the data structure easily.
   
    - Linked lists can grow dynamically (i.e. at run time) – the amount of memory space allocated can grow and shrink as needed.

- Disadvantages of Linked Lists:
    - A linked list will use more memory storage than arrays. It has more memory for an additional linked field or next pointer field.
    - Linked list elements cannot randomly accessed.
    - Binary search cannot be applied in a linked list.
    - A linked list takes more time in traversing of elements.

- Nodes:
    - A linked list is an ordered sequence of items called **nodes**
  
    - A node is the basic unit of representation in a linked list
 
    - A node in a singly linked list consists of two fields:
        - A *data* portion
        - A *link (pointer)* to the *next* node in the structure
  
    - The first item (node) in the linked list is accessed via a front or head pointer
        - The linked list is defined by its head (this is its starting point)

- We will use `Node` and `List` classes (https://youtu.be/Dfu7PeZ3v2Q)
    ```cpp
    class Node {
        public:
            int info;	 // data
            Node* next;	 // pointer to next node in the list
            /*Node(int val) {info = val; next=NULL}*/
    };

    class List {
        public:
            // head: a pointer to the first node in the list. 
            // Since the list is empty initially, head is set to NULL
            List(void) {head = NULL;} // constructor
            ~List(void);			  // destructor
	    
        private:
	        Node* head;
    };
    // isEmpty, insertNode, findNode, deleteNode, displayList
    ```

- Boundary condition 
    - Empty data structure
    - Single element in the data structure
    - Adding / removing beginning of data structure
    - Adding / removing end of data structure
    - Working in the middle

### Insertion at beginning in Linked List
- https://youtu.be/yMoHuOZzMpk

- It is just a 2-step algorithm:
    - `New node` should be connected to the `first node`, which means the head. This can be achieved by assigning the address of node to the head.
   
    - `New node` should be considered as a `head`. It can be achieved by declaring head equals to a new node.

-   ```cpp
    void insertStart(int val) { 
        Node *node = new Node; // create a new node (node=node)
        node->info=val; // put value

        if(head == NULL) { // check if the list is empty
            head = node; 
            node->next = NULL
        }
        else { // if list is not empty
            node->next = head; 
            head = node; 
        }
    }
    ```

### Insertion at the end in Linked List
-   ```cpp
    void insertEnd(int val) {
        Node *node = new Node; // create a new node
        node->info = val; // put value
        node->next = NULL; // pointer of last node is NULL 

        if(head == NULL) { // if empty
            node->next = NULL
            head = node;
        }
        else { 
            Node *cur = new Node();
            cur = head;
            while(cur->next != NULL) {
                cur = cur->next;
            }
            cur->next = node;
        }
    }
    ```
### Insertion at Particular Position
- In this case, we don’t disturb the `head` and `tail` nodes. Rather, a new node is inserted between two consecutive nodes. 

- We call one node as `current` and the other as `previous`, and the new node is placed between them.

- Two steps we need to insert between `previous` and `currect`:
    - Pass the address of the new node in the next field of the previous node.
   
    - Pass the address of the current node in the next field of the new node.

-   ```cpp
    void insertPosition(int pos, int val) {
        Node *pre; 
        Node *cur; 
        Node *node = new Node;

        node->data = val; 
        cur = head; 

        for(int i=1; i<pos; i++) {
            pre = cur; 
            cur = cur->next; 
        } 
        pre->next=node; 
        node->next=cur; 
    }
    ```

-   ```cpp
    void insertSpecificValue(int sp_val, int data) {     
        Node *pre; 
        Node *cur; 
        Node *node = new Node;

        node->info = data; 
        cur = head; // "current" in the beginning points to head, and "previous" points to NULL

        while(cur->data != sp_val) {
            pre = cur; 
            cur = cur->next; 
        } 
        node->next = cur;            
        cur->next = node; 
    }
    ```

### Deleting the First Node from a Linked List
- Following steps we need to remove the first node:
    - Check if the linked list exists or not `if(head == NULL)`.
    
    - Check if it is one element list.
    
    - However, if there are nodes in the linked list, then we use a pointer variable `PTR` that is set to point to the first node of the list. For this, we initialize `PTR` with Head that stores the address of the first node of the list. 
    
    - Head is made to point to the next node in sequence and finally the memory occupied by the node pointed by PTR is freed and returned to the free pool.

-   ```cpp
    void deleteFirst() {
        if(head == NULL) { // if empty
            cout << "Underflow" << endl;
        }
        else if(head.next == NULL) { // if only one element
            Node *ptr;
            ptr = head;
            head = NULL;
            delete ptr;
        }
        else { // otherwise
            Node *ptr;
            ptr = head;
            head = head->next;
            delete ptr;
        }
    }
    ```

### Deleting the Last Node from a Linked List
- Following steps we need to remove the first node:
    - Check if the linked list exists or not `if(head == NULL)`.
   
    - Check if it is one element list.
    
    - Take a pointer variable `PTR` and initialize it with `head`. That is, `PTR` now points to the first node of the linked list. In the while loop, we take another pointer variable `PREPTR` such that it always points to one node before the PTR. Once we reach the last node and the second last node, we set the NEXT pointer of the second last node to NULL, so that it now becomes the (new) last node of the linked list. The memory of the previous last node is freed and returned back to the free pool.

-   ```
    STEP 1: IF START = NULL
            WRITE UNDERFLOW
            Go to STEP 8
            [END OF IF]
    STEP 2: SET PTR = START
    STEP 3: REPEAT Steps 4 and 5 while PTR->NEXT != NULL
    STEP 4:     SET PREPTR = PTR
    STEP 5:     SET PTR = PTR->NEXT
            [END OF LOOP]
    STEP 6: SET PREPTR->NEXT = NULL
    STEP 7: FREE PTR
    STEP 8: EXIT
    ```

### Deleting the Specific Node in a Linked List
-   ```
    Step 1: IF START = NULL
            Write UNDERFLOW Go to Step 10
            [END OF IF]
    Step 2: SET PTR = START
    Step 3: SET PREPTR = PTR
    Step 4: Repeat Steps 5 and 6 while PREPTR-> DATA I = NUM
    Step 5: SET PREPTR = PTR
    Step 6: SET PTR = PTR -> NEXT
            [END OF LOOP)
    Step 7: SET TEMP = PTR
    Step 8: SET PREPTR -> NEXT - PTR-> NEXT
    Step 9: FREE TEMP
    Step 10: EXIT
    ```

## Circular Linked List
- https://youtu.be/7ELt4-z4YeI

- In a circular linked list, the last node contains a pointer to the first node. 

- No node points to NULL!

- Start at `head`, iterate until you find `head` again: `t == head, t.next == head`

- Complexity for all operations is `O(n)`

-   ```cpp
    class  Node {
        int info;
        Node *next;
    };

    class CircularLList {
        public:
            Node *last;

        CircularLList() {
            last = NULL;
        }
    };
    ```

### Insertion at Beginning in Circular Linked List
```cpp
void addBegin(int val) {
    Node *temp = new Node();
    temp->info=val;

    if (last == NULL) { // if empty
        last = temp;
        temp->next = last; // points next to itself // in simple LL it pointed to NULL
    }
    else {
        temp->next = last;
        last = temp;
    }

```

### Insertion at the End in Circular Linked List
```cpp
while cur->next != last) {
    cur = cur->next;
}
cur->next = New;
New->next = last; 
```

### Insertion at Particular Position in Circular Linked List 
```cpp
void insertNode(int item,int pos) {
	Node *New = new Node();
    Node *prev;
	Node *cur;
	New->data = item;    

	if(last == NULL){	// insert into empty list
		last = New;
		last->next = last;
   	}

	prev = last;
	cur = last->next;

	for (int i=1; i<pos; i++) {
        prev = cur;
	    cur = cur->next;
	} 	

    New->next = cur;	
	prev->next = New;
}
```

### Deletion a Node in Circular Linked List
- From a single-node circular linked list (node points to itself):
    ```cpp
    last = NULL;
    delete cur;
    ```

- Delete the head node:
    ```cpp
    while(prev->next != last) {
        prev = cur; 
        cur = cur->next;
    }
    prev->next = cur->next;	
    delete cur;
    ```

- Delete a middle node Cur:
    ```cpp
    for(i=1; i<=pos; i++) {
        prev = cur; 
        cur = cur->next;
    }
    prev->next = cur->next;
    delete cur;
    ```

- Delete the end node:
    ```cpp
    while(cur->next != last) { 
        prev = cur; 
        cur = cur->next;
    }
    prev->next = cur->next;   
    delete cur;
    ```
## Doubly Linked List
- https://youtu.be/v8xyoI11PsU

- DLL contains a pointer to the next as well as the previous node in the sequence. Therefore, it consists of three parts:
    - data
    - a pointer to the next node
    - a pointer to the previous node

-   ```cpp
    class Node {
        int info;
        Node *next;
        Node *pre;
    }
    ```


## Stacks
- Last in, first out (LIFO)

- Elements are added to and removed from the top of the stack (the most recently added items are at the top of the stack).

- <img src="images/09.png" width=300> <img src="images/10.png" height=207>

- Operations on Stack:
    - `push(i)`	to insert the element `i` on the top of the stack.
    - `pop()` to remove the top element of the stack and to return the removed element as a function value.
    - `top()` to return the top element of stack(s)
    - `empty()` to check whether the stack is empty or not. It returns true if stack is empty and returns false otherwise.

### Array Representation of Stacks
- In the computer’s memory, stacks can be represented as a linear array.

- Every stack has a variable called TOP associated with it, which is used to store the address of the topmost element of the stack.

- TOP is the position where the element will be added to or deleted from

- There is another variable called MAX, which is used to store the maximum number of elements that the stack can hold.

- Underflow and Overflow:
	- if `TOP = NULL` (underflow) it indicates that the stack is empty and 
	
    - if `TOP = MAX–1` (overflow) then the stack is full.

- Pseudocode for PUSH, POP, PEEK:
    ```
    PUSH operation
    Step 1: IF TOP - MAX-3
            PRINT "OVERFLOW" 
            Goto Step 4
            [END OF IF]
    Step 2: SET TOP = TOP + 1
    Step 3: SET STACK[TOP] = VALUE
    Step 4: END

    
    POP operation
    Step 1: IF TOP MILL
            PRINT "UNDERFLOW"
            Goto Step 4 
            [END OF IF]
    Step 2: SET VALUE STACK(TOP) 
    Step 3: SET TOP = TOP - 1
    Step 4: END

    PEEK operation
    Step 1: IF TOP = NULL
            PRINT "STACK IS EMPTY"
            Goto Step 3
    Step 2: RETURN STACK[TOP]
    Step 3: END
    ```

### Linked Representation of Stack
- Stack may be created using an array. This technique of creating a stack is easy, but the drawback is that the array must be declared to have some fixed size. 

- In a linked stack, every node has two parts—one that stores data and another that stores the address of the next node. The START pointer of the linked list is used as TOP.

- PUSH is adding a node at beginning, POP deleting front node.

### Infix to Postfix

- Algorithm used (Postfix):
    - Step 1: Add `)` to the end of the infix expression

    - Step 2: Push `(` onto the STACK

    - Step 3: Repeat until each character in the infix notation is scanned
        - IF a `(` is encountered, `push` it on the STACK.
        
        - IF an `operand` (whether a digit or acharacter) is encountered, `add` it postfix expression.
        
        - IF a `)` is encountered, then
            - a. Repeatedly `pop` from STACK and `add` it to the postfix expression until a `(` is encountered.
            - b. Discard the `(`. That is, remove the `(` from STACK and do not add it to the postfix expression
        
        - IF an operator `O` is encountered, then
            - a. Repeatedly `pop` from STACK and `add` each operator (popped from the STACK) to the postfix expression which has the **same precedence or ahigher precedence than O**
           
            - b. `Push` the operator to the STACK
        -
         [END OF IF]

    - Step 4: Repeatedly `pop` from the STACK and `add` it to the postfix expression until the STACK is empty
    - Step 5: EXIT

- If `/` adds to `((-*` we will take only `*`, then it will be `((-/`

-   ```
    Example: (A * B) + (C / D) – (D + E)

    (A * B) + (C / D) – (D + E))    [put extra ")" at last]

    Char	Stack	    Expression
    (	    ((	        Push at beginning "("
    A	    ((	        A
    *	    ((*	        A
    B	    ((*	        AB
    )	    (	        AB*
    +	    (+	        AB*
    (	    (+(	        AB*
    C	    (+(	        AB*C
    /	    (+(/	    AB*C
    D	    (+(/	    AB*CD
    )	    (+	        AB*CD/
    -	    (-	        AB*CD/+
    (	    (-( 	    AB*CD/+
    D	    (-( 	    AB*CD/+D
    +	    (-(+	    AB*CD/+D
    E	    (-(+	    AB*CD/+DE
    )	    (-	        AB*CD/+DE+
    )		            AB*CD/+DE+-
    ```

### Evaluation of Postfix expression
-   ```
    [AB*CD/+DE+-] ==> 2 3 * 2 4 / + 4 3 + -

    Char	Stack	    Operation
    2	    2	
    3	    2, 3	
    *	    6	        2*3
    2	    6, 2	
    4	    6, 2, 4 	
    /	    6, 0	    2/4
    +	    0	        6+0
    4	    6, 4	
    3	    6, 4, 3	
    +	    6, 7	    4+3
    -	    -1	        6-7
    ```

### Infix to Prefix

#### First method
- Algorithm used (Prefix): 

    - Step 1. `Push` `)` onto STACK, and `add` `(` to start of the A.

    - Step 2. Scan A from right to left and repeat step 3 to 6 for each element of A until the STACK is empty or contain only `)`

    - Step 3. If an **operand** is encountered add it to B

    - Step 4. If a **right parenthesis** is encountered push it onto STACK

    - Step 5. If an **operator** is encountered then:
        - a. Repeatedly pop from STACK and add to B each operator (on the top of STACK) which has **only higher precedence than the operator**.
        
        - b. Add operator to STACK

    - Step 6. If **left parenthesis** is encountered then

        - a. Repeatedly pop from the STACK and add to B (each operator on top of stack until a right parenthesis is encountered)

        - b. Remove the left parenthesis

    - Step 7. **Reverse** B to get prefix form

-   ```
    Example: 14 / 7 * 3 - 4 + 9 / 2

    (14 / 7 * 3 - 4 + 9 / 2 [Put extra "(" to start]

    Char	Stack	    Expression
    2	    )	        Push at beginning ")"
    /	    )/	        2
    9	    )/	        2 9
    +	    )+	        2 9 /
    4	    )+	        2 9 / 4
    -	    )+-	        2 9 / 4
    3	    )+-	        2 9 / 4 3
    *	    )+-* 	    2 9 / 4 3
    7	    )+-*	    2 9 / 4 3 7
    /	    )+-*/	    2 9 / 4 3 7
    14	    )+-*/       2 9 / 4 3 7 14
    (                   2 9 / 4 3 7 14 / * - +

    DON'T FORGET TO REVERSE: + - * / 14 7 3 4 / 9 2
    ```

#### Second method 
- Algorithm used (Prefix): 

    - Step 1: Reverse the infix string. Note that while reversing the string you must interchange left and right parentheses. Eg. `(3+2)` will be `(2+3)` but not `)2+3(`

    - Step 2: Obtain the postfix expression of the infix expression obtained in Step 1.

    - Step 3: Reverse the postfix expression to get the prefix expression

-   ```
    Example: 14 / 7 * 3 - 4 + 9 / 2

    Reversed: 2 / 9 + 4 - 3 * 7 / 14

    Char	Stack	    Expression
    2	    (	        Push at beginning "("
    /	    (/	        2
    9	    (/	        2 9
    +	    (+	        2 9 /
    4	    (+	        2 9 / 4
    -	    (+-	        2 9 / 4
    3	    (+-	        2 9 / 4 3
    *	    (+-* 	    2 9 / 4 3
    7	    (+-*	    2 9 / 4 3 7
    /	    (+-*/	    2 9 / 4 3 7
    14	    (+-*/       2 9 / 4 3 7 14
    )                   2 9 / 4 3 7 14 / * - +

    DON'T FORGET TO REVERSE: + - * / 14 7 3 4 / 9 2

    NOTE: Operator with the same precedence must not be popped from stack
    ```

### Evaluation of Prefix Expression
- For postfix we eveluated `a+b` but in prefix we will do `b+a`

-   ```
    Example: 14 / 7 * 3 - 4 + 9 / 2 ==> + - * / 14 7 3 4 / 9 2

    Char	Stack	            Operation
    2	    2	
    9	    2, 9	
    /	    4	                9/2 [but in postfix we did 2/9]
    4	    4, 4 	
    3	    4, 4, 3	    
    7	    4, 4, 3, 7
    14	    4, 4, 3, 7, 14
    /	    4, 4, 3, 2	        14/2  
    *       4, 4, 6             2*2
    -       4, 2                6-4
    +       6                   2+4
    ```

## Queue
- First in, first out (FIFO)

- The queue has a **front** and a **rear**
    - <img src="images/11.png" width=400>
    - Items can be removed only at the **front**
    - Items can be added only at the ohter end, the **rear**

- Types of queues:
    - Linear queue
    - Circular queue
    - Double ended queue (Deque)
    - Priority queue

### Linear Queue
- A queue is a sequence of data elements

- **Enqueue** (add element to back) when an item is `inserted` into the queue, it always goes `at the end` (rear). 

- **Dequeue** (`remove` element from front) when an item is taken from the queue, it always comes `from the front`. 

- Implemented using either array or a linear linked list.

- Array implementation:
    - **ENQUEUE**
        ```
        Step 1: IF REAR = MAX-1 
                    Write OVERFLOW
                    Goto step 4
                [END OF IF]
        Step 2: IF FRONT = -1 and REAR = -1
                    SET FRONT = REAR = 0
                ELSE
                    SET REAR = REAR + 1
                [END OF IF]
        Step 3: SET QUEUE [REAR] = NUM
        Step 4: EXIT
        ```
    - **DEQUEUE**
        ```
        Step 1: IF FRONT = -1 OR FRONT > REAR %3D
                    Write UNDERFLOW
                ELSE
                    SET VAL = QUEUE[FRONT]
                    SET FRONT = FRONT + 1 %3D   
                [END OF IF]
        Step 2: EXIT
        ```

- Linked list implementation:
    - **ENQUEUE** the same as adding a node at the end
        ```
        Step 1: Allocate memory for the new node and name it as PTR
        Step 2: SET PTR -> DATA = VAL
        Step 3:
            IF FRONT = NULL
                SET FRONT = REAR = PTR
                SET FRONT -> NEXT = REAR -> NEXT = NULL
            ELSE
                SET REAR -> NEXT = PTR
                SET REAR = PTR
                SET REAR -> NEXT = NULL
            [END OF IF]
        Step 4: END

        ```
    - **DEQUEUE** the same as deleting a node from the beginning
        ```
        Step 1: IF FRONT = NULL
                    Write "Underflow"
                    Go to Step 5
                [END OF IF]

        Step 2: SET PTR = FRONT
        Step 3: SET FRONT = FRONT -> NEXT
        Step 4: FREE PTR
        Step 5: END
        ```

### Circular Queue
- https://youtu.be/ihEmEcO2Hx8


### Double Ended Queue
- It is exactly like a queue except that elements can be added to or removed from the **head** or the **tail**.

- No element can be added and deleted from the middle. 

- Implemented using either a circular array or a circular doubly linked list.

- In a deque, two pointers are maintained, `LEFT` and `RIGHT`, which point to either end of the deque. 

- The elements in a deque extend from the `LEFT` end to the `RIGHT` end and since it is circular, `Deque[N–1]` is followed by `Deque[0]`.

- Two types:
    - **Input restricted deque** In this, insertions can be done only at one of the ends, while deletions can be done from both ends.

    - **Output restricted deque** In this deletions can be done only at one of the ends, while  insertions can be done on both ends.

- <img src="images/12.png" width=400>

### Priority Queue
- A priority queue is a data structure in which each element is assigned a priority.

- The priority of the element will be used to determine the order in which the elements will be processed. 

- An element with *higher priority* is processed before an element with a l*ower priority*.

- Two elements with the same priority are processed on a first-come-first-served (FCFS) basis.
