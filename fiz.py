def fizz_buzz(input):
    if input % 3 == 0:
        return "fizz buzz"
    if input % 5 == 0:
        return "buzz "
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizz buzz "
    return input


print(fizz_buzz(15))
