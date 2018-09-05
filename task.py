"""
Write a class in which its one method accepts a string from console and 
another method to print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

"""


if __name__ == "__main__":
    pass
    
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# input: 'This is mE 123'

# output: 'tHIS IS Me 123'

string = "This is mE 123"
print(string.swapcase())  



# If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d

# Then, the output of the program should be:

# Helloworld

class Check:


    def __init__(self):
        self.text = ""

    def inputString(self):
        self.text = input("Enter the String:")

    def checkString(self):
        e = []
        a = self.text
        l = len(a)
        # print(l)
        b = list(a)
        # print(b)
        for x in range(0,l,2):
            e.append(b[x])


        z = "".join(str(x) for x in e)
        print(z)

p =  Check()
p.inputString()
p.checkString()


# The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# Input:

# ABCDCDC

# CDC

# Output:2

string = "ABCDCDC"
substring = "CDC"


count = 0
for i, x in enumerate(string):
    if x == 'C':
        if string[i:i+3] == substring:
            count += 1

print(count)
