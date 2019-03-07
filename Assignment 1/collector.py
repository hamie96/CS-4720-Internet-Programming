import math

# Hamilton Bradford
# CS 4720
# Assignment 1
# Written on Pop OS 18.04 (Ubuntu Fork)
# Using Vim and Python 3.6.7


class Collector:

        def __init__(self):
                self.list = []
        
        def count(self):
                return len(self.list)

        def sum(self):
                return sum(self.list)

        def sum_squares(self):
                square = 0
                for i in self.list:
                    square = (i ** 2) + square
                return square

        def average(self):
                return self.sum() / self.count()

        def variance(self):
                variance = 0
                for i in self.list:
                    variance = variance + (( i - self.average() ) ** 2)
                return variance / (len(self.list))

        def standard_deviation(self):
                return math.sqrt(self.variance())
	
        def add(self, x):
                self.list.append(x)

        def weprint(self):
                print(*self.list)


                
