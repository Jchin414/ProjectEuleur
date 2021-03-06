# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, 
# the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci
# sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
#1/17/2022 7:15-7:45

	
if __name__ == "__main__": #main definition
	answer = 0 #initial answer = 0 
	x = 1  # first integer 
	y = 2  # second integer
	while x <= 4000000: #setting limit 
		if x % 2 == 0: #if number is even 
			answer += x # adds all values
		x, y = y, x + y #sets all values to the next value in the sequence 
	
print(answer) # prints answer 