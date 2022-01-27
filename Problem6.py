# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

startnum = 100 #starting number 
summation = sum(i for i in range(1, startnum + 1)) #adds all the numbers between 1 and n + 1
summation2 = sum(i**2 for i in range(1, startnum + 1)) #add all the squares of the numbers between 1 and n + 1 
print (summation2**2 - summation2) #prints answer 













