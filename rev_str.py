# Take input from user
original_string = input("Enter a string: ")

# Initialize an empty string to store reversed characters
reversed_string = ""

# Loop through each character and prepend it to the new string
for char in original_string:
    reversed_string = char + reversed_string

# Display the results
print("Original string:", original_string)
print("Reversed string:", reversed_string)
