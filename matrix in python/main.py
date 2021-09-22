import numpy as np
# Matrix in Python using numpy class

#defing fillMAtrix function
def fillMatrix(arr, m,n):
    for i in range(m):
        c=[]
        for j in range(n):
            j = int(input("Enter the number : "))
            c.append(j)
            #out of the inner for loop
        arr.append(c)

def printMatrix(arr):
    for r in arr:
        print(r)

#transpose matrix function
def Transpose(arr):
    arr2 = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return arr2

if __name__ == '__main__':
    #matrix m x n
    m = int(input('Insert number of rows : '))
    n = int(input('Insert number of coloumns : '))
    arr = []
    arr2 = []
    fillMatrix(arr,m,n)
    print('Printing matrix filled')
    printMatrix(arr)
    #transpose matrix
    arr2 = Transpose(arr)
    print('Printing transpose matrix...')
    printMatrix(arr2)
    print('End of the program')
