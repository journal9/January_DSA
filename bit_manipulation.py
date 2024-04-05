#Write a function that takes an integer and returns the number of 1 bits present in its binary representation.
def numSetBits(A):
    count = 0
    while A>0:
        if (A & 1)==1:
            count+=1
        A = A>>1 
    return count  

# You are given two integers A and B.
# If B-th bit in A is set, make it unset
# If B-th bit in A is unset, make it set
# Return the updated A value
def solve(A, B):
    A = A^(1<<B)
    return A

# You are given two integers A and B.
# If B-th bit in A is set, make it unset.
# If B-th bit in A is unset, leave as it is.
# Return the updated A value.
def solve(A, B):
    if A & (1<<B)>0:
        A=A^(1<<B)
    return A  

# You are given two integers A and B.
# Return 1 if B-th bit in A is set
# Return 0 if B-th bit in A is unset 
def solve(A, B):
    if A & (1<<B)>0:
        return 1
    if A & (1<<B)==0:
        return 0
    
# Given an integer A. Unset B bits from the right of A in binary.
def solve(A, B):
    i=0
    while i<B:
        if A & (1<<i) > 0:
            A = A^(1<<i)
        i+=1
    return A

# Given an integer A, find and return the Ath magic number.
# A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.
# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
def solve(A):
    magic = 0
    for i in range(0,32):
        if A& 1<<i >0:
            magic+=pow(5,i+1)
    return magic    

# We define f(X, Y) as the number of different corresponding bits in the binary representation of X and Y.
# For example, f(2, 7) = 2, since the binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.
def solve(A):
    # sum = 0
    # for i in range(0,len(A)):
    #     for j in range(0,len(A)):
    #         D = A[i]^A[j]
    #         count = 0
    #         while (D):
    #             count += D & 1
    #             D >>= 1
    #         sum+=count
    # print(sum)
    N=len(A)
    ans=0
    mod=10**9+7
    for i in range(32):
        count1=0
        count0=0
        for j in range(N):
            if (A[j]>>i)&1:
                count1+=1
            else:
                count0+=1
        ans+=(2*count1*count0) % mod
    print(ans%mod)        

solve([1, 3, 5])