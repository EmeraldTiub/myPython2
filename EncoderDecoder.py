message = input("Enter a message to encode or decode: ")
message = message.lower()
output = ""
for letter in message:
    if letter.islower():
        value = ord(letter) + 13
        letter = chr(value)
        if not letter.islower():
            value -= 26
            letter = chr(value)
    output += letter
print("Output message: ", output)
