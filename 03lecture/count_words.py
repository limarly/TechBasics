def count_words(input_string):
    # Split the input string into words using whitespace as the separator
    words = input_string.split()
    # Return the number of words in the list
    return len(words)

# Example usage:
input_string = "This is a sample string with eight words."
word_count = count_words(input_string)
print("Number of words:", word_count)


