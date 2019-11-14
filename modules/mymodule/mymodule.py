def count_vowels(sentence:str) -> dict:
    """Return list of vowels foudn in sentence"""
    vowels = set('aeiou')
    vowel_count = {}
    for char in list(sentence):
        if char in vowels:
            vowel_count.setdefault(char, 0)
            vowel_count[char] += 1
    return str(sorted(vowel_count.items()))

def find_common_vowels(sentence:str, letters:str):
    """Find vowels common to both inputs"""
    return set(sentence).intersection(set(letters))

