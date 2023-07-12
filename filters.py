items = [
    ("product1", 88),
    ("procuct2", 44),
    ("product3", 11),

]
filtered = list(filter(lambda item: item[1] >= 44, items))
print(filtered)
