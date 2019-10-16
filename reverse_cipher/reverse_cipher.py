# Reverse Cipher 

# https://nostarch.com/crackingcodesresources (BSD Licensed)

# Saving the original message as a string 
message = 'Three can keep a secret, if two of them are dead.'

# Setting up an empty string for our translation 
translated = ''

# Setting our index to be one fewer than the length of the message
i = len(message) - 1

# Loop through the message until there are no more characters 
while i >= 0: 
    # Add the i'th character, which starts at length - 1, to the empty string
    translated = translated + message[i]
    # Decrement i 
    i = i - 1

# Print the translation 
print(translated)
