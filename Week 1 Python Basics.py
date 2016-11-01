
"""
Created on Tue Nov  1 18:02:28 2016

@author: Ewa
"""
# Week 1:Python Basics
###Exercise: vara varb
"""
Assume that two variables, varA and varB, are assigned values, either numbers or strings.
Write a piece of Python code that prints out one of the following messages:
"string involved" if either varA or varB are strings
"bigger" if varA is larger than varB
"equal" if varA is equal to varB
"smaller" if varA is smaller than varB
"""
if type(varA)== str or type(varB) == str:
    print('string involved')
elif int(varA) > int(varB):
    print('bigger')
elif int(varA) == int(varB):
    print('equal')
else :
    print('smaller')
    
###Exercise: while exercise 1
"""
In this problem you'll be given a chance to practice writing some while loops.
1. Convert the following into code that uses a while loop.
print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!"""
k = 2
while (k<=10):
    print(k)
    k+=2
print('Goodbye!')

"""
2. Convert the following into code that uses a while loop.
prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""
k = 10
print('Hello!')
while (k>=2):
    print(k)
    k-=2
    
"""
3. Write a while loop that sums the values 1 through end, inclusive. 
end is a variable that we define for you. So, for example, if we define end 
to be 6, your code should print out the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.
For problems such as these, do not include input statements or define 
variables we will provide for you. Our automating testing will provide values
 so write your code in the following box assuming these variables 
 are already defined.
 """
total=0
k=0
while (k<=end):
    total+=k
    k+=1
print(total)

##for exercise 1
"""
In this problem you'll be given a chance to practice writing some for loops.
1. Convert the following code into code that uses a for loop.
prints 2
prints 4
prints 6
prints 8
prints 10
prints "Goodbye!"
"""
k = 2
for k in range(2,12, 2):
    print(k)
print('Goodbye!')

"""
2. Convert the following code into code that uses a for loop.
prints "Hello!"
prints 10
prints 8
prints 6
prints 4
prints 2
"""
print('Hello!')
for k in range(10, 0, -2):
    print(k)
    

"""
3. Write a for loop that sums the values 1 through end, inclusive. 
end is a variable that we define for you. So, for example, if we define 
end to be 6, your code should print out the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.
For problems such as these, do not include input statements or 
define variables we will provide for you. Our automating testing will 
provide values so write your code in the following box assuming these variables 
are already defined.
"""
total=0
for k in range (1, end+1, 1):
    total+=k
print(total)

## Problem Set 1
"""
Problem 1
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""
vowels = 'aeiou'
count = 0
for i in range(0, len(vowels)):
    for j in range(0, len(s)):
        if (s[j]==vowels[i]):
            count=count+1
print('Number of vowels:', count)

"""
Problem 2
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
bob = 'bob'
count = 0
for j in range(0, len(s)-2):
        if (s[j:j+3]==bob):
            count=count+1
print('Number of times bob occurs is:', count)

"""
Problem 3
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the 
letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print
Longest substring in alphabetical order is: abc
"""
longest=""
temp=""
k=0
for i in range(0,len(s)-1):
    temp=s[i]
    k=i+1
    while (k<len(s) and s[k]>=s[k-1]):
            temp=temp+s[k]
            k=k+1
    if len(temp)>len(longest):
        longest=temp
        temp=""
print('Longest substring in alphabetical order is:', longest)
