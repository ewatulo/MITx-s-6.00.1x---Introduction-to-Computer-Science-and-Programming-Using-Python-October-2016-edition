#### Objected Oriented Programming

##Exercise: hand
#5.0/5.0 points (graded)
#In this problem, you'll be asked to read through an object-oriented implementation of the hand from the word game problem of Problem Set 4. You'll then be asked to implement one of its methods. Note that the implementation of the object-oriented version of the hand is a bit different than how we did things with the functional implementation; pay close attention to doc strings and read through the implementation carefully.
#To begin: Download hand.py and read through the file. Be sure to understand what's going on in the file. Make a few instances of the Hand class, and play around with the existing methods.
#When you have completed reading through the file, implement the update method.
#Paste the entire Hand class in the box below.

import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        interim=self.hand.copy()
        for letter in word:
            if letter in interim.keys() and interim[letter]>0:
                interim[letter]-=1
            else:
                return False
        self.hand=interim
        return True

##Exercise: genPrimes
#5.0/5.0 points (graded)
#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
def genPrimes():
    x=2
    next=x
    primeSet=[]
    while True:
        yield next
        primeSet.append(next)
        p=next
        next=next+1
        k=0
        while k<len(primeSet):
            if (next % primeSet[k]) != 0:
                k=k+1
            else:
                next+=1
                k=0
                

######## Problem Set 5 ###################
#Paste your implementation of the Message class in the box below.
#Fill in the build_shift_dict(self, shift)
#Fill in the apply_shift(self, shift) method 
#Paste your implementation of the entire PlaintextMessage class in the box below.
#Paste your implementation of the entire CipertextMessage class in the box below.
import string

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        delta=shift
        letterSet=""
        newDict={}
        for k in string.ascii_lowercase:
            letterSet=letterSet + k
        for k in string.ascii_uppercase:
            letterSet=letterSet + k
        
        for l in letterSet:
            if l.islower():
                newPosition=delta-26+string.ascii_lowercase.index(l)
                newDict[l]=letterSet[newPosition].lower()
            else:
                newPosition=delta-26+string.ascii_uppercase.index(l)
                newDict[l]=letterSet[newPosition].upper()
        
        return newDict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        text=self.get_message_text()
        newText=""
        newAlphabet=self.build_shift_dict(shift)
        
        for s in text:
            if s in (" !@#$%^&*()-_+={}[]|\:;'<>?,./\"") or s in string.digits:
                newText=newText+s
            else:
                newText=newText+newAlphabet[s]
        return newText

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift=shift
        self.encrypting_dict=self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift=shift
        self.encrypting_dict=self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        bestTuple=()
        shift_value=0
        decrypted_text=""
        word_count=0
        wordlist=self.get_valid_words()
        
        for s in range(26):
            count=0
            decr=[]
            shifted_text=self.apply_shift(26-s)
            text_to_words=shifted_text.split(' ')
            for i in text_to_words:
                decr.append(i)
                if is_word(wordlist, i):
                    count+=1
            if count>word_count:
                if s==0:
                    shift_value=0
                else:
                    shift_value=26-s
                word_count=count
                decrypted_text=decr
        
        final_text=""
        for k in decrypted_text:
            final_text=final_text+k+" "
            
        final_text=final_text[:-1]
        
        bestTuple=(shift_value, final_text)
        return bestTuple

###Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.
###Paste your function decrypt_story() in the box below.
def decrypt_story():
        
    story=get_story_string()
    story_object=CiphertextMessage(story)
    return story_object.decrypt_message()

        
        