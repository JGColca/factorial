
def factorial():
    number = int(input("Please enter a number: "))
    total = 1
    while number > 1:
        total *= number
        number = (number - 1)
    return total
print(factorial())
