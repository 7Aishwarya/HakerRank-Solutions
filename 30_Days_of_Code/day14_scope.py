'''Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference
instance variable.
'''


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    
    def computeDifference(self):
        maximum = 0
        minimum = 100
        for i in self.__elements:
            a = abs(i)
            if a > maximum:
                maximum = a
            if a < minimum:
                minimum = a
        self.maximumDifference = maximum - minimum



    

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)