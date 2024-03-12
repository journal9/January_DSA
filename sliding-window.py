#Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.
# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
# Output : 39
def maxSubstring(nums,k):
    n = len(nums)
    if k >n:
        return -1
    s = sum(nums[:k])
    mx = s
    for i in range(1,n-k+1):
        s = s - nums[i-1] + nums[i+k-1]
        mx = max(mx,s)
    return mx

a=[1, 4, 2, 10, 23, 3, 1, 0, 20]
b=4
kt = maxSubstring(a,b)
print(kt)