

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

bsq = [x*x for x in b]
print("bsq", bsq)

bsq_even = [x*x for x in b if x % 2 == 0]
print("bsq_even", bsq_even)

prods = [x*y for x in b for y in b]
print("prods", prods)
print("length of prods", len(prods))


