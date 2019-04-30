

# print(3, f(3))



def f(x):
    return 5 * x


print(3, f(3))

def f(x):
    """
    THis is the doc of f(x)
    :param x:
    :return:
    """
    return 5 + x

print(3, f(3))

print(f.__doc__)

f.george = 33

print(f.george)

