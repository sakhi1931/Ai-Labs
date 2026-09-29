def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.
    
    Ignores spaces and capitalization.
    """
    cleaned = ''.join(e.lower() for e in s if e.isalnum())
    return cleaned == cleaned[::-1]

def count_words(text: str) -> int:
    """
    Count the total number of words in a text string.
    """
    return len(text.split())

def celsius_to_fahrenheit(c: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (c * 9/5) + 32