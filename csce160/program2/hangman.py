'''
hangman.py
Zynab Ali
'''

import random

WORDLIST_FILENAME = "words.txt"
ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
VOWELS = 'aeiou'
MAX_GUESSES = 6
MAX_WARNINGS = 3

# Helper code
def load_words():
    '''
    Returns a list of valid words. Words are strings of lowercase letters.
    '''
    print("\nLoading word list from file...")
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

def is_word_guessed(secret_word, letters_guessed):
    '''
    Determines if all the letters in the secret_word have been guessed.
    Iterates over each letter in the secret_word to check if the letter is
    in letters_guessed. Return True if all letters have been guessed.
    
    secret_word: string, the word the user is guessing;
      assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    This function creates a guessed_word that consists of '_ ' for each letter not
    yet guessed and letters that have been guessed.

    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    s = ''
    for char in secret_word:
        if char in letters_guessed:
            s += f'{char}'
        else:
            s += '_ '
    return s

def get_available_letters(letters_guessed):
    '''
    Returns a list of letters that have not yet been guessed.
    Use the constant ALL_LETTERS and parameter, letters_guessed to determine
    the letters not yet guessed.
    
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_guessed = [x.lower() for x in letters_guessed]
    return ''.join([x for x in ALL_LETTERS if x not in letters_guessed])

def invalid_guess(warnings_remaining, guesses_remaining):
    '''
    Call this function when the user enters a letter already guessed or
    a symbol that is not a letter.
    This function returns new values for warnings and guesses remaining.
    warnings_remaining: int, the warnings remaining before the incorrect guess
    guesses_remaining: int, the guesses remaining before the incorrect guess
    returns: int, int, the number of warnings and guesses remaining after the invalid guess
    '''
    if warnings_remaining <= 0:
        if guesses_remaining <= 0:
            return (warnings_remaining, guesses_remaining)
        return (warnings_remaining, max(guesses_remaining - 1, 0))
    return (max(warnings_remaining - 1, 0), guesses_remaining)

def incorrect_guess(guessed_letter, guesses_remaining):
    '''
    Call this function when the user makes a guess that is valid, but it doesn't
    match a letter in the secret word.
    This function returns a new value for the number of guesses remaining.

    guessed_letter: string, the letter guessed by the player
    guesses_remaining: int, the guesses remaining before the incorrect guess
    returns: int, the number of guesses remaining after incorrect bad guess
    '''
    if guessed_letter in VOWELS:
        return max(guesses_remaining - 2, 0)
    return max(guesses_remaining - 1, 0)

def calculate_score(guesses_remaining, secret_word):
    '''
    Call this function to calculate the user's score at the end of the game.

    guesses_remaining: int, guesses remaining at the conclusion of the game
    secret_word, string, the secret word
    returns: int, the score if guesses_remaining is > 0; otherwise, 0.
    '''
    score = guesses_remaining*len(set(secret_word))
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
    print(f'You have {guesses_remaining} guesses left.')
    print(f'You have {warnings_remaining} warnings left.')
    print(f'Available letters: {available_letters}')
    return input('Enter a letter: ')

def display_game_outcome(score, secret_word):
    '''
    Displays the outcome of the game.
    If the score is greater than 0, display 'Congratulations, you won!'
    and the user's score. Otherwise, display 'Sorry, you ran out of guesses' and
    the secret word.

    score, int, the user's score
    secret_word, string, the secret word
    '''
    if score > 0:
        print('Congratulations, you won!')
        print(f'Your total score for this game is: {score}')
    else:
        print('Sorry, you ran out of guesses.')
        print(f'The word was {secret_word}.')

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    other_word = other_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] == '_':
            continue
        if my_word[i] != other_word[i]:
            return False
    return True

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

    while True:
        if guesses_remaining <= 0:
            break

        letter = prompt_for_letter(guesses_remaining, warnings_remaining, available_letters)[0].lower()
        if letter not in ALL_LETTERS or letter in letters_guessed:
            warnings_remaining, guesses_remaining = invalid_guess(warnings_remaining, guesses_remaining)
        else:
            letters_guessed += letter
            if letter not in secret_word:
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                guesses_remaining = incorrect_guess(letter, guesses_remaining)
            else:
                if is_word_guessed(secret_word, letters_guessed):
                    break
                else:
                    print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        available_letters = get_available_letters(letters_guessed)

    score = calculate_score(guesses_remaining, secret_word)
    display_game_outcome(score, secret_word)

if __name__ == "__main__":
    main()
