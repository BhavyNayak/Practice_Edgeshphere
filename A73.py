# 73. Create a list of prime numbers using list comprehension.
primes=[i for i in range(2,101) if all(i%x!=0 for x in range(2,int(i**0.5)+1))]
print(primes)