# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?
#1/18/22 10:00-11:30


import math

answer = 1 #initializes answer 
for i in range(1, 21): #loops through the values 1 through 21
	answer *= i // math.gcd(i, answer)# the next smallest number that is equally divisible by the greatest common divisor
print(answer) #prints answer 
