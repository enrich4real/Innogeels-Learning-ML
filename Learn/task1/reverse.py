#reversing an array
import numpy as np
a=int(input("Enter the number of rows="))
b=int(input("Enter the number of columns="))
z=0
mat=np.zeros(shape=(a,b), dtype = int)
for i in range(0,a):
    for j in range(0,b):
        c=int(input("Enter the number in {},{}=".format(i+1,j+1)))    
        mat[i,j]=c
print(mat)
mat1=np.flip(mat)
print("the reversed matrix is",mat1)