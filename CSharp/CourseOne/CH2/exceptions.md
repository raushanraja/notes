#### Exception
- These are unexpected behaviour that occurs during execution of program
and needs to be handeled properly.
- These breaks the normal flow of program.
- In C# it's handeled by using `try-catch-finally` block
- Finally block always runs.
    - This block is mainly used to free resources
    - Like closing database connection
    - File etc..
- Syntax:
```c#
try{
    body
}
catch(Exception type){
    body
}
finally{
    body
}
```


