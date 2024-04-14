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

C = Solution()
q = C.solve(10000000)
print(q)

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
