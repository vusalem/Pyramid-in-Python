start = 1
row = 5

for r in range(1, row + 1):
    spaces = (row - r) * " "
    print(spaces, end="")

    a = r*2 - 1
    for x in range(1, a + 1):
        print(x, end="")
    print()