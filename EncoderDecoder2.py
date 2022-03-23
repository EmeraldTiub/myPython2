message = input("Enter a message to encode or decode: ")
key = eval(input("Enter a key value from 1-26: "))
message = message.lower()
output = ""
for letter in message:
    if letter.islower():
        value = ord(letter) + key
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("Output message: ", output)
