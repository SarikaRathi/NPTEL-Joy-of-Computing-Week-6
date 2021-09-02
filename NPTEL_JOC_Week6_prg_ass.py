
# Week 6: Programming Assignment 1 - Matrix
# Due on 2021-09-09, 23:59 IST
# Given two integers r and c, indicating the number of rows and columns, print a two-dimensional matrix such that the elements of the matrix are in an increasing sequence from 1 to rXc, in a row-major order.
# Input Format:
# First line of the input contains two space separated integers indicating the rows and columns
# Output Format:
# Display r lines indicating the elements of the Matrix
a,b=input().split (" ")
k=1
a=int(a)
b=int(b)
for i in range(1,a+1):
  for j in range(1,b+1):
    if j==b:
      print (k,end="")
    else:
      print(k,end=" ")
    k+=1
  if i==a:
    break
  else:
    print()
print (end="")

# Week 6: Programming Assignment 2 - Number Triangle I
# Due on 2021-09-09, 23:59 IST
# Given an integer input 'n', print a number triangle of n lines as shown in the example.

a=int(input())
k=1
for i in range (1,a+1):
  for j in range(1,i+1):
    print(k,end="")
  k+=1
  print ()
  
# Week 6: Programming Assignment 3 - Symmetric Matrix
# Due on 2021-09-09, 23:59 IST
# Given a N X N square matrix, determine if it is a Symmetric Matrix.
# Input Format:
# The first line of the input contains an integer N which represents the number of rows and the number of columns.
# Next N lines represent the elements of the matrix.
# Output Format:
# Print Yes or No

def isSymmetric(mat, N):
  for i in range(N):
    for j in range(N):
      if (mat[i][j] != mat[j][i]):
        return False
  return True
    
a = int(input())
m = []
for i in range(1,a+1):
  l = list(map(int, input ().split ()))
  m.append(l)
if (isSymmetric(m, a)):
  print("Yes",end="")
else:
  print("No",end="")