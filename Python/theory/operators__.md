---
markdown:
  image_dir: /assets
  path: operators.md
  ignore_from_front_matter: true
  absolute_image_path: false
export_on_save:
  markdown: true
---

# Operators

+ **Arithematic operator**
+ **Comparision(Relational) operator**
+ **Assignment operator**
+ **Logical operator**
+ **Bitwise operator**
+ **Membership operator**
+ **Identity operator**

<div style="page-break-after: always"></div>

## Arithematic Operator
|operator|Function|Example|
|:---|:---|:---|
|$+$|Addition|a + b|
|$-$|Subtraction|a - b|
|$*$|Multiplication|a * b|
|$/$|Division|a / b|
|$//$|Floor division|a // b, returns integer quotient after a / b|
|$**$|Exponent|a ** b = $a^b$|
|$\%$|Modulus|a %  b, return remainder after a / b|
---------------------------------------

## Comparision(Relational) operator

+ Perform comparision on operands
+ And retrun $True$ or $False$

|operator|Function|Example|
|:---|:---|:---|
| $==$  | Equal to | a == b|
| $!=$  | Not equal to| a != b|
| $>$ | Greater than| a > b|
| $<$ | Less than| a < b|
| $>=$  | Greater than or equal to| a >= b|
| $<=$  | Less than or equal to| a <= b|

<div style="page-break-after: always"></div>

## Assignment Operator

|operator|Example|Equivalent to|
|:---|:---|:---|
|$=$|x = 5 	  |x = 5 |
|$+=$|	x += 5 	|x = x + 5 |
|$-=$|	x -= 5 	|x = x - 5 |
|$*=$|	x *= 5 	|x = x * 5 |
|$/=$|	x /= 5 	|x = x / 5 |
|$\%=$|	x %= 5 	|x = x % 5 |
|$//=$| 	x //= 5|	x = x // 5 |
|$**=$| 	x **= 5| 	x = x ** 5 |
|$\&=$|	x &= 5 	|x = x & 5 |
|\|$=$|	x \|= 5 	|x = x \| 5 |
|^$=$|	x ^= 5 	|x = x ^ 5 |
|$>>=$| 	x >>= 5| 	x = x >> 5 |
|$<<=$| 	x <<= 5| 	x = x << 5 |

<div style="page-break-after: always"></div>

## Logical Operator

+ Logical operator perform boolean logic
+ Always returns True or false if applied on boolean operands
+ **and** and **or** eturn actual value if applied on other than boolean operands
  + **and** return whatever is in right side of operator
  + **or** return whatever is in left side of operator
  
+ **not** ( if applied on other than boolean operands ) retuns **True** if operand is $0 $ otherwise, **False**

|operator|Function|Example|
|:---|:---|:---|
|$and$| True if both the operands are true| a **and** b|
|$or$|True if either of the operands is true|a **or** b|
|$not$| True if operand is false (complements the operand)|**not** (a)|
---------------------------------------
## Bitwise Operator

+ Act on operands as if they were string of binary digits.
+  It operates bit by bit.
+ x=10 (0000 1010), y=4 (0000 0100)

|operator|Function|Example|
|:---|:---|:---|
 $\&$|	Bitwise AND 	|x & y = 0 (0000 0000)
 $\mid$|	Bitwise OR 	|x \| y = 14 (0000 1110)
 $\tilde{}$|	Bitwise NOT 	|~x = -11 (1111 0101)
 ^|	Bitwise XOR 	|x \^ y = 14 (0000 1110)
 $>>$| 	Bitwise right shift 	|x >> 2 = 2 (0000 0010)
 $<<$| 	Bitwise left shift 	|x << 2 = 40 (0010 1000)

<div style="page-break-after: always"></div>

## Membership operator

+ Used to check whehter a value of variable is available in sequence (list, tuple, dictionary, set) or not
+ In case of dictionary we can only check for keys
+ Retruns $True$ or $False$

|operator|Function|Example|
|:---|:---|:---|
| $in$      |$True$ if **value/variable is found in the sequence**| 'Hello' **in**  'Hello world!' |
| $not\ in$ |$True$ if **value/variable is not found in the sequence**|'Java' **not in** 'Hello world!'|    
---------------------------------------

## Identity operator

+ Determines if two values(variables) are located on the same part of memory
+ Determines whether a value is of a certain class or type
+ Compares memory location of two objects
+ Retruns $True$ or $False$

|operator|Function|Example|
|:---|:---|:---|
| $is$      | returns $True$ if the type of the value in <br> the **right operand points to the same type in the left operand.** | ``` x = 5```<br> type(x) **is** int |
| $is\ not$ |returns $True$ if the type of the value in the <br> **right operand points to a different type than the value in the left operand.**| ``` x = 5.2```<br>type(x) **is not** int|  

<div style="page-break-after: always"></div>
