def number():
    smallest = None
    print("Before:", smallest)
    for itervar in [3, 41, 12, 9, 74, 15]:
        if smallest is None or itervar < smallest:
            smallest = itervar
        print("Loop:", itervar, smallest)
    print("Smallest:", smallest)

def number2():
    small = None
    print("Após:", small)
    for intervalo in [4, 12, 55, 33, 66, 101]:
        if small is None or small < intervalo:
            small = intervalo
        print(intervalo, small)
number2()
