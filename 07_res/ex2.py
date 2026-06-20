"""


    1
    2   2
    3   3   3
    2   2
    1

"""


def ex(n:int):
    if n < 1:
        print("impossivel")
        return

    for i in range(1,n+1):
        print(f"{i:2} " * i)


ex(15)


def ex2(n:int):
    if n < 1:
        print("impossivel")
        return

    for i in range(1,n+1):
        for j in range(i):
           print(f"{i} ", end="")

        print()


ex2(3)


"""

    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
    

"""

print("------------")

def ex3(n:int):
    if n < 1:
        print("impossivel")
        return

    for i in range(1,n+1):
        for j in range(1, i+1):
           print(f"{j} ", end="")

        print()


ex3(5)