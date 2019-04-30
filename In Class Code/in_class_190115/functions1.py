

def square(x):
    """
    Return the square of the single parameter.
    :param x: A numeric value
    :return: The squre of x
    """
    return x*x

def move(a, d = 10):
    return a + d

x = move(3, 4)
print(x)

y = move(7)
print(y)


def hexd(a = 0, b = 0, c = 0, d = 0):
    return a + 2*b + 4*c + 8*d


x = hexd(3)
print(x)

y = hexd(0,0,0,3)
print(y)

y = hexd(d = 3)
print(y)

y = hexd(1, d = 3)
print(y)
y = hexd(a = 1, d = 3)
print(y)

y = hexd(d = 4, b = 7)
print(y)


def sumx(*args):
    t = 0
    for x in args:
        t += x
    return t

b = [1, 2, 3, 4, 5]

print(sumx(2,3,4))

print(sumx(3, 4, 5, 6, 7, 8, 9, 10))

print(sumx())

print(sumx(*b))









