

word = raw_input("Please enter the word to test.")
rev_word = ""
#for c in palinTest:
#    print(c)




for index in range(len(word)-1,-1,-1):  ##What is second -1
    rev_word += word[index]

print(rev_word)

if rev_word.lower() == word.lower():
    print("{0} is a Palindrome!").format(word)

else: print("{0} is not a palindrome!").format(word)


    #if palinTest == palinTest[index]:
        #print(palinTest[index])
    #    print(index)


#print(palinTest[0])
#print(palinTest[1])
#reverse[]

#while index >= 0;
#    reverse.append:(palinTest[index])
#    index -= -1

#print(reverse)
#print(str(reverse))

##THIS WORKS
#palinTest = raw_input("Please enter the word to test.")
#length = len(palinTest)
#index = 0

#while index < len(palinTest) / 2 + 1:
## while 0 is less thant 3(cat) / 2 +1:
    #if palinTest[index].lower() != palinTest[-index - 1].lower():  ##cant get upper case to work
    ##if mom [c] (lowercase) is not equal to cat[t](lowercase):
    #    print "Not Palindrome"
    #    break
    #index += 1
    ##take index = 0 + 1 until it is more than len(palinTest) /2 +1 then run else
#else:
    #print "Palidrome"
####








#pullApart = list(palinTest)
#print(pullApart)


#for test in range(0, len())
