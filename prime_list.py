#Display all the prime numbers between 1 to 250.
#Store the results in a results.txt file.

#Function to check if the number is prime:
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#Adds the prime number to a list:
primeList = []
for i in range(1, 251):
    if is_prime(i):
        primeList.append(i)
        
#created a .txt file and add the numbers to it:

f = open('PrimeResults.txt', 'w')
for prime in primeList:
    f.write(str(prime) + '\n')
f.close()