# A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal 
# from left to right is constant, i.e., all elements in a diagonal are the same. 
# Given a rectangular matrix mat, your task is to complete the function isToeplitz which returns true 
# if the matrix is Toeplitz otherwise, it returns false.

def isToeplitz(mat):
    
    rows = len(mat)
    columns = len(mat[0])
    
    mat_a = [[mat[i][j] for j in range(columns - 1)] for i in range(rows - 1)]
    mat_b = [[mat[i][j] for j in range(1, columns)] for i in range(1, rows)]
    
    return mat_a == mat_b 


mat = [[0, 1, 11], [3, 0, 1], [4, 3, 0]]
print(isToeplitz(mat))


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToeplitz(matrix)

        if b == True:
            print("true")
        else:
            print("false")

# } Driver Code Ends