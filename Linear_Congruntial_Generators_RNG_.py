
if __name__ == '__main__':
    variable = []

    seed = 7
    a=5
    c=3
    m = 16
    times = 20

    while (times != 0):

        val = (a*seed + c)%m

        u = val/m

        variable.append(u)

        print(val)

        seed = val

        times = times - 1

    print("Random Numbers :",variable)