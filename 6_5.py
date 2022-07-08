def rev(spisok: list) -> list:
    for i in range(len(spisok) // 2):
        j = (i + 1) * -1
        spisok[i], spisok[j] = spisok[j], spisok[i]
    return spisok

