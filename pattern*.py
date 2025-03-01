#print the pattern like
#  *
# **
#***

num=int(input("Enter the number"))

for currentrow in range(num):
    for currentnum in range(num):
        if(currentrow < num-(currentnum+1)):
            print(" ",end=" ")
        else:
            print("*",end="")
    print("")
