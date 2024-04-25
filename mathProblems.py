# all prime numbers between 2 to A
def solve(A):
    ans = []
    P = [1]*(A+1)
    for i in range(2,A+1):
        if P[i]:
            ans.append(i)
            for j in range(i*i,A+1,i):
                P[j]=0
    # res = ' '.join(ans)
    return ans

s = solve(49)
print(s)

# list of numbers of factors a list of numbers.
import math
def solve(A):
    m = max(A)
    s=[1]*(m+1)
    for i in range(m+1):
        s[i] = i
    st = math.ceil(math.sqrt(m))
    for i in range(2,m+1):
        if s[i]==i:
            for j in range(i*i,m+1,i):
                if s[j]==j:
                    s[j]=i
    ans = []
    for n in A:
        x = s[n]
        f=1
        while x>1:
            c=0
            while n%x==0:
                c+=1
                n//=x
            x = s[n]
            f*=c+1
        ans.append(f)
    return ans

r = solve([10,20])
print(r)