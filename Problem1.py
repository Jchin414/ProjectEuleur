#If we list all the natural numbers
#below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 or 5 below 1000.
#1/17/2022 7:15-7:45

def calculation():#calculation function 
	answer = sum(x for x in range(1000) #the answer will equal the sum of all numbers in the range to 1000
        if (x % 3 == 0 or x % 5 == 0)) #if the numbers are equally divisible by 3 or 5
	return str(answer) #returns answer 

if __name__ == "__main__": #if name eq eq main funcition 
	print(calculation()) #prints the whole calcualtion






































