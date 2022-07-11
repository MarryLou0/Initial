def end_zeros():
    number = input('Insert a number to find how many zeros it has: ')
    reversed_number = number[::-1]
    i = 0
    for x in reversed_number:
        if x == "0":
            i +=1
        else:
            break

    return i


 print(end_zeros())



