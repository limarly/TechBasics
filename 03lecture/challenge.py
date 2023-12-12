def reverse_string_if_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        reversed_string = input_string[::-1]  # Reverse the string
        print("Reversed string:", reversed_string)
    else:
        print("Original string:", input_string)

# Example usage:
input_string1 = "abcd"  # Length is 4 (multiple of 4)
input_string2 = "hello"  # Length is not a multiple of 4

reverse_string_if_multiple_of_4(input_string1)  # Will print the reversed string
reverse_string_if_multiple_of_4(input_string2)  # Will print the original string

# not the right exercise!!