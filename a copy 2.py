
def zeros(n):
    primes = {0:1}
    def prime(x):
        if x in primes:
            return primes[x]
        primes[x] = x * prime(x-1)
        return primes[x]
    return prime(n)

x = str(zeros(994))
# print(zeros(994))
print(len(x))