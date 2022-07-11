def max_digit():
    number = input("Insert a number to find its biggest digit: ")
    ch = number[0]
    for x in number:
        if x > ch:
            ch = x
        elif x == 9:
            break
        else:
            pass
    return ch

print(max_digit())

