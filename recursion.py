# Calculate digits of a number through recursion
class Solution:
    def solve(self, A):
        sum=0
        return self.sumDigit(sum,A)

    def sumDigit(self,sum,n):
        sum+=n%10
        if n//10==0:
            return sum
        n=n//10
        return self.sumDigit(sum,n)

# C = Solution()
# q = C.solve(10000000)
# print(q)

#You are given an integer A, print A to 1 using using recursion.
class Solution:
    # @param A : integer
    def solve(self, A):
        self.printInc(A)
        print()

    def printInc(self,n):
        if n==0:
            return 
        print(n,end=' ')
        self.printInc(n-1)

#Write a program to find the factorial of the given number A using recursion.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return self.fact(A)

    def fact(self,A):
        if A==1:
            return 1
        else:
            return self.fact(A-1) * A     
        
#The Fibonacci numbers are the numbers in the following integer sequence.
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        return self.fibo(A)


    def fibo(self,A):
        if A<=1:
            return A
        return (self.fibo(A-1)+ self.fibo(A-2))

#Write a recursive function that checks whether string A is a palindrome or Not.
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        i = 0
        j = len(A)-1
        return self.pal(i,j,A)

    def pal(self,i,j,n):
        if i > j:    # base condition
            return 1
        if n[i] == n[j]:    # Actual Logic
            i += 1
            j -= 1
            return self.pal(i,j,n)
        
        else:
            return 0
    
c = Solution()
q = c.solve("strings")
print(q)

#Return 1 if the sum of digits of number till single digit is 1 , else 0
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        while True:
            if A // 10 == 0:
                if A == 1:
                    return 1
                else:
                    return 0
            else:
                A = sum_of_digits(A)

def sum_of_digits(n):
    if n == 0:
        return 0
    return sum_of_digits(n//10) + n%10

s = Solution()
q = s.solve(83557)
print(q)

#generate valid parenthesis list of length A
class Solution:
    # @param A : integer
    # @return a list of strings
    def par(self,ans,n,openc,closec,res):
        if len(ans)==2*n:
            res.append(ans)
        if openc<n:
            self.par(ans+'(',n,openc+1,closec,res)
        if closec<openc:
            self.par(ans+')',n,openc,closec+1,res)
        return res

    def generateParenthesis(self, A):
        return self.par('',A,0,0,[])


s = Solution()
q = s.generateParenthesis(2)
print(q)


#Given a set of distinct integers A, return all possible subsets.
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def __init__(self):
        self.res = []

    def substr(self,A,curr,idx,res):
        if idx==len(A):
            self.res.append(sorted(curr.copy())) #passing shallow copy
            return
        self.substr(A,curr,idx+1,res)
        curr.append(A[idx])
        self.substr(A,curr,idx+1,res)
        curr.pop(len(curr)-1)

    def subsets(self, A):
        self.substr(A,[],0,self.res)
        return sorted(self.res)
    
s = Solution()
q = s.subsets([1,2,3])
print(q)


#Given an integer array A of size N denoting collection of numbers , return all possible permutations.
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def __init__(self):
        self.res = []

    def per(self,A,idx,ans,visit):
        n = len(A)
        if idx==len(A):
            temp  = ans.copy()
            self.res.append(temp)
            return
        for i in range(len(A)):
            if not visit[i]:
                visit[i] = True
                ans[idx] = A[i]
                self.per(A,idx+1,ans,visit)
                visit[i]=False

    def permute(self, A):
        n = len(A)
        visit = [False]*n
        ans = [0]*n
        self.per(A,0,ans,visit)
        return self.res
