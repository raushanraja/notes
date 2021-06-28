  
  
  
##  Data Strctures
  
  
+ <img src="https://latex.codecogs.com/gif.latex?list"/>
+ <img src="https://latex.codecogs.com/gif.latex?set"/>
+ <img src="https://latex.codecogs.com/gif.latex?tuple"/>
+ <img src="https://latex.codecogs.com/gif.latex?dictionary"/>
  
<div style="page-break-after: always"></div>
  
##  list
  
  
+ collection of items
+ items can be of different data types
+ duplicate items are allow
+ items or elements of list are indexed and the order is preserved
+ items can be accessed using their index
+ items are defined inside the square brackets <img src="https://latex.codecogs.com/gif.latex?[%20&#x5C;%20]"/>
+ list in python are mutable
  
+ >```python
  >fruits=['apple',2,'green',True] #METHOD 1
  >fruits=list(['apple',2,'green',True]) #METHOD 2
  >```
  
----------------------
  
##  set
  
  
+ collection of items
+ items can be of different data types
+ duplicate items are considered only once
+ items or elements unindexed and unordered
+ items cannot be accessed using their index but can be iterated over
+ items are defined inside the curly brackets <img src="https://latex.codecogs.com/gif.latex?&#x5C;{%20&#x5C;}"/>
+ list in python are mutable
  
+ >```python
  >fruits={'apple',2,'green',True} #METHOD 1
  >fruits=set(['apple',2,'green',True]) #METHOD 2
  >```
  
<div style="page-break-after: always"></div>
  
##  tuple
  
  
+ collection of items
+ items can be of different data types
+ duplicate items are allow
+ items or elements of list are indexed and the order is preserved
+ items can be accessed using their index
+ items are defined inside the paranthesis <img src="https://latex.codecogs.com/gif.latex?(%20&#x5C;%20)"/>
+ list in python are immutable (once created tuple cannot be changed), deletion is not allowed, changing a value is not allowed
  
+ >```python
  >fruits=('apple',2,'green',True) #METHOD 1
  >fruits=tuple(['apple',2,'green',True]) #METHOD 2
  >```
  
--------------------------
  
##  dictionary
  
  
+ collection of key:value pair
+ key:value can be of different data types
+ duplicate values are allow but duplicate keys are not allowed
+ pairs are not ordered
+ values can be accessed using their key
+ pairs are defined inside the curly brackets <img src="https://latex.codecogs.com/gif.latex?&#x5C;{%20&#x5C;%20&#x5C;}"/>
+ list in python are mutable
  
+ >```python
  >fruits={'apple':2,'green':True} #METHOD 1
  >fruits=dict({'apple':2,'green':True}) #METHOD 2
  >```
  
<div style="page-break-after: always"></div>
  
##  Built-in Methods on data-structures
  
  
####  List
  
|Method| Description|
|:---|:---|
|<img src="https://latex.codecogs.com/gif.latex?append()"/> |Adds an element at the end of the list|
|<img src="https://latex.codecogs.com/gif.latex?clear()"/> |Removes all the elements from the list|
|<img src="https://latex.codecogs.com/gif.latex?copy()"/> |Returns a copy of the list|
|<img src="https://latex.codecogs.com/gif.latex?count()"/> |Returns the number of elements with the |specified value
|<img src="https://latex.codecogs.com/gif.latex?extend()"/> |Add the elements of a list (or any |iterable), to the end of the current list
|<img src="https://latex.codecogs.com/gif.latex?index()"/> |Returns the index of the first element |with the specified value
|<img src="https://latex.codecogs.com/gif.latex?insert()"/> |Adds an element at the specified position|
|<img src="https://latex.codecogs.com/gif.latex?pop()"/> |Removes the element at the specified |position
|<img src="https://latex.codecogs.com/gif.latex?remove()"/> |Removes the item with the specified value|
|<img src="https://latex.codecogs.com/gif.latex?reverse()"/> |Reverses the order of the list|
|<img src="https://latex.codecogs.com/gif.latex?sort()"/> |Sorts the list|
  
<div style="page-break-after: always"></div>
  
####  Set
  
  
|Method|Description|
|:----|:----|
|<img src="https://latex.codecogs.com/gif.latex?add()"/>|Adds an element to the set|
|<img src="https://latex.codecogs.com/gif.latex?clear()"/>|Removes all the elements from the set|
|<img src="https://latex.codecogs.com/gif.latex?copy()"/>|Returns a copy of the set|
|<img src="https://latex.codecogs.com/gif.latex?difference()"/>|Returns a set containing the |difference between two or more sets
|<img src="https://latex.codecogs.com/gif.latex?difference&#x5C;_update()"/>|Removes the items in this set |that are also included in another, specified set
|<img src="https://latex.codecogs.com/gif.latex?discard()"/>|Remove the specified item|
|<img src="https://latex.codecogs.com/gif.latex?intersection()"/>|Returns a set, that is the |intersection of two other sets
|<img src="https://latex.codecogs.com/gif.latex?intersection&#x5C;_update()"/>|Removes the items in this |set that are not present in other, specified set(s)
|<img src="https://latex.codecogs.com/gif.latex?isdisjoint()"/>|Returns whether two sets have a |intersection or not
|<img src="https://latex.codecogs.com/gif.latex?issubset()"/>|Returns whether another set contains |this set or not
|<img src="https://latex.codecogs.com/gif.latex?issuperset()"/>|Returns whether this set contains |another set or not
|<img src="https://latex.codecogs.com/gif.latex?pop()"/>|Removes an element from the set|
|<img src="https://latex.codecogs.com/gif.latex?remove()"/>|Removes the specified element|
|<img src="https://latex.codecogs.com/gif.latex?symmetric&#x5C;_difference()"/>|Returns a set with the |symmetric differences of two sets
|<img src="https://latex.codecogs.com/gif.latex?symmetric&#x5C;_difference&#x5C;_update()"/>|inserts the |symmetric differences from this set and another
|<img src="https://latex.codecogs.com/gif.latex?union()"/>|Return a set containing the union of sets|
|<img src="https://latex.codecogs.com/gif.latex?update()"/>|Update the set with the union of this |set and others
  
<div style="page-break-after: always"></div>
  
####  Tuple
  
  
|Methods|Description|
|:----|:----|
|<img src="https://latex.codecogs.com/gif.latex?count()"/>Returns the number of times a specified |value occurs in a tuple
|<img src="https://latex.codecogs.com/gif.latex?index()"/>Searches the tuple for a specified value |and returns the position of where it was found
  
--------------------------
  
####  Dictionary
  
  
|Methods|Description|
|:----|:----|
|<img src="https://latex.codecogs.com/gif.latex?clear()"/>|Removes all the elements from the dictionary|
|<img src="https://latex.codecogs.com/gif.latex?copy()"/>|Returns a copy of the dictionary|
|<img src="https://latex.codecogs.com/gif.latex?fromkeys()"/>|Returns a dictionary with the specified keys and values|
|<img src="https://latex.codecogs.com/gif.latex?get()"/>|Returns the value of the specified key|
|<img src="https://latex.codecogs.com/gif.latex?items()"/>|Returns a list containing the a tuple for each key value pair|
|<img src="https://latex.codecogs.com/gif.latex?keys()"/>|Returns a list containing the dictionary's keys|
|<img src="https://latex.codecogs.com/gif.latex?pop()"/>|Removes the element with the specified key|
|<img src="https://latex.codecogs.com/gif.latex?popitem()"/>|Removes the last inserted key-value pair|
|<img src="https://latex.codecogs.com/gif.latex?setdefault()"/>|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
|<img src="https://latex.codecogs.com/gif.latex?update()"/>|Updates the dictionary with the specified key-value pairs|
|<img src="https://latex.codecogs.com/gif.latex?values()"/>|Returns a list of all the values in the |dictionary
|<img src="https://latex.codecogs.com/gif.latex?has&#x5C;_key()"/>|Returns true if key in dictionary dict, |false otherwise
|<img src="https://latex.codecogs.com/gif.latex?cmp()"/>|Compares elements of both dict.|
  