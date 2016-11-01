# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:03:13 2016

@author: Ewa
"""
# Week 2 Simple Program
"""
Exercise: Guess my number
In this problem, you'll create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you 
give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
Here is a transcript of an example session:
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.
When the user enters something invalid, you should print out a message to 
the user explaining you did not understand their input. Then, you should re-ask 
the question, and prompt again for input. For example:

Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c

"""
print("Please think of a number between 0 and 100! ")
epsilon=1
numGuess = 0
low = 0
high = 100
ans = (low+high)//2
choice='a'

while choice!="c":
    numGuess+=1
    print("")
    print("Is your secret number", ans, "?")
 
    choice=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
    
    if str(choice)=="l":
        low=ans
    elif str(choice)=="h":
        high=ans
    elif str(choice)=="c":
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = (low+high)//2
print("Game over. Your secret number was:", ans)

"""
Exercise: square
Write a Python function, square, that takes in one number and returns the square of that number.
This function takes in one number and returns one number.
"""
def square(x):
    '''
    x: int or float.
    '''
    return x**2
    

"""
Exercise: eval quadratic
Write a Python function, evalQuadratic(a, b, c, x), that returns the 
value of the quadratic a⋅x2+b⋅x+c.
This function takes in four numbers and returns a single number.
"""
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2) + b*x+c
    

"""
Exercise: fourth power
Write a Python function, fourthPower, that takes in one number and returns 
that value raised to the fourth power.
You should use the square procedure that you defined in an earlier exercise 
exercise (you don't need to redefine square in this box; when you call square, 
the grader will use our definition).
This function takes in one number and returns one number.
"""
def fourthPower(x):
    '''
    x: int or float.
    '''
    s= square(x)
    t = square(s)
    return t
    

"""
Exercise: odd
Write a Python function, odd, that takes in one number and returns True 
when the number is odd and False otherwise.
You should use the % (mod) operator, not if.
This function takes in one number and returns a boolean.
"""
def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return bool(x%2)

"""
Exercise: iter power
Write an iterative function iterPower(base, exp) that calculates the 
exponential base^exp by simply using successive multiplication. For example, 
iterPower(base, exp) should compute base^exp by multiplying base times itself 
exp times. Write such a function below.
This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥ 0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed.
"""
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result=1
    if exp==0:
       return 1
    else:
       while exp>0:
            result=result*base
            exp=exp-1
    return result

"""
Exercise: power recur
In Problem 1, we computed an exponential by iteratively executing successive 
multiplications. We can use the same idea, but in a recursive function.
Write a function recurPower(base, exp) which computes base^exp by recursively 
calling itself to solve a smaller version of the same problem, and then 
multiplying the result by base to solve the initial problem.
This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥0. It should return one numerical value. 
Your code must be recursive - use of the ** operator or looping constructs is 
not allowed."""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==0:
        return 1
    else:
        return base*recurPower(base, exp-1)
        
"""
Exercise: gcd iter
The greatest common divisor of two positive integers is the largest 
integer that divides each of them without remainder. For example,
gcd(2, 12) = 2
gcd(6, 12) = 6
gcd(9, 12) = 3
gcd(17, 12) = 1
Write an iterative function, gcdIter(a, b), that implements this idea. 
One easy way to do this is to begin with a test value equal to the smaller 
of the two input arguments, and iteratively reduce this test value by 1 until 
you either reach a case where the test divides both a and b without remainder, 
or you reach 1."""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = 0
    if a>b:
        test=b
    else:
        test=a
    while test>1:
        if a%test==0 and b%test==0:
            break
        else:
            test=test-1
    return test
    
##Exercise: gcd recur
#The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
#gcd(2, 12) = 2
#gcd(6, 12) = 6
#gcd(9, 12) = 3
#gcd(17, 12) = 1
#A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:
#If b = 0, then the answer is a
#Otherwise, gcd(a, b) is the same as gcd(b, a % b)
#Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = 0
    if b==0:
        test=a
    else:
        test=gcdRecur(b, a%b)
    return test

####################
#Exercise: is in
#We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.
#First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!
#If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)
#Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.
#As you design the function, think very carefully about what the base cases should be.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    import math
    char = str(char)

    if len(aStr)==0:
        return False
    elif len(aStr)==1:
        if aStr==char:
            return True
        else:
            return False
    else:
        if len(aStr)%2==0:
            half = len(aStr)/2
            middle = int(half-1)
        else:
            half = math.floor(len(aStr)/2)
            middle = int(half)
            
        if aStr[middle]==char:
            return True
        elif char<aStr[middle]:
            return isIn(char, aStr[0:middle])
        else:
            return isIn(char, aStr[middle+1:len(aStr)])
            
##Grader
#A regular polygon has n number of sides. Each side has length s.
#The area of a regular polygon is: 0.25∗n∗s2tan(π/n)
#The perimeter of a polygon is: length of the boundary of the polygon
#Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

def polysum(n, s):
    import math
    ar = (0.25*n*(s**2))/math.tan(math.pi/n)  
    perimeter = n*s
    total = ar+perimeter**2
    return round(total, 4)


######Problem Set 2 ###############
#Problem 1 - Paying Debt off in a Year
#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#
#The following variables contain values as described below:
#
#balance - the outstanding balance on the credit card
#
#annualInterestRate - annual interest rate as a decimal
#
#monthlyPaymentRate - minimum monthly payment rate as a decimal
#
#For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
#
#Remaining balance: 813.41
#instead of
#
#Remaining balance: 813.4141998135 
#So your program only prints out one thing: the remaining balance at the end of the year in the format:
#
#Remaining balance: 4784.0
#A summary of the required math is found below:
#
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

unpaidBalance = balance
monthlyInterests = annualInterestRate/12.0
month=0
for i in range(0,12):
    month=month+1
    minimumPayment = round(unpaidBalance*monthlyPaymentRate,2)
    unpaidBalance = round(unpaidBalance-minimumPayment,2)
    #print("Month", month, "remaining balance:", unpaidBalance)
    unpaidBalance = round(unpaidBalance + round(unpaidBalance*monthlyInterests,2),2)
print("Remaining balance:", unpaidBalance)

##
#Problem 2 - Paying Debt Off in a Year
#Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
#In this problem, we will not be dealing with a minimum monthly payment rate.
#The following variables contain values as described below:
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
#Lowest Payment: 180 
#Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
monthlyInterests = annualInterestRate/12.0
month=0
lowestPayment=0
unpaidBalance = 1000000
while unpaidBalance>0:
    lowestPayment=lowestPayment+10
    unpaidBalance = balance
    for i in range(0,12):
        month=month+1
        unpaidBalance = unpaidBalance-lowestPayment
    #print("Month", month, "remaining balance:", unpaidBalance)
        unpaidBalance = unpaidBalance + unpaidBalance*monthlyInterests
print('-------------------')
print("Lowest Payment:", lowestPayment)

###
#Problem 3 - Using Bisection Search to Make the Program Faster
#You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)
#Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!
#The following variables contain values as described below:
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.
#What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.
#In short:
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
#Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   
while abs(balance) >= epsilon:
    balance = initBalance
    month = 0
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high + low)/2.0
minPay = round(minPay,2)
print('-------------------')
print('Lowest Payment: ' + str(minPay))
