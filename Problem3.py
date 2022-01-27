#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 

number = 600851475143 #number 
i = 2 #sets the first prime number 
while i * i < number: #determines the factors 
    while number % i == 0: #determines whether number is divisible by the factor
        number = number/i #sets number divisible by new factor 
    i = i + 1 # increasing next factor

print(number) #print answer 




    