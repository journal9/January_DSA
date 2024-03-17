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

#Smallest subarray with sum greater than a given value
def smallestSub(nums,x):
    l,r = 0,0
    curr = 0
    length = len(nums)
    minSub = length + 1
    while r<length:
        while curr<=x and r<length:
            curr+=nums[r]
            r+=1
        while curr>x and l<length:
            minSub = min(minSub,r-l) 
            curr-=nums[l]
            l+=1          
    return minSub

#Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
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

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# s[i] is either 'A', 'C', 'G', or 'T'.
def findRepeatedDnaSequences(s):
        pairs={}
        ret=[]
        i=0
        j=i+10
        while j<len(s)+1:
            if s[i:j] not in pairs:
                pairs[s[i:j]] = 1
            else:
                pairs[s[i:j]] += 1
            i+=1
            j+=1   
        ret = [key for key,value in pairs.items() if value>1] 
        return ret  
        
        # visited=set()
        # res=set()
        # for i in range(9,len(s)):
        #     a=s[i-9:i+1]
        #     if a in visited:
        #         res.add(a)
        #     else:
        #         visited.add(a)
        # return list(res)

        # if len(s) < 10:
        #     return []
        # substrings = []
        # for i in range(len(s) - 9):
        #     substrings.append(s[i:i+10])
        # counts = Counter(substrings)
        # result = []
        # for substring, count in counts.items():
        #     if count > 1:
        #         result.append(substring)
        # return result

        # l, n = 10, len(s)
        # seen = set()
        # output = set()
        # for start in range(n- l + 1):
        #     tmp = s[start:start+l]
        #     if tmp in seen:
        #         output.add(tmp[:])
        #     seen.add(tmp)
        # return output