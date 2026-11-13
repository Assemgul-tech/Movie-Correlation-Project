def count_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in text if char in vowels)

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return text.lower() == text.lower()[::-1]

def capitalize_string(text):
    return ' '.join(word.capitalize() for word in text.split())
