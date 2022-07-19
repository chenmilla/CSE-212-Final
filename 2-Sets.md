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
In Python, a set can be implemented using curly braces. Example: **my_set = {5,7,9}.** To create an empty set, we use the following code: **empty_set = set().** The **in** operator can be used to see if an iteam exist within a set.
| Common Stack Operation | Description | Python Code | Big-O Notation |
| ---------------------- | ----------- | ----------- | -------------- |
| add(value)	                | 	Adds "value" to the set | **my_set.add(v)** | O(1) - Performance of hashing the value (assuming good conflict resolution) |
| member(value)	 | Determines if "value" is in the set	 | **if value in my_set:** | O(1) - Performance of hashing the value (assuming good conflict resolution) |
| member(value)	 | Determines if "value" is in the set | **if value in my_set:** | O(1) - Performance of hashing the value (assuming good conflict resolution) |
| size()	 | Returns the number of items in the set | **length = len(my_set)** | O(1) |

Intersection and union between two sets can be done as following in Python:
![This is an image](https://github.com/chenmilla/CSE-212-Final/blob/main/images/Intersection_Union.JPG)

## Example
Let's say you will like to match TV shows that you have in common with your family:

```python 

Elisa = {"Breaking bad", "Better Call Saul", "The Office", "Money Heist", "More Girls", "Love is Blind", "Gilmore girls" }
Juanfer ={"Breaking bad", "Better Call Saul", "The Office", "Narcos", "Prison Break", "Ozark", "Survivor", "The last dance", "Luis Miguel"}
Jorge ={"Breaking bad", "Club de Cuervos", "Flash", "Stranger Things", "Cobra Kai", "Better Call Saul", "Maradona", "Ronaldo","The Office"}

set_A = Elisa.intersection(Juanfer) 
set_B = set_A.intersection(Jorge) 
print(set_B)



```
The following code will give the following result:
```
{'Breaking bad', 'The Office', 'Better Call Saul'}
```


## Problem to Solve
Your school wants to create an app to help students with dating. To see if students could be a great match, they need to have a least three things in common. Show a simple example of how you can implement this. 

Your code should include the following:
* At least 4 participants
* Ask the participants about their interests.
* Display if they are a great match or not.

You can check your code with the solution here:[Solution](datingApp.py)
 
[Back to Welcome Page](0-welcome.md)
