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

def minSubArrayLen(target, nums):
    minS = len(nums)
    sum=nums[0]
    i=0
    j=0
    while j < len(nums) and i<=j:
        if(sum<target):
            j+=1
            if j==len(nums):
                break
            sum+=nums[j]
        else:
            minS = min(minS,j-i+1)
            sum-=nums[i]
            i+=1
    print(minS)        
            

a = [2,3,1,2,4,3]
b = 7
minSubArrayLen(b,a)