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