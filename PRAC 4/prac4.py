"""
a=[[1,2,3],[4,5,6],[7,8,4]]
u=int(input("enter a scalar:"))
for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j]=u*a[i][j]
print("A matrix multiplication by scalar is:",a)
"""



"""
m=[[1,2,3],[4,5,6],[7,8,9]]
n=[[1,2,3,4],[4,5,6,5],[7,8,9,2]]
r=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(m)):
    for j in range(len(n[0])):
        for k in range(len(n)):
            r[i][j]+=m[i][k] * n[k][j]
print("matrix of m is:",m)
print("matrix of n is",n)
print("product of two matrix is:",r)
"""                
