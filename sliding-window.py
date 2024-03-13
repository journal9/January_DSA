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

#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
def containsNearbyDuplicate(nums, k):
    n = len(nums)
    i=0
    if n > k:
        while i<n-k:
            if nums[i] in nums[i+1:i+k+1]:
                return True
            i+=1 
    if len(nums[i:])<=k:
        if len(nums[i:]) != len(set(nums[i:])):
            return True       
    return False  

#Given a string s, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
            l,r = 0,0
            k = []
            k[:] = s
            max_sbstr = 0
            substr = []
            while r<len(k):
                if k[r] in substr:
                    ids = substr.index(k[r])
                    substr[:] = substr[ids+1:]
                    idx = k.index(k[r])
                    l=idx+1  
                substr.append(k[r])
                max_sbstr = max(max_sbstr,len(substr))
                r+=1
            return max_sbstr

        # L = ans = 0
        # x = set()

        # for R in range(len(s)):
            
        #     while s[R] in x:
        #         x.remove(s[L])
        #         L += 1
        #     if R - L + 1 > ans:
        #         ans = R - L + 1
        #     x.add(s[R])
        # return ans