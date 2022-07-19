
# Tree

## Introduction
When I was a kid, I did not have a play station or a computer where I could play video games. Also, I did not have Cable T.V. so, so I used to spend most of my free time playing with my friend outdoors. I remember once we were pretending to have a tree house. As I was climbing a tree, one of its branches hit my eye, but I did not notice it until a friend told me that I had blood on my face. After looking at myself in a side mirror of a car, I got super scared since I did not know if I have lost my eye or how deep the injury was. My mom took me to the hospital where they aided me. I had a successful recovery and nothing serious happened to me. However, we are not talking about these kinds of trees. Instead, we are talking about Binary Trees. 

**Binary Trees**

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Binary%20Tree.png)

* Binary trees cannot link to no more than two other nodes.
* The top node is called **root** node.
* A node that is not associated to other node is known as **leaf** node.
* A node that has attached nodes is a **parent** node.
* The node attached to a parent node are **child** nodes.
* A **subtree** are the nodes to the left and right of any parent node form a subtree.
  

## Binary Search Trees
Also known as BST. A BST is a binary tree and has rules when data is put into it. The way data is placed is by comparing the data with the parent node. If new node is less than parent node, then it is put in the left. If the new node is greater than parent node, then is placed in the right. By following these rules, the data is placed in the tree sorted.

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Binary%20Tree%20search.png)


**Add Node to BST**

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Add%20Node%20to%20BST.png)

Let's say we would like to insert the value 19 in the tree. First, it will compare to the value of the root. Since it is greater, if will go to the right. Then it will encounter with a new value where it will follow the same process. In this case, 25. Since 19 is less than 25, the new value will go to the left and check if there is an additional node to compare. In this case, there is not a node to compare, so the new value has found its place in the tree.

* When we have a balanced tree, we have **O(log n).**

**Unbalanced BST**
In the past example, the tree was balanced since the root node had a value of 14. What about if we add the values in ascending order, this is: 2-5-11-18-30-33-34. 

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Unbalanced%20BST.png)

The tree is not a tree anymore, instead it looks more like a linked list. 

* When we have a unbalanced tree, we have **O(n).**
## Balanced Binary Search Trees

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Balanced%20AVL%20Tree.png)

**Unbalanced AVL Tree after Adding Node**
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Unbalanced%20AVL%20Tree%20after%20Adding%20Node.png)

**Rebalanced AVL Tree**
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Rebalanced%20AVL%20Tree.png)

## BST Operations

### INSERTING INTO A BST




### TRAVERSING A BST

## BST IN PYTHON
 
| Common Stack Operation | Description | Big-O Notation |
| ---------------------- | ----------- | -------------- |
| insert(v)              | Inserts the value "v" into the tree |  O(log n) |
| remove(v)              | Remove the value "v" from the tree. |  O(log n) |
| contains(v) | 	Determine if a value is in the tree. | O(log n) |
| traverse_forward | Visit all objects from smallest to largest. | O(n)) |
| traverse_reverse | Visit all objects from largest to smallest. | O(n) |
| height(node) | Determine the height of a node. If the height of the tree is needed, the root node is provided.. | O(n) |
| size() | Return the size of the BST. | O(1) |
| empty() | Returns true if the root node is empty. This can also be done by checking the size for 0. | O(1) |


## Example




## Problem to Solve









 
[Back to Welcome Page](0-welcome.md)
