itmes = [
    ("product1", 99),
    ("product2", 12),
    ("product3", 77),

]


def s_items(item):
    return item[1]


itmes.sort(key=s_items)
print(itmes)
