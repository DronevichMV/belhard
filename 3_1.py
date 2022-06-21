sent = input("Enter your sentence: ")
result = sent.replace(" ", "-")
print(result)

result = sent.split(" ")
result = "-".join(result)
print(result)



