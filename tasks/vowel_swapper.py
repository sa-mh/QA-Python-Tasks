def vowel_swapper(string):
    # ==============
    # Your code here
    length = len(string)
    strng = list(string)
    temp = ""
    i = 0
    while i != length :
        if strng[i] == "a" or strng[i] == "A":
            strng[i]= "4"
            i = i + 1
           # print(i)
        elif strng[i] == "e" or strng[i] == "E":
            strng[i]= "3"
            i = i + 1
           # print(i)
        elif strng[i] == "i" or strng[i] == "I":
            strng[i]= "!"
            i = i + 1
           # print(i)
        elif strng[i] == "o":
            strng[i]= "ooo"
            i = i + 1
           # print(i)
        elif strng[i] == "O" :
            strng[i]= "000"
            i = i + 1
           # print(i)
        elif strng[i] == "u" or strng[i] == "U":
            strng[i]= "|_|"
            i = i + 1
            #print(i)
        else :
            i = i + 1
           # print(i)
    return temp.join(strng)
    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console
