# Sets

## Introduction
The planet where we live is best known as earth. It is estimated to be 4.543 billion years old. Many of us believe that the first people who lived on earth were Adan and Eve. Since then, human beings have procreated and filled the earth. As today, there are around 7.753 billion people living on earth. The probability of you having a DoppelgäNger (look-alike) is about one in 1 trillion according to a research done by the University of Adelaide. Even if you find a DoppelgäNger, still that person is not you. This is what Set is about: there are not duplicates.
    

  

## Characteristics of Sets
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/640px-PolygonsSetIntersection.svg.png)

* The average time for doing various operations on sets is O(1) 
* Sets are good for avoiding duplicates. 
* Sets don't care about order like lists, stacks and queues.
* Sets are good for finding unique values.
* Sets are good for finding differences 

## Hashing 
It is the process of converting an input into a fixed-size number using an algorithm

**index(n) = n**
This formula helps to either add or lookup for data. N tell us the index where is stored or where is going to be stored. Example: 
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/index(n)_n.png)

**index(n) = n % 10**
This formula acomplish the same as formula index(n), but this one is helpful for bigger number. For example Lets say say we want to store the following number in a list 78499852, the index where this number is going to be store at is 2. What about 9982456? This number will be store in index number 6. If you notice, it is stored in index 5489126n, the last digit (n) of whatever number the data has been hashed to. The equation we just described can be generalized as follows: **index(n) = n % sparse_list_size**. 
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/index(n)_n%2510.png)

**index(n) = hash(n) % sparse_list_size**
This equation is used for strings and floats. Hash(n) will convert non-integers into integers, and then it can acomplish the formulas explained above.

![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/hash_examples..JPG)

**NOTE** Not everything can be hashed. For example, in the above picture, you can notice that lists in Python cannot be hashed.

## Conflicts
Conflicts can occur when we are storing data in the same index. We can solve this with either open addressing or chaining.

**Open addressing**
This is when looks for the next index avaible. It can be implemented in different ways, but one of the most common is to look to the right one spot at a time until it finds an empty index. 
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/open_addressing.png)

**Chaining**
In this case, it will stay at the same index, but it will link a list to that index. By doing this, many values can be stored to its corresponding index. 
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/chaining.png)

**NOTE:** By dealing with conflicts, our O(1) performance may approach O(n) if conflict is high. We can avoid this by incrementing the size of our list.   

## Common Sets Operations
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

You can check your code with the solution here:
 
[Back to Welcome Page](0-welcome.md)
