N = int(input("Enter first number: "))
M = int(input("Enter second number: "))
K = int(input("Enter third number: "))

i = K
count = 0
while count < N:
    if not i % M:
        count += 1
        print(i)
    i += 1



