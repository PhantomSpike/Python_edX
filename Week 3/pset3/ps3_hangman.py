# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/Users/aleksandar/Desktop/Code/Python_edX/Week 3/pset3/words.txt"

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
#wordlist = loadWords()

#secretWord = 'pressing' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return set(secretWord) <= set(lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word_to_print = str()
    for letter in secretWord:
        if letter in lettersGuessed:
            word_to_print += letter
        else:
            word_to_print += '_ '
    return(word_to_print)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    stringy = list(set(alphabet) - set(lettersGuessed))
    stringy.sort()
    return ''.join(stringy)
    

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
    # FILL IN YOUR CODE HERE...
    word_len = len(secretWord)
    lettersGuessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+ str(word_len) + ' letters long')
    print('-----------')
    guesses_left = 8
    while guesses_left>0:
        print('You have ' + str(guesses_left)+' guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters: '+availableLetters)
        guess = input('Please guess a letter: ').lower()
        if guess in lettersGuessed:
            guessedword = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: " + guessedword)
        else:
            lettersGuessed.append(guess)
            guessedword = getGuessedWord(secretWord, lettersGuessed)
            if guess in secretWord:
                print('Good guess: '+ guessedword)
                if isWordGuessed(secretWord, lettersGuessed):
                    print('-----------')
                    return print('Congratulations, you won!')
            else:
                print('Oops! That letter is not in my word: ' + guessedword)
                guesses_left -= 1
        print('-----------')
    return print('Sorry, you ran out of guesses. The word was ' + secretWord + '.' )
    
            
                
        
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
