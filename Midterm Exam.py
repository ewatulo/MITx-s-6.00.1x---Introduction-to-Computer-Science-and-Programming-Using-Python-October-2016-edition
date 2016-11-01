####### Midterm Exam
### Problem 4
#Implement a function called closest_power that meets the specifications below.
#def closest_power(base, num):
#    '''
#    base: base of the exponential, integer > 1
#    num: number you want to be closest to, integer > 0
#    Find the integer exponent such that base**exponent is closest to num.
#    Note that the base**exponent may be either greater or smaller than num.
#    In case of a tie, return the smaller value.
#    Returns the exponent.
#    '''
#    # Your code here
#For example,
#closest_power(3,12) returns 2
#closest_power(4,12) returns 2
#closest_power(4,1) returns 0
#Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    r=0
    count=0
    t=[]
    while r<num:
        r=base**count
        t.append(abs(num-r))
        count=count+1
    return t.index(min(t))

##Problem 5
#10.0/10.0 points (graded)
#Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
#Hint: You will need to traverse both lists in parallel.
#This function takes in two lists of numbers and returns a number.
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    total=[]
    for i in range(len(listA)):
        total.append(listA[i]*listB[i])
    return sum(total)
    
## Problem 6
#15.0/15.0 points (graded)
#Implement a function that meets the specifications below.
#def deep_reverse(L):
#    """ assumes L is a list of lists whose elements are ints
#    Mutates L such that it reverses its elements and also 
#    reverses the order of the int elements in every element of L. 
#    It does not return anything.
#    """
#    # Your code here
#For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
#Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
    
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    for i in L:
        i.reverse()
    L.reverse()
    

##Problem 7
#20.0/20.0 points (graded)
#Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.
#Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:
#intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
#difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
#Here are two examples:
#If f(a, b) returns a + b
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
#then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
#If f(a, b) returns a > b
#d1 = {1:30, 2:20, 3:30}
#d2 = {1:40, 2:50, 3:60}
#then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    t=()
    inter={}
    diff={}
    t=(inter, diff)
    d1_copy=d1.copy()
    d2_copy=d2.copy()
    for key in d1:
        if key in d2:
            inter[key]=f(d1[key], d2[key])
            
            del(d1_copy[key])
            del(d2_copy[key])
        else:
            diff[key]=d1[key]
    for key in d2_copy:
        diff[key]=d2_copy[key]
        
        t=(inter, diff)
    return t
    
    
##Problem 8
#20.0/20.0 points (graded)
#Implement a function that meets the specifications below.
#For example, the following functions, f, g, and test code:
#def f(i):
#    return i + 2
#def g(i):
#    return i > 5
#L = [0, -10, 5, 6, -4]
#print(applyF_filterG(L, f, g))
#print(L)
#Should print:
#6
#[5, 6]
    
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    L_copy=L[:]
    
    for i in L_copy:
        if not g(f(i)):
            L.remove(i)
    if len(L)==0:
        return -1
    else:
        return max(L)
        

##Problem 9
#15.0/15.0 points (graded)
#Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).
def flatten(l):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    t=[]
    for elem in l:
        if isinstance(elem,(list, tuple)):
            for x in flatten(elem):
                t.append(x)
        else:
            t.append(elem)
    return t