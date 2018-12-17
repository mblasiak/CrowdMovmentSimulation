def print_2D_list_difrances(list_1: [[]], list_2: [[]]):
    if len(list_1) != len(list_2):
        print("List row(s)")
        return
    for x in range(0, len(list_1)):
        if len(list_1[x]) != len(list_2[x]):
            print("List column(s) not equal")

        for y in range(0, len(list_1[0])):
            if list_1[x][y] != list_2[x][y]:
                print("Position of miss match : {} {}".format(x, y))
                print("Excpected value {}  given value {}".format(list_1[x][y], list_2[x][y]))
