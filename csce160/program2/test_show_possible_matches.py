import hangman


def test_show_possible_matches_prints_one_match(capsys):
    hangman.show_possible_matches('t_ _ t', ['test', 'tear'])
    out, _ = capsys.readouterr()
    assert out == 'test \n'


def test_show_possible_matches_prints_two_match(capsys):
    hangman.show_possible_matches('t_ _ t', ['test', 'tear', 'tact'])
    out, _ = capsys.readouterr()
    assert out == 'test tact \n'
