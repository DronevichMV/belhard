slovar_1 = {'name':input("Enter your name: "), 'email':input("Enter your email: ")}
n = int(input("Enter last number: "))
slovar_2 = {i:slovar_1 for i in range(0, n, 1)}
print(slovar_2)

