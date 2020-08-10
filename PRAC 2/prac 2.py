"""
x=[[3,5],[6,4],[1,2]]
print(x)
"""



"""
x=[[9,6,1],[9,6,4],[6,6,7]]
y=[[7,5,0],[4,6,1],[4,5,3]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[j][k]
for r in result:
    print(r)
"""



"""

x=[[3,5],[6,4],[1,2]]
result=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]= x[i][j]
for r in result:
    print(r)

"""
