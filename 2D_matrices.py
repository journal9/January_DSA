#Traverse spirally through the matrix
def generateMatrix(A):
    if A==1:
        mtrx = [1]
        return mtrx
    mtrx = [[0]*A  for _ in range(A)]  # <------this
    r_start,r_end,c_start,c_end = 0,A,0,A
    ct = 1
    while r_start<r_end or c_start < c_end:
        for i in range(c_start,c_end):
            mtrx[r_start][i] = ct
            ct+=1
        r_start+=1        
        for i in range(r_start,r_end):
            mtrx[i][c_end-1] = ct
            ct+=1
        c_end-=1
        for i in range(c_end-1,c_start-1,-1):
            mtrx[r_end-1][i] = ct
            ct+=1  
        r_end-=1
        for i in range(r_end-1,r_start-1,-1):
            mtrx[i][c_start] = ct
            ct+=1
        c_start+=1    

    return mtrx


t = generateMatrix(1)
print(t)

#sum of all sub matrices
def solve(A):
    N = len(A)
    sum=0
    for i in range(0,N):
        for j in range(0,N):
            sum+=A[i][j]*(i+1)*(j+1)*(N-i)*(N-j)
    print(sum)
A = [ [1, 1],
      [1, 1] ]
solve(A)