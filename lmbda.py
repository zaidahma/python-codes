itmes = [
    ("product1", 99),
    ("product2", 12),
    ("product3", 77),

]
itmes.sort(key=lambda item: item[1])
print(itmes)
