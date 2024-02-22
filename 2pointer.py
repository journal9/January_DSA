#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
def twoSum(numbers: List[int], target: int) -> List[int]:
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

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers) -1
        while left_pointer < right_pointer:
            if numbers[left_pointer] + numbers[right_pointer] == target : return left_pointer+1, right_pointer+1 
            elif numbers[left_pointer] + numbers[right_pointer] < target: left_pointer += 1 
            elif numbers[left_pointer] + numbers[right_pointer] > target: right_pointer -= 1

#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

def threeSum(nums: List[int]) -> List[List[int]]:
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

def threeSum(nums: List[int]) -> List[List[int]]:
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
def maxArea(height: List[int]) -> int:
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


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
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
def threeSumClosest(self, nums: List[int], target: int) -> int:
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