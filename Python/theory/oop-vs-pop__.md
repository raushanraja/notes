---
markdown:
  image_dir: /assets
  path: oop.md
  ignore_from_front_matter: true
  absolute_image_path: false
export_on_save:
  markdown: true
---

# Descreption

+ combination of data and method parts
+ may have several variables and methods

|Class|Object|
|:---|:---|
|Generalized form of object|Instance of class|
|eg:- vehicle|car,bus,etc|

## class syntax

> ```python
> class MyDemo:
>   pass
> #follows Pascal case convention
> ```

## function syntax

> ```python
>  def funName():
> #follows camelCase convention"
> ```
> 
### Example

>```python
>#  class definition
>    class MyDemo:
>        x=20
>        y=30
>        def myFun(slef):
>            print(self.x)
>
>    obj = Mydemo() # Object creation
>    obj.myFun()    # Function call with the object
>```



|OOP|POP|
|:---|:---|
|Object oriented programming||
|Programs are created by class and object||
|In real time have many data hiding techniques||
|Follows bottom to up approch||
|User defined data type||

#### Q. Why do we don't have multiple inheritance in python?

+ In case we have two different parent class with same method, then there is problem of ambiguity to run the method. That's why python does not support Multiple Inheritance.