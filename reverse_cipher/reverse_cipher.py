# Reverse Cipher 

# https://nostarch.com/crackingcodesresources (BSD Licensed)

# Asking our user for an input message
message = input("Hello! Enter a spooky, secret message you'd like to encrypt: ")

# Setting up an empty string for our translation 
translated = ''

# Setting our index to start at the last character in the string 
## We do this by setting it to the length of the string minus one 
### Minus one because computer science counting starts at zero 
i = len(message) - 1

# Loop through the message until there are no more characters 
## While our index is greater than or equal to zero 
### Zero would be the first letter in the string 
#### Note: comparison values also evaluate to a Boolean! 
while i >= 0: 
    # Add the i'th character, which starts at length - 1, to the empty string
    translated = translated + message[i]

    # Uncomment the below code to see the iteration in action 
    # print('i is', i, ', message[i] is ', message[i], ', translated message is:', translated)

    # Decrement i 
    i = i - 1

# Print the translation 
print(translated)
