# Stack

## Introduction
Have you been in the supermarket doing your groceries and bought bread to make the most famous college meal? By college meal, I don't mean Maruchan Ramen Noodles Soup. I am talking about the peanut butter sandwich. However, someone has put that bread loaf on the shelves for you. You grabbed the one that is in front of you and the bread loaf that was behind it, now becomes the first one on the shelve. This system is best known as LIFO (Last In First Out). This is exactly how Stacks work.      

  

## Characteristics of Stacks
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Stack-sv.svg.png)

* Stacks are linear data structre, which means its Big O notaion is O(n). 
* Stacks are similar to list since it stores data in an order. 
* Stacks follows LIFO (Last In First Out) data structure, meaning you can only add or delete an element at the top.
* Stacks are good at reversing things.
* Stacks are excellent implementation for backtracking. For example, when you press *Ctrl + Z* to reverse something that went wrong while typing, you are using stacks. 

## Common Stack Operations
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

Your code should include the following:
* Create two empty stacks, one for Samsung Galaxy and the other one for iPhone.
* Push each model to its corresponding stack. Your top smartphone should be the most recent model. 
* Give your Grand Father the option to choose between the two, then display the result.
 
