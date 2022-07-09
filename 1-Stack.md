# Stack

## Introduction
Have you been in the supermarket doing your groceries and decided to buy bread to make the most famous college meal. I am not talking about Maruchan Ramen Noodles Soup. I am talking about the peanut butter sandwich. However, someone has put the bread on the shelves for you. You grab the one that is in front of you.  

  

## Characteristics of Stacks
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Stack-sv.svg.png)

* Stacks are linear data structre, which means its Big O notaion is O(1). 
* Stacks are similar to list since it stores data in an order. 
* Stacks follows LIFO (Last In First Out) data structure, meaning you can only add or delete an element at the top.


## Common Stack Operations
In Python, a list can be used to implement a stack. To **push** an iteam to the top of a stack, we can use the Python’s built-in **append** function. To **pop** and remove the topmost iteam of the stack, we implement **pop** function. Also, if we would like to know the length of our stack, we can implement the Python's built-in **len** function. 
| Common Stack Operation | Description | Python Code | Big-O Notation |
| ---------------------- | ----------- | ----------- | -------------- |
| push(v)                | Inserts the value "v" to the top of the stack | **my_stack.append(v)** | O(1) |
| pop() | Deletes and returns the topmost element of the stack | **value = my_stack.pop()** | O(1) |
| size() | Returns the size of the stack | **length = len(my_stack)** | O(1) |
| empty() | Returns TRUE if the stack is empty | **if len(my_stack) ==0:** | O(1) |


## Example


## Problem to Solve
