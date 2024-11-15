## Two main ways
- if-else
    - ternary operator: syntex: condition ? run this if true : run this if false
- switch

### if-else
- Syntax:
```c#
if(condition){
    body
}
else if (condition){
    body
}
else {
    body
}
```

### switch
- Syntax:
```c#
switch(expression){
    case LabelOne :
        body
        break;
    case LabelTwo :
        body
        break;
    case LabelThree:
    case LabelFour:
    case LabelFive:
        body_for_all_three_cases
        break;
    default:
        body
        break;
}
```

