N = int(input("Enter first number: "))
M = int(input("Enter second number: "))
K = int(input("Enter third number: "))
for i in range (N+1):
    if not i % M and i > K:
        print(i)


