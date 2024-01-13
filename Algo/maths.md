- Prime Numbers
- LCM & HCF
- Factorials
- Quadratic Equations
- Mean, Median & Mode
- Permutation & Combination
- Arithmetic Progression
- Geometric Progression


### Prime Numbers:
- The numbers that can be divided only by 1 and itself are called prime numbers.
- Example: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
- Usages of prime numbers in computer science are
    - Crypgraophy: The security is based on difficulties in finding prime numbers. 
    - Hashing Functions
    - Random Number Generator
    - DSA: For example, the size of hastable is often a prime number, to reudce the clustering & improve distribution of values.
    - Error Checking: Used in error-checking methods such as checksums & CRC (Cyclic Redundancy Check).


### LCM & HCF:
#### Least Common Multiple (LCM): 
- It is the smallest multiple that is divisible by two or more numbers. 
- To find the LCM, you can list the multiples of each number and find the smallest one that all numbers share.
- Example: LCM of 4 and 6 is 12 because it's the smallest number divisible by both 4 and 6.

#### Highest Common Factor (HCF):
- It is the largest number that divides two or more numbers without leaving a remainder. 
- To find the HCF, you can factorize the numbers into their prime factors and identify the common factors.
- Example: HCF of 12 and 18 is 6 because it's the largest number that divides both 12 and 18.


### Factorials:
- Factorial of a Number: The factorial of a non-negative integer n (denoted as n!) is the product of all positive integers less than or equal to nn.
- Example: 5!=5×4×3×2×1=1205!=5×4×3×2×1=120

### Quadratic Equations:
- An equation of the form ax^2+bx+c=0, where a, b, and c are constants and x is the variable. 
- These equations can have zero, one, or two real roots depending on the discriminant (b^2−4ac).

### Mean, Median & Mode
- Mean: Also known as the average, it is calculated by summing up all values in a dataset and dividing by the number of values.
- Median: The middle value of a dataset when arranged in ascending or descending order. If there's an even number of values, the median is the average of the two middle values.
- Mode: The value that appears most frequently in a dataset.

### Permutation & Combination:
    - 
#### Permutation
- It is the number of ways of selecting a subset of n objects from a set of n distinct objects.
- In, Permutation the order of selection matters and replacement is not allowed.
- The number Permutation of n objects taken r at a time is P(n, r) = n! / (n - r)!.
- Example: 
    - Permutation of 3 objects taken 2 at a time is 6, as 3! / (3 - 2)! = 6.
    - Permutation of 5 objects taken 3 at a time is 60, as 5! / (5 - 3)! = 60.

#### Combination
- It is the number of ways of selecting a subset of n objects from a set of n distinct objects.
- In, Combination the order of selection doesn't matter and replacement is allowed.
- The number Combination of n objects taken r at a time is C(n, r) = n! / (r! * (n - r)!).
- Example: 
    - Combination of 3 objects taken 2 at a time is 3, as 3! / (2! * (3 - 2)! = 3.
    - Combination of 5 objects taken 3 at a time is 10, as 5! / (3! * (5 - 3)! = 10.

### Arithmetic Progression
A sequence of numbers where the difference between consecutive terms is constant. 
The nth term of an AP is given by a+(n−1)×d, where a is the first term and d is the common difference.
- Formula: 
    - nth term, an = a1 + (n - 1) * d 
    - sum of N terms of AP, sn = n/2 * (2a + (n - 1) * d)
    - common difference , d = a2-a1 = a3 - a2 = an - an-1



### Geometric Progression
A sequence of numbers where each term after the first is obtained by multiplying the previous term by a fixed, non-zero number called the common ratio (r). 
The nth term of a GP is given by arn−1arn−1, where a is the first term.
- Formula: 
    - nth terms of GP, an = a * r^n
    - sum of N terms of GP, sn = a * (1 - r^n) / (1 - r)
    - common ratio, r = (a2 - a1) / (a1 - a0)
