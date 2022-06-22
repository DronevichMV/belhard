sent = input("Enter your sentence: ")
sent = sent.replace(" ", "")
spisok = list(sent)
mnozh = set(spisok)
slovar = dict.fromkeys(mnozh, 0)
for mnozh in spisok:
    slovar[mnozh] += 1
print(slovar)

