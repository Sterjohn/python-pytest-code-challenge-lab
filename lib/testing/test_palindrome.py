import pytest
from palindrome import longest_palindromic_substring

def test_basic_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

def test_basic_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_characters_no_palindrome():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]

def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"

def test_palindrome_in_middle():
    assert longest_palindromic_substring("abcbad") == "abcba"

def test_long_string():
    result = longest_palindromic_substring("a" * 1000)
    assert result == "a" * 1000

def test_numbers_in_string():
    assert longest_palindromic_substring("12321") == "12321"