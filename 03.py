# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

print([div for div in [i for i in range(3, int(600851475143 ** 0.5), 2) if 600851475143 % i == 0] if all(div % i != 0 for i in range(3, int(div ** 0.5), 2) if i != div)][-1])
