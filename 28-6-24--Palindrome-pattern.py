#Given a two-dimensional integer array arr of dimensions 
#n x n, consisting solely of zeros and ones, identify the row or column 
#(using 0-based indexing) where all elements form a palindrome. 
#If multiple palindromes are identified, prioritize the palindromes found in rows 
#over those in columns. Within rows or columns, the palindrome with the smaller index 
#takes precedence. The result should be represented by 
#the index followed by either 'R' or 'C', indicating whether the palindrome 
#was located in a row or column. The output should be space-separated. 
#If no palindrome is found, return the string -1.


class Solution:
    def pattern (self, arr):
        n = len(arr)
    
        def is_palindrome(list):
            if (list == list[::-1]):
                return True
            else:
                return False
            
        for i in range(0, n):
            if is_palindrome(arr[i]):
                return str(i) + ' R'
        
        column = []
    
        for i in range(0, n):
            column.clear()
            for j in range(0, n):
                column.append(arr[j][i])
            if is_palindrome(column):
                return str(i) + ' C'
    
        return str(-1)
             



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends
