## Types:
1. for loop
    - `for`
    - `foreach`
2. while loop
3. do while loop

## Loop Control Statements
- break : Break out of the loop. Syntax: `break;`
- continue : Skips the current iteration and go to next iteration. Syntax: `continue;`

### For loop
- It performs an operation for a set number of times.

#### 1.1 `for`
- Runs till the loop condition is met using the control variable
- Syntax:
```c#
for(control variable; loop condition; updating control varialbe){
    body
}
```
- Example:
```c#
for(int i = 0; i<=10; i++){
    Console.WriteLine("i is currently {0}", i);
}
```

#### 1.2 `foreach`
- Syntax:
```c#
foreach(control_variable in someo_array){
    body
}
```
- Example:
```c#
int[] nums = [1,3,4,5,6];
string s = "console.writeline print the given statement on console";

foreach(int i in nums){
    Console.WriteLine("I in {0}", i);
}


int count = 0;
foreach(char c in s){
    if(c == 't'){
        count ++;
    }
}
```


### 2. While Loop
- Performs an operation for as long a particular condition exits.
- Syntax:
```c#
while(condition){
    body
}
```
- Example:
```c#
string inputStr = "";
while(inputStr != "exit"){
    inputStr= Console.ReadLine("");
    Console.WriteLine("You entered {0}", inputStr);
}
Console.WriteLine("While Loop exited");
```

### 3. Do-While Loop
- Do-While runs at least once and everything is similar to while loop
- Syntax:
```c#
do {
    body
}while(condition);
```
- Example:
```c#
int x = 0;
do{
    Console.WriteLine("X is {0}", x);
}while(x > 0);
```
