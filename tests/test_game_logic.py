from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_guess_too_high_regression():
    # Regression: before the fix, 60 vs 50 returned "Too Low" with a "Go HIGHER!" hint
    result = check_guess(60, 50)
    assert result == "Too High"
    assert result != "Too Low"


def test_guess_with_string_secret():
    # App passes secret as str on even attempts; comparison should still work
    assert check_guess(60, "50") == "Too High"
    assert check_guess(40, "50") == "Too Low"
    assert check_guess(50, "50") == "Win"


def test_parse_guess_valid_number():
    ok, value, err = parse_guess("50")
    assert ok is True
    assert value == 50
    assert err is None


def test_parse_guess_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_invalid_input():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_enter_submission_regression():
    # Regression: pressing Enter submits the form; valid input must parse correctly
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None
