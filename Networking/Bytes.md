#### Hexadecimal
- A byte (8 bits, decimal range: 0-255) in Hexadecimal is always represented by 2 Hex Characters.

- It  ranges from 00 to FF, where
    - Each Hexadecimal charater represents 4 bits( a small byte aka nibble, decimal range: 0-15)
    - Exmaple:
    ```
    Decimal    Hexadecimal    Binary
    
    0           00              0000 0000
    1           01              0000 0001
    .....
    128         80              1000 0000
    .....
    255         FF              1111 1111


    If we see for 128 as  example:
    In decimal it's 128,
    In Binary  it's 10000000
    In Hexadecimal, we are breaking the Binary representation in blocks of 4
    so after that it comes as 1000 0000 , which after converting individual blocks into decimal Hexadecimal 8 0,
    combining both gives us 80 in Hexadecimal.
    ```
- Reason of breaking the binary representation in blocks of 4 is that, maximum value that a hexadecimal character can represent is 15. 
    - So, if binary value is 1111 it can be represented by a single hex character
    - Anything greater (like 1111 0001) cannot be represented by a single hex character
    - So, we break the binary representation in blocks of 4, which can give maximum of (2) 1111 and 1111, which can easily be represented by 2 single hex character
    - Exmaple:
    ```
    1111 1111 -> FF
    ```
