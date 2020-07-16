# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False
    
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # empty list to store letters guessed
    partGuessed = []
    
    for i in secretWord:
        if i in lettersGuessed:
            partGuessed.append(i)
        else:
            partGuessed.append('_ ')
    
    return ''.join(partGuessed)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # to use all alphabets in lower case by calling string.ascii_lowercase
    import string
    
    # create a list of all alphabets
    avaiLetters = []
    for i in string.ascii_lowercase:
        avaiLetters.append(i)
    
    for i in lettersGuessed:
        if i in avaiLetters:
            avaiLetters.remove(i)
    
    return ''.join(avaiLetters)    

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print(13*'-')
    
    # initialize variable to track chances left
    chancesLeft = 8
    # initialize letters guessed
    lettersGuessed = []
    
    while chancesLeft > 0:
        print('You have', chancesLeft, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        
        # get a guess from user
        letter = input('Please guess a letter: ')
        
        if letter in lettersGuessed:
            print("OOps! You've already guessed that letter:",
                getGuessedWord(secretWord, lettersGuessed))
            
            print(13*'-')
            
        elif letter in secretWord:
            lettersGuessed.append(letter)            
            
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            
            print(13*'-')            
            
            if isWordGuessed(secretWord, lettersGuessed):
                print('Congratulations, you won!')
                return
            
        else:
            lettersGuessed.append(letter)
            
            print('OOps! That letter is not in my word:', 
                  getGuessedWord(secretWord, lettersGuessed))
            chancesLeft -= 1
            
            print(13*'-')
            
            if chancesLeft == 0:
                print('Sorry, you ran out of guesses. The word was',
                      secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
