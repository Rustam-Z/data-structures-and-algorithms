# Linked List in Java
- [Nodes and Size](#nodes-and-size)
- [Boundary condition](#boundary-condition)
- [addFirst()](#addFirst())
- [addLast()](#addLast())
- [removeFirst()](#removeFirst())
- [removeLast()](#removeLast())

## Nodes and Size
```java
public class LinkedList<E> implements ListI<E> {
    class Node<E> {
        E data;
        Node<E> next;
        public Node(E obj) {
            data = obj;
            next = null;
        }
    } // Node

    private Node<E> head; // head
    private int currentSize; // get current size of list
    public LinkedList() {
        head = null;
        currentSize = 0;
    }
    // addFirst(), addLast()
} // LinkedList
```

## Boundary Condition
- Empty data structure
- Single element in the data structure
- Adding / removing beginning of data structure
- Adding / removing end of data structure
- Working in the middle

## addFirst()
```java
// complexity = O(1)
public void addFirst(E obj) {
    Node <E> node = new Node<E>(obj); // create a node

    node.next = head; // new node points to head
    head = node; // change head to new node

    currentSize++; // increment size when add, decrement when delete
}
```

## addLast()

```java
// complexity = O(n)
public void addLast(E obj) {
    Node <E> node = new Node<E>(obj); // create a node

    if(head == null) { // if empty
        head = node;
        currentSize++;
        return
    }

    Node<E> tmp = head; // temporary pointer 'head'

    while(tmp.next != null) { // seek last node (it points to "null")
        tmp = tmp.next;
    }
    tmp.next = node;
    currentSize++;
}
```

```java
// complexity = O(1), because of the glogal "tail" pointer
// "tail" same as "head", it should be declared in LinkedList class
public void addLast(E obj) {
    Node <E> node = new Node<E>(obj); // create a node

    if(head == null) { // if empty
        head = tail = node;
        currentSize++;
        return
    }
    // tail = хвост
    tail.next = node;
    tail = node;
    currentSize++;
    return
}
```

## removeFirst()
```java
public E removeFirst() {
    if(head == null) // if list is empty
        return null;

    E tmp = head.data; // temp which points to head

    if(head.next == null) // if we have just one element // same as "head == tail"
        head = tail = null; 
    else 
        head = head.next; // after removing change head

    currentSize--; // decrement size
    return tmp;
}
```

## removeLast()
```java
public E removeLast() {
    if(head == null) // if list is empty
       return null;

    if(head.next == null) { // if we have just one element // same as "head == tail"
        return removeFirst();
    }

    Node<E> current = head, previous = null; // "current" in the beginning points to head, and "previous" points to null
    while(current != tail) {
        previous = current;
        current = current.next;
    }
    previous.next = null; // after deleting the last element, the previous must point to null
    tail = previous; // update tail pointer, if you will not do it you will have two linked lists

    currentSize--;
    return current.data;
}
```