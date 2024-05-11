# Linked List in Python
- [Nodes and Size](#nodes-and-size)
- [Boundary condition](#boundary-condition)
- [addFirst()](#addFirst())
- [addLast()](#addLast())
- [removeFirst()](#removeFirst())
- [removeLast()](#removeLast())

## Nodes and Size
```python
class LinkedList:
    class Node:
        def __init__(self, obj):
            self.data = obj
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.currentSize = 0

    def addFirst(self, obj):
        node = self.Node(obj)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.currentSize += 1

    def addLast(self, obj):
        node = self.Node(obj)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.currentSize += 1

    def removeFirst(self):
        if self.head is None:
            return None
        tmp = self.head.data
        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.currentSize -= 1
        return tmp

    def removeLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.removeFirst()
        current = self.head
        previous = None
        while current != self.tail:
            previous = current
            current = current.next
        previous.next = None
        self.tail = previous
        self.currentSize -= 1
        return current.data
```
## Boundary Condition
- Empty data structure
- Single element in the data structure
- Adding / removing beginning of data structure
- Adding / removing end of data structure
- Working in the middle

## addFirst()
```python
def addFirst(self, obj):
        node = self.Node(obj)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.currentSize += 1
```

## addLast()
```python
def addLast(self, obj):
        node = self.Node(obj)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.currentSize += 1
```

## removeFirst()
```python
def removeFirst(self):
        if self.head is None:
            return None
        tmp = self.head.data
        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.currentSize -= 1
        return tmp
```

## removeLast()
```python
def removeLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.removeFirst()
        current = self.head
        previous = None
        while current != self.tail:
            previous = current
            current = current.next
        previous.next = None
        self.tail = previous
        self.currentSize -= 1
        return current.data
```
