---
markdown:
  image_dir: /assets
  path: data-structures.md
  ignore_from_front_matter: true
  absolute_image_path: false
export_on_save:
  markdown: true
---


## Data Strctures
  
+ $list$
+ $set$
+ $tuple$
+ $dictionary$

<div style="page-break-after: always"></div>

## list

+ collection of items
+ items can be of different data types
+ duplicate items are allow
+ items or elements of list are indexed and the order is preserved
+ items can be accessed using their index
+ items are defined inside the square brackets $[ \ ]$
+ list in python are mutable
  
+ >```python
  >fruits=['apple',2,'green',True] #METHOD 1
  >fruits=list(['apple',2,'green',True]) #METHOD 2
  >```

----------------------

## set

+ collection of items
+ items can be of different data types
+ duplicate items are considered only once
+ items or elements unindexed and unordered
+ items cannot be accessed using their index but can be iterated over
+ items are defined inside the curly brackets $\{ \}$
+ list in python are mutable
  
+ >```python
  >fruits={'apple',2,'green',True} #METHOD 1
  >fruits=set(['apple',2,'green',True]) #METHOD 2
  >```

<div style="page-break-after: always"></div>

## tuple

+ collection of items
+ items can be of different data types
+ duplicate items are allow
+ items or elements of list are indexed and the order is preserved
+ items can be accessed using their index
+ items are defined inside the paranthesis $( \ )$
+ list in python are immutable (once created tuple cannot be changed), deletion is not allowed, changing a value is not allowed
  
+ >```python
  >fruits=('apple',2,'green',True) #METHOD 1
  >fruits=tuple(['apple',2,'green',True]) #METHOD 2
  >```

--------------------------

## dictionary

+ collection of key:value pair
+ key:value can be of different data types
+ duplicate values are allow but duplicate keys are not allowed
+ pairs are not ordered
+ values can be accessed using their key
+ pairs are defined inside the curly brackets $\{ \ \}$
+ list in python are mutable
  
+ >```python
  >fruits={'apple':2,'green':True} #METHOD 1
  >fruits=dict({'apple':2,'green':True}) #METHOD 2
  >```

<div style="page-break-after: always"></div>

## Built-in Methods on data-structures

#### List
|Method| Description|
|:---|:---|
|$append()$ |Adds an element at the end of the list|
|$clear()$ |Removes all the elements from the list|
|$copy()$ |Returns a copy of the list|
|$count()$ |Returns the number of elements with the |specified value
|$extend()$ |Add the elements of a list (or any |iterable), to the end of the current list
|$index()$ |Returns the index of the first element |with the specified value
|$insert()$ |Adds an element at the specified position|
|$pop()$ |Removes the element at the specified |position
|$remove()$ |Removes the item with the specified value|
|$reverse()$ |Reverses the order of the list|
|$sort()$ |Sorts the list|

<div style="page-break-after: always"></div>

#### Set

|Method|Description|
|:----|:----|
|$add()$|Adds an element to the set|
|$clear()$|Removes all the elements from the set|
|$copy()$|Returns a copy of the set|
|$difference()$|Returns a set containing the |difference between two or more sets
|$difference\_update()$|Removes the items in this set |that are also included in another, specified set
|$discard()$|Remove the specified item|
|$intersection()$|Returns a set, that is the |intersection of two other sets
|$intersection\_update()$|Removes the items in this |set that are not present in other, specified set(s)
|$isdisjoint()$|Returns whether two sets have a |intersection or not
|$issubset()$|Returns whether another set contains |this set or not
|$issuperset()$|Returns whether this set contains |another set or not
|$pop()$|Removes an element from the set|
|$remove()$|Removes the specified element|
|$symmetric\_difference()$|Returns a set with the |symmetric differences of two sets
|$symmetric\_difference\_update()$|inserts the |symmetric differences from this set and another
|$union()$|Return a set containing the union of sets|
|$update()$|Update the set with the union of this |set and others

<div style="page-break-after: always"></div>

#### Tuple

|Methods|Description|
|:----|:----|
|$count()$Returns the number of times a specified |value occurs in a tuple
|$index()$Searches the tuple for a specified value |and returns the position of where it was found

--------------------------

#### Dictionary

|Methods|Description|
|:----|:----|
|$clear()$|Removes all the elements from the dictionary|
|$copy()$|Returns a copy of the dictionary|
|$fromkeys()$|Returns a dictionary with the specified keys and values|
|$get()$|Returns the value of the specified key|
|$items()$|Returns a list containing the a tuple for each key value pair|
|$keys()$|Returns a list containing the dictionary's keys|
|$pop()$|Removes the element with the specified key|
|$popitem()$|Removes the last inserted key-value pair|
|$setdefault()$|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
|$update()$|Updates the dictionary with the specified key-value pairs|
|$values()$|Returns a list of all the values in the |dictionary
|$has\_key()$|Returns true if key in dictionary dict, |false otherwise
|$cmp()$|Compares elements of both dict.|