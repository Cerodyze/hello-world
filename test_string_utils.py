"""
Functional tests for string utility functions.
"""
import pytest
from string_utils import (
    reverse_string,
    is_palindrome,
    count_vowels,
    capitalize_words,
    remove_spaces
)


class TestStringUtils:
    """Test suite for string utility functions."""
    
    def test_reverse_string(self):
        """Test string reversal functionality."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"
        assert reverse_string("12345") == "54321"
    
    def test_is_palindrome(self):
        """Test palindrome detection functionality."""
        assert is_palindrome("racecar") == True
        assert is_palindrome("hello") == False
        assert is_palindrome("A man a plan a canal Panama") == True
        assert is_palindrome("Python") == False
        assert is_palindrome("") == True
        assert is_palindrome("a") == True
    
    def test_count_vowels(self):
        """Test vowel counting functionality."""
        assert count_vowels("hello") == 2
        assert count_vowels("Python") == 1
        assert count_vowels("aeiou") == 5
        assert count_vowels("bcdfg") == 0
        assert count_vowels("") == 0
        assert count_vowels("AEIOU") == 5
    
    def test_capitalize_words(self):
        """Test word capitalization functionality."""
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python programming") == "Python Programming"
        assert capitalize_words("") == ""
        assert capitalize_words("a b c") == "A B C"
        assert capitalize_words("HELLO WORLD") == "Hello World"
    
    def test_remove_spaces(self):
        """Test space removal functionality."""
        assert remove_spaces("hello world") == "helloworld"
        assert remove_spaces("  spaces  ") == "spaces"
        assert remove_spaces("") == ""
        assert remove_spaces("nospaces") == "nospaces"
        assert remove_spaces("a b c d e") == "abcde"
