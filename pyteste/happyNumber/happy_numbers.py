
def happy(number):
    box = []
    while number != 1 and number not in box:
        box.append(number)
        number = sum([int(i)**2 for i in str(number)])
    return number == 1