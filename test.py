# def lengthOfLongestSubstring(s):
#     l,r = 0,0
#     k = []
#     k[:] = s
#     max_sbstr = 0
#     substr = []
#     while r<len(k):
#         if k[r] in substr:
#             ids = substr.index(k[r])
#             substr[:] = substr[ids+1:]
#             idx = k.index(k[r])
#             l=idx+1  
#         substr.append(k[r])
#         max_sbstr = max(max_sbstr,len(substr))
#         r+=1
#     print(max_sbstr)
#     return True

# st= "abcabcdekbb"
# kt = lengthOfLongestSubstring(st)

# def smallestSub(nums,x):
#     l,r = 0,0
#     curr = 0
#     length = len(nums)
#     minSub = length + 1
#     while r<length:
#         while curr<=x and r<length:
#             curr+=nums[r]
#             r+=1
#         while curr>x and l<length:
#             minSub = min(minSub,r-l) 
#             curr-=nums[l]
#             l+=1          
#     return minSub

# nump = [1,4,45,52,-12,79]
# a = 51
# kt = smallestSub(nump,a)
# print(kt)

# def smallestSubWithSum(arr, n, x):
 
#     # Initialize current sum and minimum length
#     curr_sum = 0
#     min_len = n + 1
 
#     # Initialize starting and ending indexes
#     start = 0
#     end = 0
#     while (end < n):
 
#         # Keep adding array elements while current
#         # sum is smaller than or equal to x
#         while (curr_sum <= x and end < n):
#             curr_sum += arr[end]
#             end += 1
 
#         # If current sum becomes greater than x.
#         while (curr_sum > x and start < n):
 
#             # Update minimum length if needed
#             if (end - start < min_len):
#                 min_len = end - start
 
#             # remove starting elements
#             curr_sum -= arr[start]
#             start += 1
 
#     return min_len

# arr1 = [1, 4, 45, 6, 10, 19]
# x = 51
# n1 = len(arr1)
# res1 = smallestSubWithSum(arr1, n1, x)
# print(res1)

# def minSubArrayLen(s):
#     pairs={}
#     ret=[]
#     i=0
#     j=i+10
#     while j<len(s)+1:
#         if s[i:j] not in pairs:
#             pairs[s[i:j]] = 1
#         else:
#             pairs[s[i:j]] += 1
#         i+=1
#         j+=1   
#     ret = [key for key,value in pairs.items() if value>1] 
#     print(ret)        
            

# a = [2,3,1,2,4,3]
# b = 7
# minSubArrayLen("AAAAAAAAAAA")

# def numSetBits(A):
#     count=0
#     b = str(bin(A))
#     for i in b:
#         if i=='1':
#             count+=1
#     return count

# rt = numSetBits(5)
# print(rt)        

# def solve(A, B):
#     A.reverse()
#     print(A)
#     A = A[:B+1].reverse()
#     return A

# t = solve([1,2,3,4,5],2)
# print(t)

# # print(4//3)
def solve(A):
    max_r = -1
    N = len(A)
    c=N-1
    r=0
    while r<N and c>=0:
        while c>=0 and A[r][c]==1:
            max_r=r
            c-=1
        r+=1    
    print(max_r)                  


A = [   [0, 0, 1],
         [0, 0, 1],
         [0, 1, 1]   ]

solve(A)