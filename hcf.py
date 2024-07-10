import math
def hcf(a,b):
    return math.gcd(a,b)
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print("The HCF of ", n1, "and", n2,"is: ",hcf(n1,n2))