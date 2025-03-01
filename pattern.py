#print the pattern of numberof rows and column
#Rows=2, column=3
#1,2,3
#1,2,3

n=int(input("Enter the number of rows"))
m=int(input("Enhter the number of column"))

for currentrow in range(n):
    for currentnum in range(m):
        print(currentnum+1,end=" ")
    print(" ")
    
