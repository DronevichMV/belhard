message = input("message: ")
key = input("key: ")

if len(message) != len(key):
    raise ValueError("len of message and key must be equal")

message_bin = ""
key_bin = ""
for i in range(len(key)):
    char = bin(ord(message[i]))[2:]
    char = "0" * (8 - len(char)) + char
    message_bin += char
    char = bin(ord(key[i]))[2:]
    char = "0" * (8 - len(char)) + char
    key_bin += char
result = ""
for i in range(len(key_bin)):
    if message_bin[i] != key_bin[i]:
        result += "1"
    else:
        result += "0"

print(result)







