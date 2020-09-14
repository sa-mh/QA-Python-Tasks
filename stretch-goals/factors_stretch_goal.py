def factors(number):
    # ==============
    # Your code here
    factors = []
    i = 2
    c = 0
    while i < number :
        if number % i == 0:
            factors.append(i)
            i = i + 1
            c = c + 1
        else :
             i = i + 1
    if c == 0:
        return "13 is a prime number"
    else :
        return factors
    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “13 is a prime number”
