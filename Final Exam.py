### Final Exam ###############
"""
Created on Tue Nov  1 17:41:27 2016

@author: Ewa
"""
#Problem 3
#10.0/10.0 points (graded)
#Numbers in Mandarin follow 3 simple rules.
#
#There are words for each of the digits from 0 to 10.
#For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
#For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If the digit is a zero, it is not included.
#Here is a simple Python dictionary that captures the numbers between 0 and 10.
#trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
#          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
#We want to write a procedure that converts an American number (between 0 and 99), written as a string, into the equivalent Mandarin.
#Example Usage
#convert_to_mandarin('36') will return san shi liu
#convert_to_mandarin('20') will return er shi
#convert_to_mandarin('16') will return shi liu
#Paste your entire function, including the definition, in the box below. Assume that we provide trans for you. Do not leave any debugging print statements.

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    result=""
    if len(us_num)==2:
            
        ###for numbers 11-19
        if us_num[0]=='1' and us_num[1]!='0':
            result=trans['10']+" "+trans[us_num[1]]
        
        ### for 10
        elif len(us_num)==2 and us_num[1]=='0' and us_num[0]=='1':
            result=trans['10']
            
        ### for 10, 20, 30....
        elif len(us_num)==2 and us_num[1]=='0' and us_num[0]!='1':
            result=trans[us_num[0]]+" "+trans['10']
            
        ## all the rest out of 2-digit group
        else:
            result=trans[us_num[0]]+" "+trans['10'] + " " + trans[us_num[1]]
    else:
        result=trans[us_num[0]]
    return result
    

###Problem 4
#20.0/20.0 points (graded)
#You are given the following definitions:
#A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
#A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.
#Implement a function that meets the specifications below.
#For example:
#If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the longest run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
#If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run of monotonically decreasing numbers in L is [5, 4]. Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    incr=[]
    decr=[]
    
    for i in range(len(L)-1):
        temp_inc=[]
        temp_dec=[]
        temp_inc.append(L[i])
        temp_dec.append(L[i])
        j=i+1
        while (j<len(L) and L[j]>=L[j-1]):
            temp_inc.append(L[j])
            j+=1
            
        j=i+1
        while (j<len(L) and L[j]<=L[j-1]):
            temp_dec.append(L[j])
            j+=1
            
        if len(temp_inc)>len(incr):
            incr=temp_inc
            temp_inc=[]
            
        if len(temp_dec)>len(decr):
            decr=temp_dec
            temp_dec=[]
        
    if len(incr)>len(decr):
        return sum(incr)
    elif len(incr)==len(decr):
        if L.index(incr[0])<L.index(decr[0]):
            return sum(incr)
        else:
            return sum(decr)
    else:
        return sum(decr)


###Problem 5
#15.0/15.0 points (graded)
#In this problem, you will implement a class according to the specifications in the template file usresident.py. The file contains a Person class similar to what you have seen in lecture and a USResident class (a subclass of Person). Person is already implemented for you and you will have to implement two methods of USResident.
#For example, the following code:
#a = USResident('Tim Beaver', 'citizen')
#print(a.getStatus())
#b = USResident('Tim Horton', 'non-resident')
#will print out:
#citizen
### will show that a ValueError was raised at a particular line

class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status != 'citizen' and status != 'legal_resident' and \
            status != 'illegal_resident':
                raise ValueError()
        else:
            self.status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status


###Problem 6-1
#10.0/10.0 points (graded)
#This question has 3 parts
#Consider the following hierarchy of classes:
#class Person(object):     
#    def __init__(self, name):         
#        self.name = name     
#    def say(self, stuff):         
#        return self.name + ' says: ' + stuff     
#    def __str__(self):         
#        return self.name  
#
#class Lecturer(Person):     
#    def lecture(self, stuff):         
#        return 'I believe that ' + Person.say(self, stuff)  
#
#class Professor(Lecturer): 
#    def say(self, stuff): 
#        return self.name + ' says: ' + self.lecture(stuff)
#
#class ArrogantProfessor(Professor): 
#    def say(self, stuff): 
#        return 'It is obvious that ' + self.say(stuff)
#As written, this code leads to an infinite loop when using the Arrogant Professor class.
#
#Change the definition of ArrogantProfessor so that the following behavior is achieved:
#e = Person('eric') 
#le = Lecturer('eric') 
#pe = Professor('eric') 
#ae = ArrogantProfessor('eric')
#
#>>> e.say('the sky is blue')
#eric says: the sky is blue
#
#>>> le.say('the sky is blue')
#eric says: the sky is blue
#
#>>> le.lecture('the sky is blue')
#I believe that eric says: the sky is blue
#
#>>> pe.say('the sky is blue')
#eric says: I believe that eric says: the sky is blue
#
#>>> pe.lecture('the sky is blue')
#I believe that eric says: the sky is blue
#
#>>> ae.say('the sky is blue')
#eric says: It is obvious that eric says: the sky is blue
#
#>>> ae.lecture('the sky is blue')
#It is obvious that eric says: the sky is blue
#Paste ONLY your ArrogantProfessor class in the box below. Do not leave any debugging print statements.

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: '+ self.lecture(stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)
        

#Problem 6-2
#10.0/10.0 points (graded)
#You change your mind, and now want the behavior as described in Part 1, except that you want:
#>>> ae.say('the sky is blue')
#eric says: It is obvious that I believe that eric says: the sky is blue
#>>> ae.lecture('the sky is blue')
#It is obvious that I believe that eric says: the sky is blue
#Change the definition of ArrogantProfessor so that the behavior described above is achieved.
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: '+ self.lecture(stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
        
##Problem 6-3
#15.0/15.0 points (graded)
#You change your mind once more. You want to keep the behavior from Part 2, but now you would like:
#>>> pe.say('the sky is blue')
#Prof. eric says: I believe that eric says: the sky is blue 
#>>> ae.say('the sky is blue')
#Prof. eric says: It is obvious that I believe that eric says: the sky is blue 
#Change the Professor class definition in order to achieve this. You may have to modify your implmentation for a previous part to get this to work.
class Professor(Lecturer): 
    def say(self, stuff): 
        return "Prof. "+ self.name + ' says: ' + self.lecture(stuff)
        

##Problem 7
#20.0/20.0 points (graded)
#Write a function called general_poly, that meets the specifications below.
#For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗10^3+2∗10^2+3∗10^1+4∗10^0
#So in the example the function only takes one argument with general_poly([1, 2, 3, 4]) and it returns a function that you can apply to a value, in this case x = 10 with general_poly([1, 2, 3, 4])(10).
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def f(x):
        total=0
        k=len(L)
        for e in L:
            k-=1
            total+=e*(x**k)
        return total
    return f