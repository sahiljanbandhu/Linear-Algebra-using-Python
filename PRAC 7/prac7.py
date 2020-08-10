def row_mult(row, num):
  return [x * num for x in row]
def row_sub(row_left, row_right):
  return [a - b for (a, b) in zip(row_left, row_right)]
def row_echlon(mtx): 
  temp_mtx = list(mtx)

  def echelonify(rw, col):
    for i,row in enumerate(temp_mtx[(col+1):]):
      i += 1
      if rw[col] == 0: continue
      temp_mtx[i+col] = row_sub(row, row_mult(rw, row[col] / rw[col]))      

  for i in range(len(mtx)):
    active_row = temp_mtx[i]
    echelonify(active_row, i)
  temp_mtx = [
    
    [(0 if (0.0000000001 > x > -0.0000000001) else x) 
      for x in row] 
    for row in temp_mtx
  ]

  return temp_mtx
print("enter dimension of matrix:")
r=int(input("enter no rows: "))
c=int(input("enter no cols: "))
mtx=[]
for i in range(r):
  mtx.append([])
  print("enter elements of row: ",i)
  for j in range(c):
    n=float(int(input("enter elements: ")))
    mtx[i].append(n)
    print("entered matrix: ")
    for row in mtx:
      print (' '.join(("{0:.2f}".format(x) for x in row)))
      mtx_result=row_echlon(mtx)
print("Row Echlon from matrix: ")
for row in mtx_result:
  print (' '.join(("{0:.2f}".format(x) for x in row)))

