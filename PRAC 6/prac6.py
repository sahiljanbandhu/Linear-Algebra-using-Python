"""
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
print("gcd of two numbers is",gcd(a,b))
"""



"""
a=0
b=0
c=0
i=0
n=27
for i in range(a,n-1):
    c=(i*i)-n
    if c>0:
        b=c**0.5
        if i*i-b*b==n:
            print("final_a",i)
            print("final_b",b)
            print("final_n",n)
            break
"""


"""
a=int(input("enter a:"))
b=int(input("enter b:"))
a1=int(input("enter a1:"))
b1=int(input("enter b1:"))
a2=int(input("enter a2:"))
b2=int(input("enter b2:"))
def gcd(a,b):
    (a==a1==a2) & (b==b1==b2)
    if a==0:
        return b
    return gcd(b%a,a)
print("gcd of two number is:",gcd(a,b),gcd(a1,b1),gcd(a2,b2))

"""












    
