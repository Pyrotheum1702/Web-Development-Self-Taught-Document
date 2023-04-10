# Content Overview
1. Array Data Structure
2. Linked List Data Structure
3. Stack Data Structure
4. Queue Data Structure
5. Heap Data Structure
6. Hash Table Data Structure
7. Binary Tre Data Structure
8. Recursion Function
9. Sorting Algorithms
# Array Data Structure
1. Lesson Content:
  - Array Data Structure
  - Array in Python
2. What i learned:
- An array is a collection of items stored at contiguous memory locations.
- List and Array are similar. However user can not constraint the type of elements stored in a list.
- Array can be handled in Python by a module named `array`. They can be useful when we have to manipulate only a specific data type values.
  - `array` module:
    - The data type is specified at the array creation time by using a single character is called the type code.
    - `array(i, [x])`: where `i` is type code, `[x]` is the value list.
    - Elements of an array can only have a specific type specified by the type code.
# Linked List Data Structure
1. Lesson Content:
  - Linked List Data Structure
2. What i learned:
  - Linked List is a linear collection of items, where each item point to the next item in the list. Item in linked list are called *node* where each node have 2 part, a part that hold the value and a pointer to the next node, linking each node to the other.
  - Linked List also have 2 item are the *head* and the *tail* where the head point to the first node and the tail point to the last node.
# Stack Data Structure
1. Lesson content:
  - Stack Data Structure
2. What i learned:
  - Stack is a linear collection of items, where items are inserted and remove in a specific order.
  - Retrieval an item from the stack follow the LIFO principle(last in first out), where the item to be retrieve will always be the last item that was added to the stack.
  - In Python, we could use `list` to mimic a stack.
# Queue Data Structure
1. Lesson content:
  - Queue Data Structure
2. What i learned:
  - Queue is similar to stack, is a linear collection of items, where items are inserted and remove in a specific order.
  - Retrieval an item from the stack follow the FIFO principle(first in first out), where the item to be retrieve will always be the oldest item that was added to the stack.
  - In Python, we could use `list` to mimic a queue.
# Heap Data Structure
1. Lesson content:
  - Heap Data Structure
2. What i learned:
  - Heap is a tree based data structure in which each parent node is less than or equal to its child node. Which is a min heap, where a max heap is the opposite with each parent node is greater than or equal to its child node. It is useful to implement a priority queue where the queue item that has the lowest value or the highest value to get dequeued first.
  - In Python, we could use `heapq` module. This module has the relevant functions to carry out various operations on heap data structure.
  - Below is a list of these functions:
    - `.heapify(x)`: Converts a regular list `x` to a heap.
    - `.heappush(i)`: Push the item onto the heap , maintaining the heap invariant.
    - `.heappop()`: Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, `IndexError` is raised.
  - A node in a heap could have at most 2 children node.
  - Min Heap:
    - The value a node must be higher than the value of the parent node
    - Items of a heap is stored in an array or a list in Python, where the root node is the first element, the root node should always have the lowest value in the heap. The child of a node could be found using these formula:
      - `i*2+1` and `i*2+2`: where `i` is the index of the parent node
        - For instance:
          - Consider this array: [1, 2, 6, 7, 4, 8, 11]
          - 2 and 6 is child of 1 :
            - Index of 1 is 0:
            - `0*2+1 = 1` -> `array[1] = 2`
            - `0*2+2 = 2` -> `array[2] = 6`
          - 7 and 4 is child of 2 :
            - Index of 2 is 1:
            - `1*2+1 = 3` -> `array[3] = 7`
            - `1*2+2 = 4` -> `array[4] = 4`
          - 8 and 11 is child of 6 :
            - Index of 6 is 2:
            - `2*2+1 = 5` -> `array[5] = 8`
            - `2*2+2 = 6` -> `array[6] = 11`
# Binary Tree Data Structure
1. Lesson content:
  - Binary Tree Data Structure
  - Binary Search Tree
2. What i learned:
  - A tree data structure is a hierarchical structure that is used to represent and organize data in a way that is easy to navigate and search. It is a collection of nodes that are connected by edges(pointer) and has a hierarchical relationship between the nodes. The topmost node of the tree is called the root, and the nodes below it are called the child nodes. A Recursive structure.
  - Binary Tree is defined as a tree data structure where each node has at most 2 children.
  - Binary search tree is binary tree but with the nodes that are sorted by these rule:
    - the child node on the left must have the value that is smaller than the parent node value
    - the child node on the right must have the value that is greater than the parent node value
  - Each node of a Binary Tree contains the following parts:
    - Data / Value
    - Reference to left child node
    - Reference to right child node
  - The tree can be traversed by deciding on a sequence to visit each node. There are three ways which we use to traverse a tree:
    - In-order Traversal
    - Pre-order Traversal
    - Post-order Traversal
# Recursion
1. Lesson Content:
  - Recursion
2. What i learned:
  - Recursion is the process in which a function calls itself over and over until a certain condition is met, otherwise infinite loop will occur.
  - let's take factorial for the example:
    - `factorial 5` is basically `5 * factorial 4` and `factorial 4` is basically `4 * factorial 3` and so on until `factorial 1` is 1 so the recursion stop and return all the upper layer function call all the way to the top an return the computation.
    - `factorial(5)` could be graphically describe as this:
```mermaid
5! = 5 * 4! -> [ 5 * 24 = 120 ]
  4! = 4 * 3! -> [ 4 * 6 = 24  ]
    3! = 3 * 2! -> [ 3 * 2 = 6   ]
      2! = 2 * 1! -> [ 2 * 1 = 2   ]
        1! = 1
```
# Sorting Algorithms
1. Lesson Content:
  - Bubble Sort
  - Quick Sort
2. What i learned:
  - Bubble sort is used to repeatedly compare adjacent items in a list or an array and exchange them if they are not in ascending or descending order.
  - Quick sort:
    - It picks an element as a pivot and partitions the given array around the picked pivot.
    - Quick sort turn an array to a two part and split them up over and over again recursively until the size of a part is equal or lesser then 1 and sort the elements during that process.
    - How Quick sort work i depth:
      - 1. Pick a any element as a pivot point.
      - 2. Initialize the left and right pointers, pointing to the left and right ends of the list.
      - 3. Start moving the left and right pointers toward the pivot while their values are smaller and greater than the pivot, respectively.
      - 4. At each step, check and place the elements smaller than the pivot to the left of the pivot, and elements greater than that to the right.
      - 5. When the two pointers meet or cross each other, we have completed one iteration of the list and the pivot is placed in its correct position in the final sorted array.
      - 6. Now, two new lists are obtained on either side of the pivot. Repeat steps 1–5 on each of these lists until all elements are placed in their correct positions.
