def calculator(a, b, operator):
    # ==============
    #
    if operator == "+" :
        return a + b
    elif operator == "-" :
        return a - b
    elif operator == "*" :
        return a * b
    elif operator == "/" :
        return a / b
    else :
        return "invalid operator"

    # ==============

print(calculator(2, 4, "+")) # Should print 6 to the console
print(calculator(10, 3, "-")) # Should print 7 to the console
print(calculator(4, 7, "*")) # Should print 28 to the console
print(calculator(100, 2, "/")) # Should print 50 to the console
