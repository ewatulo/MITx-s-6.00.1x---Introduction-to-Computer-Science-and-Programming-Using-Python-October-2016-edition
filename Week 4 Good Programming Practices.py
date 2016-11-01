######## Week 4 Good Programming Practices
#Exercise: integer division
#Consider the following function definition:
#def integerDivision(x, a):
#    """
#    x: a non-negative integer argument
#    a: a positive integer argument
#
#    returns: integer, the integer division of x divided by a.
#    """
#    while x >= a:
#        count += 1
#        x = x - a
#    return count
#When we call
#print(integerDivision(5, 3))
#we get the following error message:
#File "temp.py", line 9, in integerDivision
#    count += 1
#UnboundLocalError: local variable 'count' referenced before assignment
#Your task is to modify the code for integerDivision so that this error does not occur.
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count=0
    while x >= a:
        count += 1
        x = x - a
    return count

#####
#Exercise: simple divide
#ESTIMATED TIME TO COMPLETE: 4 minutes
#Suppose we rewrite the FancyDivide function to use a helper function.
#def fancy_divide(list_of_numbers, index):
#   denom = list_of_numbers[index]
#   return [simple_divide(item, denom) for item in list_of_numbers]
#
#
#def simple_divide(item, denom):
#   return item / denom 
#
#This code raises a ZeroDivisionError exception for the following call: fancy_divide([0, 2, 4], 0)
#Your task is to change the definition of simple_divide so that the call does not raise an exception. When dividing by 0, fancy_divide should return a list with all 0 elements. Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.
def simple_divide(item, denom):
   try:  
       return item / denom
   except ZeroDivisionError:
       return 0
       

########## Problem Set 4 ######################
#In this problem set, you'll implement two versions of a wordgame!
#Don't be intimidated by the length of this problem set. There is a lot of reading, but it can be done with a reasonable amount of thinking and coding. It'll be helpful if you start this problem set a few days before it is due!
#Let's begin by describing the 6.00 wordgame: This game is a lot like Scrabble or Words With Friends, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.
#The rules of the game are as follows:
#Dealing
#A player is dealt a hand of n letters chosen at random (assume n=7 for now).
#The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
#Some letters may remain unused (these won't be scored).
#Scoring
#The score for the hand is the sum of the scores for each word formed.
#The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
#Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.
#For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
#As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

###Problem 1 - Word Scores
#The first step is to implement some code that allows us to calculate the score for a single word. The function getWordScore should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score=0
    for letter in word:
        score=score + SCRABBLE_LETTER_VALUES[letter]
    if len(word)<n:
        score=score*len(word)
    else:
        score=score*len(word) + 50
    return score

##Problem 2 - Dealing with Hands
#A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters. For example, the player could start out with the following hand: a, q, l, m, u, i, l. In our program, a hand will be represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand. For example, the above hand would be represented as:
#hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}    
#Notice how the repeated letter 'l' is represented. Remember that with a dictionary, the usual way to access a value is hand['a'], where 'a' is the key we want to find. However, this only works if the key is in the dictionary; otherwise, we get a KeyError. To avoid this, we can use the call hand.get('a',0). This is the "safe" way to access a value if we are not sure the key is in the dictionary. d.get(key,default) returns the value for key if key is in the dictionary d, else default. If default is not given, it returns None, so that this method never raises a KeyError. For example:
#>>> hand['e']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'e'
#>>> hand.get('e', 0)
#0
#
#REMOVING LETTERS FROM A HAND (YOU IMPLEMENT THIS)
#The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up. For example, the player could start out with the following hand: a, q, l, m, u, i, l. The player could choose to spell the word quail . This would leave the following letters in the player's hand: l, m. Your task is to implement the function updateHand, which takes in two inputs - a hand and a word (string). updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, containing only the letters remaining. For example:
#>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
#>>> displayHand(hand) # Implemented for you
#a q l l m u i
#>>> hand = updateHand(hand, 'quail') # You implement this function!
#>>> hand
#{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
#>>> displayHand(hand)
#l m  
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handLetters = hand.copy()
    for letter in word:
        handLetters[letter]-=1
    return handLetters
    
##Problem 3 - Valid Words
#At this point, we have written code to generate a random hand and display that hand to the user. We can also ask the user for a word (Python's input) and score the word (using your getWordScore). However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the isValidWord function.
#Testing: Make sure the test_isValidWord tests pass. In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be? Additionally, the empty string ('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    assert word != (""), ('Not valid input')
        
    wordDict=getFrequencyDict(word)
    if word in wordList:
        for letter in word:
            if letter in hand and hand.get(letter, 0)>=wordDict[letter]:
                next
            else:
                return False
                break
        return True
    else:
        return False

##Problem 4 - Hand Length
#We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handCount=0
    for letter in hand:
        handCount=handCount + hand[letter]        
    return handCount
    
##Problem 5 - Playing a Hand
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
        # Keep track of the total score
    totalScore=0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand)>0:
        # Display the hand
        print('Current Hand:',end=" ")
        displayHand(hand)
        # Ask user for input
        userInput=str(input('Enter word, or a "." to indicate that you are finished: '))
        # If the input is a single period:
        if userInput=='.':
            # End the game (break out of the loop)
            print('Goodbye! Total score:', totalScore ,'points.')            
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(userInput, hand, wordList):            
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print()
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalScore=totalScore + getWordScore(userInput, n)
                print('"'+ userInput +'"', 'earned', getWordScore(userInput, n) ,'points. Total:', totalScore ,'points')
                print()
                # Update the hand 
                hand=updateHand(hand, userInput)

        # Game is over (user entered a '.' or ran out of letters), so tell user the total score
        if calculateHandlen(hand)==0:
            print('Run out of letters. Total score:', totalScore, 'points.')



###Problem 6 - Playing a Game
#A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Write the code that implements the playGame function.
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    hand=''
    while True:
        choice=str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game:'))
        if choice=='n':
            hand=dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif choice=='r':
            if len(hand)==0:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif choice=='e':
            break
        else:
            print('Invalid command.')


##Problem 7 - You and your Computer
#Now that your computer can choose a word, you need to give the computer the option to play. Write the code that re-implements the playGame function. You will modify the function to behave as described below in the function's comments. As before, you should use the HAND_SIZE constant to determine the number of cards in a hand. Be sure to try out different values for HAND_SIZE with your program.

import time
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand=''
    while True:
        choice=str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game:'))
        if choice=='n':
            userChoice=''
            while userChoice.lower() not in ('u', 'c'):
                userChoice=str(input('Enter u to have yourself play, c to have the computer play:'))
                if userChoice=='u':
                    hand=dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    
                elif userChoice=='c':
                    hand=dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    
                else:
                    print('Invalid command.')   
        elif choice=='r':
            if len(hand)==0:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                userChoice=''
                while userChoice.lower() not in ('u', 'c'):
                    userChoice=str(input('Enter u to have yourself play, c to have the computer play:'))
                    if userChoice=='u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    elif userChoice=='c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print('Invalid command.')
        elif choice=='e':
            break
        else:
            print('Invalid command.')

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')
