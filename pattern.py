#pattern
print("Pattern 1:")
n=int(input("Enter the No. of row: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print (j, end=(" "))
    print ("")
print("")

print("Pattern 2:")
n=int(input("Enter the No. of row: "))
for i in range(n+1,1,-1):
    for j in range(1,i):
        print (j, end=(" "))
    print ("")
print("")

print("Pattern 3:")
n=int(input("Enter the No. of row: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print (j, end=(" "))
    print ("")
#print("")
#n=int(input("Enter the No. of row: "))
for i in range(n+1,1,-1):
    for j in range(1,i-1):
        print (j, end=(" "))
    print ("")
print("")

print("Pattern 4:")
n=int(input("Enter the No. of row: "))
for i in range(1, n):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

for i in range(n, 1, -1):
    for j in range(1, i - 1):
        print(j, end=' ')
    print("")
