def count_vowels(input_string):
    # Convert the string to lower case to handle case insensitivity
    input_string = input_string.lower()
    
    # Define a set of vowels
    vowels = set('aeiou')
    
    # Create a set to store unique vowels found in the input string
    unique_vowels = set()
    
    # Iterate over each character in the input string
    for char in input_string:
        # If the character is a vowel, add it to the unique_vowels set
        if char in vowels:
            unique_vowels.add(char)
    
    # Print the number of unique vowels
    print(len(unique_vowels))

# Test cases
count_vowels("swEet")  # Should print 1
count_vowels("AaaaeeE")  # Should print 2
