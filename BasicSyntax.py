#identation

num = 10
if num>0:
    print("Positive")
elif num<0:
    print("Negative")

#The above program can also be written as:

num = 10
if num>0:
 print("Positive")
elif num<0:
 print("Negative")

#Both the program produces same output:

'''Note - The number of space(s) to give before the statement, is up to you/programmer, but the statement needs to be in its same block of code.

The program given below produces error:'''
num = 10
if num>0:
    print("Positive")
elif num<0:
print("Negative")

#The error produces by above Python program is only due to its indentation

#The following program also produces indentation error:

num = 10
if num>10:
    print("Positive")
        print("The value is", num)

#The above program should be structured in this way:

num = 10
if num>0:
    print("Positive")
    print("The value is", num)
    
#You can copy the code one by one and run it to understand better 

