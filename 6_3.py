def offset(n: int, spisok: list) -> list:
    if N > 0:
        for _ in range(N):
            spisok.insert(0, spisok.pop(-1))
    else:
        for _ in range(abs(N)):
            spisok.append(spisok.pop(0))
    return spisok
    print(spisok)






