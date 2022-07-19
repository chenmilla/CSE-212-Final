
# Tree

## Introduction
When I was a kid, I did not have a play station or a computer where I could play video games. Also, I did not have Cable T.V. so, so I used to spend most of my free time playing with my friend outdoors. I remember once we were pretending to have a tree house. As I was climbing a tree, one of its branches hit my eye, but I did not notice it until a friend told me that I had blood on my face. After looking at myself in a side mirror of a car, I got super scared since I did not know if I have lost my eye or how deep the injury was. My mom took me to the hospital where they aided me. I had a successful recovery and nothing serious happened to me. However, we are not talking about these kinds of trees.       

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Binary%20Tree.png)
  

## Binary Search Trees

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Binary%20Tree%20search.png)


**Add Node to BST**

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Add%20Node%20to%20BST.png)


**Unbalanced BST**

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Unbalanced%20BST.png)

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
In Python, a list can be used to implement a stack. To **push** an iteam to the top of a stack, we can use the Python’s built-in **append** function. To **pop** and remove the topmost iteam of the stack, we implement **pop** function. Also, if we would like to know the length of our stack, we can implement the Python's built-in **len** function. 
| Common Stack Operation | Description | Python Code | Big-O Notation |
| ---------------------- | ----------- | ----------- | -------------- |
| push(v)                | Inserts the value "v" to the top of the stack | **my_stack.append(v)** | O(1) |
| pop() | Deletes and returns the topmost element of the stack | **value = my_stack.pop()** | O(1) |
| size() | Returns the size of the stack | **length = len(my_stack)** | O(1) |
| empty() | Returns TRUE if the stack is empty | **if len(my_stack) ==0:** | O(1) |


## Example
Let's say you are a huge fan of soccer, which I am, and you just read a notification on your phone saying that your favorite team has signed a new player. However, you don't know anything about this player and you would like to know the history of this player, where he has played, stats, etc, we can implement Stacks to do this easily.

```python 
def player(player_name):

    
    if player_name == "haaland" or "Haaland":
        Haaland_info = ["2015–2016	Bryne 2	                     14	             18", 
        "2016–2017	Bryne                        16               0", 
        "2017	        Molde 2	                      4               2",
        "2017–2019	Molde                        39              14",
        "2019–2020	Red Bull Salzburg            16              17",
        "2020–2022	Borussia Dortmund            67              62","2022–	        Manchester City	              0	              0"]
    
    while len(Haaland_info) > 0:
        print(Haaland_info.pop())
        

name= input("What player's history would you like to know more about?: ")    

if name == "Haaland" or "haaland":

    print("Year                  Team            League appearances    Goals")
    player(name)



```
The following code will give the following result:
```
Year                  Team            League Appearances    Goals
2022–           Manchester City               0               0
2020–2022       Borussia Dortmund            67              62
2019–2020       Red Bull Salzburg            16              17
2017–2019       Molde                        39              14
2017            Molde 2                       4               2
2016–2017       Bryne                        16               0
2015–2016       Bryne 2                      14              18
```


## Problem to Solve
Your Grand Father needs a new smartphone but doesn't know which ones have come out in the past three years. He would like to buy a new smartphone, but before he would like to do some research to see which one suits better him. He has heard that Samsung Galaxy and iPhone are excellent options. To help your Grand Father, implement a solution using Stacks. 

Use the following table as a guide:
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Samsung_iPhone_table.JPG)





Your code should include the following:
* Create two empty stacks, one for Samsung Galaxy and the other one for iPhone.
* Push each model to its corresponding stack. Your top smartphone should be the most recent model. 
* Give your Grand Father the option to choose between the two, then display the result.

You can check your code with the solution here: [Solution](samsung_vs_iphone.py)
 
[Back to Welcome Page](0-welcome.md)
