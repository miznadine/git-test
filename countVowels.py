
import sys

def count_unique_vowels(input_string):
    vowels = set("aeiouAEIOU")
    unique_vowels = set()
    
    for char in input_string:
        if char in vowels:
            unique_vowels.add(char.lower())
    
    print(len(unique_vowels))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python countVowels.py <input_string>")
    else:
        input_string = sys.argv[1]
        count_unique_vowels(input_string)
