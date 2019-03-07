import collector as coll

# Hamilton Bradford
# This is my test file

x = coll.Collector()
x.add(5)
x.add(10)
print("Total amount of numbers in the list: ", x.count())
print("Sum is ", x.sum())
print("Sum of the squares is ", x.sum_squares())
print("The mean is ", x.average())
print("The variance is ", x.variance())
print("The standard deviation is ", x.standard_deviation())
print("The numbers in the list are: ")
x.weprint()


