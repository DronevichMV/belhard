def spisok_strok(spisok: list) -> list:
    spisok = list(filter(lambda x: isinstance(x, str), spisok))
    return spisok
