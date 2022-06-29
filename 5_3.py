N = int(input("Enter last number: "))

count = 0
for i in range (2, N+1, 2):
    if count < 5:
        print(i, end=" ")
        count += 1
    else:
        print()
        print(i, end=" ")
        count = 1
