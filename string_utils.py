"""
String utility functions for various text operations.
"""


def reverse_string(text):
    """Reverse a string."""
    return text[::-1]


def is_palindrome(text):
    """Check if a string is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())


def remove_spaces(text):
    """Remove all spaces from a string."""
    return text.replace(" ", "")


def main():
    """Main function to demonstrate string utilities."""
    print("String Utilities Demo")
    print("=" * 40)
    
    test_str = "hello world"
    print(f"Original: {test_str}")
    print(f"Reversed: {reverse_string(test_str)}")
    print(f"Capitalized: {capitalize_words(test_str)}")
    print(f"Vowel count: {count_vowels(test_str)}")
    print(f"Without spaces: {remove_spaces(test_str)}")
    
    palindrome_test = "racecar"
    print(f"\nIs '{palindrome_test}' a palindrome? {is_palindrome(palindrome_test)}")


if __name__ == "__main__":
    main()
