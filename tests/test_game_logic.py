import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_guess_valid_integer_string():
    ok, guess, err = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert err is None


def test_parse_guess_empty_string():
    ok, guess, err = parse_guess("")
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."


def test_parse_guess_non_numeric_text():
    ok, guess, err = parse_guess("hello")
    assert ok is False
    assert guess is None
    assert err == "That is not a number."


def test_parse_guess_decimal_input_should_be_rejected():
    """
    Known bug expectation: decimal guesses should not be accepted as valid integer guesses.
    """
    ok, guess, err = parse_guess("12.9")
    assert ok is False
    assert guess is None
    assert err == "That is not a number."
