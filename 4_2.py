sent = input("Enter your sentence: ")
sent = sent.replace(" ", "")
slovar = {i:sent.count(i) for i in sent}
print(slovar)

