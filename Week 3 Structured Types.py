# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:03:50 2016

@author: Ewa
"""
### Week 3 Structured Types
#Exercise: odd tuples
#Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    new = ()
    for i in range(0,len(aTup),2):
        new= new + (aTup[i],)
        i=i+2
    return new
    
####
#Exercise: apply to each 1
#Here is the code for a function applyToEach:
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
#Assume that
#testList = [1, -4, 8, -9]
#For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.
#Example Question:
#>>> print testList
#[5, -20, 40, -45]
def absValue(l):
    return abs(l)
applyToEach(testList, absValue)

##Exercise: apply to each 2
def absValue(l):
    return l+1
applyToEach(testList, absValue)

##Exercise: apply to each 3
##  >>> print testList
##  [1, 16, 64, 81]
def absValue(l):
    return l*l
applyToEach(testList, absValue)

####### 6. Dictionaries
#Exercise: how many
#Consider the following sequence of expressions:
#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')
#We want to write some simple procedures that work on dictionaries to return information.
#First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:
#>>> print(how_many(animals))
#6

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total=0
    for num in aDict:
            for i in aDict[num]:
                total=total+1
    return total
  
  
#Exercise: biggest
#Consider the following sequence of expressions:
#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')
#We want to write some simple procedures that work on dictionaries to return information.
#This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.
#Example usage:
#>>> biggest(animals)
#'d'
#If there are no values in the dictionary, biggest should return None.
  
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    temp =0
    keyValue=""
    for num in aDict:
        total=0
        for i in aDict[num]:
                total=total+1
        if total>temp:
            temp=total
            keyValue=num
    return keyValue
    
######### Problem Set 3 ####################################################

#Problem 1 - Is the Word Guessed
#Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
#Example Usage:
#>>> secretWord = 'apple' 
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(isWordGuessed(secretWord, lettersGuessed))
#False
#For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter in lettersGuessed:
            next
        else:
            return False
    return True
    

#Problem 2 - Printing Out the User's Guess
#Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!
#Example Usage:
#>>> secretWord = 'apple' 
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(getGuessedWord(secretWord, lettersGuessed))
#'_ pp_ e'
#When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!
#For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.
#For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=""
    for letter in secretWord:
        if letter in lettersGuessed:
            result=result + letter
        else:
            result= result + '_ '
    return result
    
    
#Problem 3 - Printing Out all Available Letters
#Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
#Example Usage:
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz
#Note that this function should return the letters in alphabetical order, as in the example above.
#For this function, you may assume that all the letters in lettersGuessed are lowercase.
#Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
#>>> import string
#>>> print(string.ascii_lowercase)
#abcdefghijklmnopqrstuvwxyz
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    left =""
    for letter in string.ascii_lowercase:
        if not letter in lettersGuessed:
            left=left+letter
    return left
    

#Problem 4 - The Game
#Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
#Hints:
#You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.
#Consider using lower() to convert user input to lower case. For example:
#guess = 'A'
#guessInLowerCase = guess.lower()
#Consider writing additional helper functions if you need them!
#There are four important pieces of information you may wish to store:
#secretWord: The word to guess.
#lettersGuessed: The letters that have been guessed so far.
#mistakesMade: The number of incorrect guesses made so far.
#availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''    
    secretWord=str(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord)  ,"letters long.")
    

    mistakesMade=0
    lettersGuessed=''
    while mistakesMade<8:
        print("-------------")
        print("You have", 8-mistakesMade ,"guesses left.")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        availableLetters = getAvailableLetters(lettersGuessed)
        guessLetter=str(input("Please guess a letter: "))
        
        if guessLetter in availableLetters:
                if guessLetter in secretWord:
                    lettersGuessed=lettersGuessed + guessLetter
                    print("Good guess:", getGuessedWord(secretWord, lettersGuessed))                    
                    if isWordGuessed(secretWord, lettersGuessed):
                        print('------------')
                        print('Congratulations, you won!')
                        break
                else:
                    lettersGuessed=lettersGuessed + guessLetter
                    print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                    mistakesMade=mistakesMade+1
        else:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

        if mistakesMade==8:
                print('------------')
                print('Sorry, you ran out of guesses. The word was', secretWord + '.')
    
    