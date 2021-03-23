'''
hangman.py
Zynab Ali
'''

import random

# -----------------------------------
# global constants
WORDLIST_FILENAME = "words.txt"
ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
VOWELS = 'aeiou'
MAX_GUESSES = 6
MAX_WARNINGS = 3
# end of global constants
# -----------------------------------

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)


def load_words():
    '''
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    word_file = open(WORDLIST_FILENAME, 'r')
    line = word_file.readline()
    word_file.close()

    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return tuple(wordlist)


def choose_word(wordlist):
    '''
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    '''
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing;
      assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def invalid_guess(warnings_remaining, guesses_remaining):
    '''
    Call this function when the user enters a letter already guessed or
    a symbol that is not a letter.
    This function returns new values for warnings and guesses remaining.
    warnings_remaining: int, the warnings remainin before the incorrect guess
    guesses_remaining: int, the guesses remaining before the incorrect guess
    returns: int, int, the number of warnings and guesses remaining after the invalid guess
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def incorrect_guess(guessed_letter, guesses_remaining):
    '''
    Call this function when the user makes a guess that is valid, but it doesn't
    match a letter in the secret word.
    This function returns a new value for the number of guesses remaining.

    guessed_letter: string, the letter guessed by the player
    guesses_remaining: int, the guesses remaining before the incorrect guess
    returns: int, the number of guesses remaining after incorrect bad guess
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def calculate_score(guesses_remaining, secret_word):
    '''
    Call this function to calculate the user's score at the end of the game.

    guesses_remaining: int, guesses remaining at the conclusion of the game
    secret_word, string, the secret word
    returns: int, the score if guesses_remaining is > 0; otherwise, 0.
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    score = guesses_remaining*len(secret_word)
    return score
    #Re:need to count the letters w/o counting the duplicates!!


def prompt_for_letter(guesses_remaining, warnings_remaining, available_letters):
    '''
    Prompt the user to enter an available letter. Converts the letter to lowercase
    before returning it.

    guesses_remaining: int, guesses remaining
    warnings_remaining, int, warnings remaining
    available_letters, string, available letters for the user to choose from.
    returns: string, lowercased letter input by the user
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def display_game_outcome(score, secret_word):
    '''
    Displays the outcome of the game.
    If the score is greater than 0, display 'Congratulations, you won!'
    and the user's score. Otherwise, display 'Sorry, you ran out of guesses' and
    the secret word.

    score, int, the user's score
    secret_word, string, the secret word
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # TODO FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def main():
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the secret word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follow the other limitations detailed in the problem write-up.
    '''
    # load the words into a list
    wordlist = load_words()

    guesses_remaining = MAX_GUESSES
    warnings_remaining = MAX_WARNINGS

    # choose a word from the word list
    secret_word = choose_word(wordlist)

    # used to keep track of letters guessed
    letters_guessed = ''

    # available letters (not yet guessed) for the player to choose from
    available_letters = get_available_letters(letters_guessed)

    # The guessed_word contains '_ ' for each letter not guessed.
    # Initially, none of the letters will be guessed, so the guessed_word
    # will contain '_' for every character after the following line
    # executes.
    guessed_word = get_guessed_word(secret_word, letters_guessed)

    print("\nLet's play:", guessed_word)

    # ############################################################
    # TODO Complete the mainline processing in this main function
    # Hint: The part you have to complete will be in a while loop
    # ############################################################

    score = calculate_score(guesses_remaining, secret_word)
    display_game_outcome(score, secret_word)


# -----------------------------------------
# Call the main function to start the game
# -----------------------------------------
if __name__ == "__main__":
    main()
