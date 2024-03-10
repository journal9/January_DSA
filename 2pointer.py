#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
from math import floor


def twoSum(numbers, target):
        # for i , n in enumerate(numbers):
        #     o = target-n
        #     numbers[i]=" "
        #     if o in numbers:
        #         return [i+1,numbers.index(o)+1]
        l = 0
        r = len(numbers) - 1

        while l < r:
            res = numbers[l] + numbers[r]
            if res == target:
                return[l+1,r+1]
            if res < target:
                l += 1
            else:
                r -= 1

def twoSum(numbers, target):
        left_pointer, right_pointer = 0, len(numbers) -1
        while left_pointer < right_pointer:
            if numbers[left_pointer] + numbers[right_pointer] == target : return left_pointer+1, right_pointer+1 
            elif numbers[left_pointer] + numbers[right_pointer] < target: left_pointer += 1 
            elif numbers[left_pointer] + numbers[right_pointer] > target: right_pointer -= 1

#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

def threeSum(nums):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if a > 0:
            break
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1                
    return res     

def threeSum(nums):
    nums.sort()
    triplets=[]
    for i in range(len(nums)):
        a = nums[i]
        lp = i+1 ;rp = len(nums)-1
        while lp<rp: 
            if nums[lp]+nums[rp]==-a:
                an = [a,nums[lp],nums[rp]]
                an.sort()
                if an not in triplets:
                    triplets.append(an)
                lp+=1
                rp-=1
            elif nums[lp]+nums[rp]>-a:
                rp-=1
            else:
                lp+=1
    return triplets   


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
def maxArea(height):
    l = 0
    r = len(height) - 1
    maxArea = 0
    while l<r:
        maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return maxArea

# maxArea([1,8,6,2,5,4,8,3,7])

#Given an array containing integers 0, 1 and 2 representing the colors red, white and blue, sort them in-place so that the same numbers are adjacent, with the order being 0, 1 and 2.

def sortColors(nums):
    zero_ptr = curr = 0
    two_ptr = len(nums) - 1
 
    while curr <= two_ptr:
        if nums[curr] == 0:
            nums[curr], nums[zero_ptr] = nums[zero_ptr], nums[curr]
            zero_ptr += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[two_ptr] = nums[two_ptr], nums[curr]
            two_ptr -= 1
        else:
             curr += 1


    def fourSum(nums, target):
        nums.sort()
        res_ls=[]
        for i in range(len(nums)):
            for m in range(i+1,len(nums)-1):
                j=m+1
                k=len(nums)-1
                while j<k:
                    sum = nums[i]+nums[m]+nums[j]+nums[k]
                    if sum==target:
                        if [nums[i],nums[m],nums[j],nums[k]] not in res_ls:
                            res_ls.append([nums[i],nums[m],nums[j],nums[k]])
                        j+=1
                    if sum<target:
                        j+=1
                    if sum>target:
                        k-=1
        return res_ls
    
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.    
def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    cl_sum = 0
    for i in range(len(nums)-2):
        l=i+1
        r=len(nums)-1
        while l<r:
            sum= nums[i]+nums[l]+nums[r]
            if sum==target:
                return target
            else:
                diff = abs(target-sum)
                if abs(target-sum)<closest:
                    closest=diff
                    cl_sum = nums[i]+nums[l]+nums[r]   
            if target>sum:
                l+=1
            if target<sum:
                r-=1
    return cl_sum 
# ret = threeSumClosest([0,1,2],3)
# print(ret)   

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
def fourSum(nums, target):
        nums.sort()
        res_ls=[]
        for i in range(len(nums)):
            for m in range(i+1,len(nums)-1):
                j=m+1
                k=len(nums)-1
                while j<k:
                    print("----------------m")
                    print(nums[i])
                    print(nums[m])
                    print(nums[j])
                    print(nums[k])
                    sum = nums[i]+nums[m]+nums[j]+nums[k]
                    if sum==target:
                        if [nums[i],nums[m],nums[j],nums[k]] not in res_ls:
                            res_ls.append([nums[i],nums[m],nums[j],nums[k]])
                        j+=1
                    if sum<target:
                        j+=1
                    if sum>target:
                        k-=1
            if j>k:
                return res_ls
        return res_ls
# ret = fourSum([-2,-1,0,0,1,2],0)
# print(ret)

#A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
def nextPermutation(nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
def isPalindrome(s):
        s = s.lower()
        d = [i for i in s if i.isalnum()]
        for i in range(floor(len(d)/2)):
            if d[i]!=d[-i-1]:
                return False
        return True

def removeDuplicates(nums):

        index = 1
        occurance = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        
        return index

#Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
def removeDuplicates(nums):
        if len(nums) < 2: return len(nums)
        slow, fast = 2, 2

        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
        
        # def removeDuplicates(self, nums):
        #     k = 0
        #     for i in nums:
        #         if k < 2 or i != nums[k - 2]:
        #             nums[k] = i
        #             k += 1
        #     return k  

        # def removeDuplicates(self, nums: List[int]) -> int:

        # index = 1
        # occurance = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         occurance += 1
        #     else:
        #         occurance = 1

        #     if occurance <= 2:
        #         nums[index] = nums[i]
        #         index += 1
        
        # return index

#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
def removeDuplicates(nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

        # i = 1
        # for j in range(1, len(nums)):
        #     if nums[j] != nums[i-1]:
        #         nums[i] = nums[j]
        #         i += 1
        # return i

        # nums[:] = sorted(set(nums))
		# return len(nums)

        # slow, fast = 0, 1
		# while fast in range(len(nums)):
		# 	if nums[slow] == nums[fast]:
		# 		fast += 1
		# 	else:
		# 		nums[slow+1] = nums[fast]
		# 		fast += 1
		# 		slow += 1
		# return slow + 1
        
        # i = 1
		# while i < len(nums):
		# 	if nums[i] == nums[i - 1]:
		# 		nums.pop(i)
		# 	else:
		# 		i += 1
		# return len(nums)

#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
def removeElement(nums, val):
        i=0
        for j in range(0,len(nums)):
            nums[j-i]=nums[j]
            if nums[j]==val:
                i+=1   
        return len(nums)-i
        
        r = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[r] = nums[r], nums[i]
                r += 1
        return r

        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k

#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        
def strStr(haystack, needle):
    if needle==haystack:
            return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
        
#   try:
#     index = haystack.index(needle)
#     return index
#   except ValueError:
#       return -1

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
def reverseWords(self, s: str) -> str:
        s=s.strip(" ")
        st = s.split()
        i=0
        j=len(st)-1
        while i<j:
            st[i],st[j]=st[j],st[i]
            i+=1
            j-=1
        return ' '.join(st)
        
        #return " ".join(s.split()[::-1])

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
def reverseVowels(s):
    p=list(s)
    l=0
    r=len(p)-1
    vowels='aeiouAEIOU'
    while l<r:
        if p[l] not in vowels:
            l+=1
        if p[r] not in vowels:
            r-=1   
        if p[l] in vowels and p[r] in vowels:
            p[l],p[r]=p[r],p[l]
            l+=1
            r-=1
    return ''.join(p)


# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while n > 0:
        if nums1[m-1] >= nums2[n-1] and m>0:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1

    # idx = m + n - 1
    # while m > 0 and n > 0:
    #     if nums1[m - 1] < nums2[n - 1]:
    #         nums1[idx] = nums2[n - 1]
    #         n -= 1
    #     else:
    #         nums1[idx] = nums1[m - 1]
    #         m -= 1
    #     idx -= 1
    # while n > 0:
    #     nums1[idx] = nums2[n - 1]
    #     n -= 1
    #     idx -= 1
    
    # i = m - 1
    # # Initialize nums2's index
    # j = n - 1
    # # Initialize a variable k to store the last index of the 1st array...
    # k = m + n - 1
    # while j >= 0:
    #     if i >= 0 and nums1[i] > nums2[j]:
    #         nums1[k] = nums1[i]
    #         k -= 1
    #         i -= 1
    #     else:
    #         nums1[k] = nums2[j]
    #         k -= 1
    #         j -= 1
            
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]  
class Solution:   
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        while li < ri:
            nums[li],nums[ri]=nums[ri],nums[li]
            li += 1
            ri -= 1
            
    def rotate(self, nums, k: int) -> None:

        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);

#Kadane's Algorithm
# Given an integer array nums, find the 
# subarray with the largest sum, and return its sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
def maxSubArray(nums):
    maxSum = float("-inf")
    currSum=0
    for i in range(len(nums)):
        currSum += nums[i]
        maxSum = max(maxSum,currSum)
        currSum = max(currSum,0)
    return maxSum 