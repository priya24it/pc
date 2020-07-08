
for num in range(1,30):
    for i in range(2, num):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")












#test_string = "Geeksforgeeks is best Computer Science Portal"
test_string = "i am a good good girl"


# printing original string
print("The original string is : " + test_string)

# using split()
# to count words in string
res = len(test_string.split())
wordlist = test_string.split()
wordfreq = []
words = {}
#for w in wordlist:

 #   wordfreq.append(wordlist.count(w))
  #  words[w] = [wordlist.count(w)]
# printing result
#print("The number of words in string are : " + str(wordfreq))

#print(words)

#0,1,1,2,3
num1 =0
num2 =1
res = ""

Numbers = ['8','3','2','9','1']
temp = ""
#for i in range(0,len(Numbers)):
    #for j in range(0,len(Numbers)):  #
        #if Numbers[i] < Numbers[j]:
            #temp = Numbers[i]
            #Numbers[i] = Numbers[j]
            #Numbers[j] = temp

#print(Numbers)





#print(num1)
#print(num2)
for i in range(0,1):
    res = num1 + num2
    print(res)
    num1 = num2
    num2  = res



