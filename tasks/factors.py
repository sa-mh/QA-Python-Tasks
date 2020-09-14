def factors(number):
    # ==============
    # Your code here
    factors = []
    i = 2
    while i < number :
        if number % i == 0:
            factors.append(i)
            i = i + 1
        else :
             i = i + 1
    return factors
    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “[]” (an empty list) to the console
