#String methods

+ $split(a)$
+ $find(a,[b,c])$
+ $upper()$
+ $lower()$
+ $capitalize()$
+ $title()$
+ $len(a)$
+ $center(a,b)$
+ $fill(a,b)$
+ $zfill(a)$


## split()

+ Return a list of the words in the string
+ The default value) means split according to any whitespace, and discard empty strings from the result.
+ maxsplit: Maximum number of splits to do  -1 (the default value) means no limit.

### Example

>```python
>mystr="Hello, I , am, raushan"
>mystr.split(",")
>mystr.split(",",maxsplit=1)
>```

## find()

+ returns index of first occurance

### Example

```python
   mystr="hello, I , am, raushan"
   mystr.find('l',3,5)             #find()

   mystr.upper()                   # retrun uppercase string
   mystr.lower()                   # return lowercase string
   mystr.capitalize()              # capitilizes first charater of first word of string. 
   mystr.title()                   # capitilizes first character of every word in string.


 

```
  