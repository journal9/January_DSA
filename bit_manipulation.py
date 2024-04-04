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