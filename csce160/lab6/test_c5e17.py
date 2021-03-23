'''
Unit tests for is_prime function
'''
import pytest
import c5e17

@pytest.mark.parametrize("number, expected",
    [(11, True), (9, False), (15, False), (21, False), (31, True), (2, True)])
def test_prime(number, expected):
    '''
    This is a parameterized unit test. This unit test gets executed
    for each pair of values defined in the parametrize annotation
    the preceeds the function header definition.
    '''
    assert c5e17.is_prime(number) == expected
