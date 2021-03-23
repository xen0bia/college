import hangman


def test_when_words_are_same_length():
    assert hangman.match_with_gaps('w_ _ d', 'word')


def test_when_words_are_not_same_length():
    assert not hangman.match_with_gaps('w_ _ d', 'words')


def test_when_other_word_has_leading_and_trailing_spaces():
    assert hangman.match_with_gaps('w_ _ d', '  word  ')


def test_when_length_same_but_words_dont_match():
    assert not hangman.match_with_gaps('lea_ y', 'leafs')
