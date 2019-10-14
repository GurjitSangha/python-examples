"""
Question:
To print all primes smaller than or equal to n using Sieve of Eratosthenes

Time Complexity: O(n*log(log(n)))
"""


def SieveOfEratosthenes(n):
    #we create a boolean array for all numbers less than or equal to n, and operate on them.
    prime = [True for i in range(n+1)]
    #initialise p to smallest prime number
    p = 2
    while (p * p <= n):   
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True):  
            #We now update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        #increment p
        p += 1
    #loop to print all prime numbers 
    for p in range(2, n+1): 
        if prime[p]: 
            print(p) 
  
#Calling the Function
SieveOfEratosthenes(50)
