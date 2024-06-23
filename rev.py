# 1 factorial of a number
def fact(n):
    if n==1:
        return 1
    return fact(n-1) * n

# a = fact(6)
# print(a)

#2 sum of numbers till n
def sum(n):
    if n==0:
        return 0
    return sum(n-1)+n
# b = sum(100)
# print(b)

#3 fibonacci series till index z
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

# c = fib(10)
# print(c)

# 4 print A to 1 using recursion
def printr(a):
    if a==0:
        return
    print(a,' ')
    printr(a-1)

# printr(6)
# print(d)

# 5 check if a number is palindrome or not
def palin(a,i,j):
    if i>=j:
        return True
    if a[i]==a[j]:
        return palin(a,i+1,j-1)
    else:
        return False

def solve(a):
    i = 0
    j = len(a)-1
    ans = palin(a,i,j)
    return ans

# e = solve('ininui')
# print(e)

# 6 sum of digits of a number
def sumd(n):
    if n%10==0:
        return 0
    return sumd(n//10) + n%10
# f = sumd(655632)
# print(f)

# calculate A power B
def poww(A,B,C):
    if B==1:
        return abs(A%C)
    A = pow(A,B-1,C) * A
    ans = abs(A%C)
    return ans

# f = poww(2,3,3)
# print(f)

# Given a number A, check if it is a magic number or not.

def magic(m):
    if m==0:
        return 0
    return magic(m//10)+m%10

def check(a):
    while True:
        if a//10==0:
            if a==1:
                return 1
            else:
                return 0
        else:
            a = magic(a)

# m = check(1243)
# print(m)

# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
def solver(A, B):   
    if A == 1:
        return 0
    if B in (0,1):
        return B
    num = solver(A-1,B//2)
    if B%2 == 0:
        return num
    p = num ^ 1
    print(p)
    return num ^ 1
    

# s = solver(4,4)
# print(s)

def modSum(A):
    m = max(A)-1
    s=[0]*m
    for i in range(m):
        s[i] += 2
    for i in range(1,m):
            if s[i]==2:
                for j in range(i+1,m+1,A[i]):
                        s[j]+=1
    return s
# # a = [5, 17, 100, 11]
# # b = 28
# i = modSum([2,3,4,5])
# print(i)

def p(A,B):
    ans = []
    P = [1]*(B+1)
    for i in range(2,B+1):
        if P[i]:
            if i>=A:
                ans.append(i)
            for j in range(i*i,B+1,i):
                P[j]=0
    # res = ' '.join(ans)
    return ans
# s = p(1,7)
# print(s)

class Solution:
    # @param A : string
    # @return a strings
    def __init__(self):
        self.stack = [0]*500000
        self.pointer = 0

    def push(self,x):
        self.pointer+=1
        self.stack[self.pointer] = x

    def pop(self):
        val = self.stack[self.pointer]
        self.pointer-=1
        return val

    def peek(self):
        return self.stack[self.pointer]
    
    def isEmpty(self):
        return self.pointer<=0

    def precedence(self,x):
        if x =='^':
            return 3
        elif x=='*' or x=='/':
            return 2
        elif x=='+' or x=='-':
            return 1
        else: return 0

    def solve(self, A):
        postfix = []
        for a in A:
            if a.isdigit():
                postfix.append(str(a))
            elif a=='(':
                self.push(a)
            elif a==')':
                while self.peek() != '(':
                    postfix.append(str(self.peek()))
                    self.pop()
                self.pop()  # Pop the '(' from the stack
            else:
                while not self.isEmpty() and self.precedence(a)<=self.precedence(self.peek()):
                    postfix.append(str(self.pop()))
                self.push(a)
        while not self.isEmpty():
            postfix.append(str(self.peek()))
            self.pop()
        print(postfix)
        return ''.join(postfix)

s = Solution()
b = s.solve('x^y/(a*z)+b')
print(b)
