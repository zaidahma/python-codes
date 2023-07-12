message = "hellow world "


def d(name):
    global message
    message = "b"


print(d("mosh"))
print(message)
