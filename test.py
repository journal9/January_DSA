# from math import floor


# s = "A man, a plan, an canal: Panama"
# s2 = s.lower()
# print(s2)
# d = [i for i in s2 if i.isalnum()]
# print(d)
# for i in range(floor(len(d)/2)):
#     if d[i]!=d[-i-1]:
#         print('false')
# print('true')

# numbers = [2,7,7,15]
# target = 14  
# for i , n in enumerate(numbers):
#     o = target-n
#     numbers[i]=" "
#     if o in numbers:
#         print(i+1,numbers.index(o)+1)    

# nums = [-1,0,1,2,-1,-4]
# nums.sort()
# triplets=[]
# for i in range(len(nums)):
#     a = nums[i]
#     lp = i+1 ;rp = len(nums)-1
#     print(nums)
#     print(nums)
#     while lp<rp:
#         print(nums[lp])
#         print(nums[rp])    
#         if nums[lp]+nums[rp]==-a:
#             an = [a,nums[lp],nums[rp]]
#             an.sort()
#             if an not in triplets:
#                 triplets.append(an)
#             lp+=1
#             rp-=1
#         elif nums[lp]+nums[rp]>-a:
#             rp-=1
#         else:
#             lp+=1

# print(triplets)
# print('no')

# height = [1,8,6,2,5,4,8,3,7]
# def maxArea(height):
#     indMax = []
#     for i in range(len(height)-1):
#         max_pdt = 1
#         if height[i]==1:
#             max_pdt = ((len(height)-i-1)*1)
#             print(max_pdt)
#             indMax.append(max_pdt) 
#             continue 
#         for j in range(i+1,len(height)):
#             print(height[i])
#             print(height[j])
#             if (j-i)*min(height[i],height[j])>max_pdt:
#                 max_pdt = ((j-i)*min(height[i],height[j]))
#         print(max_pdt)
#         indMax.append(max_pdt)  
#     indMax.sort()
#     print(indMax)
#     print(indMax[-1])         

# maxArea(height)

# def threeSumClosest(nums, target):
#     nums.sort()
#     closest = 10000
#     cl_sum =0
#     for i, a in enumerate(nums):
#         l=i+1
#         r=len(nums)-1
#         while l<r:
#             # diff = abs(target-(a+nums[i]+nums[j]))
#             # closest = min(closest,abs(target-(a+nums[i]+nums[j])))
#             if abs(target-(a+nums[l]+nums[r]))<closest:
#                 closest=abs(target-(a+nums[l]+nums[r]))
#                 cl_sum = a+nums[l]+nums[r]
#                 if target-(a+nums[l]+nums[r])>0:
#                     l+=1
#                 else:
#                     r-=1
#             if (target-(a+nums[l]+nums[r]))>0:
#                 l+=1
#             if (target-(a+nums[l]+nums[r]))<0:
#                 r-=1
#     return cl_sum

# ret = threeSumClosest([0,1,2],3)
# print(ret)

# def fourSum(nums, target):
#         nums.sort()
#         res_ls=[]
#         for i in range(len(nums)):
#             for m in range(i+1,len(nums)-1):
#                 j=m+1
#                 k=len(nums)-1
#                 while j<k:
#                     print("----------------m")
#                     print(nums[i])
#                     print(nums[m])
#                     print(nums[j])
#                     print(nums[k])
#                     sum = nums[i]+nums[m]+nums[j]+nums[k]
#                     if sum==target:
#                         if [nums[i],nums[m],nums[j],nums[k]] not in res_ls:
#                             res_ls.append([nums[i],nums[m],nums[j],nums[k]])
#                         j+=1
#                     if sum<target:
#                         j+=1
#                     if sum>target:
#                         k-=1
#             if j>k:
#                 return res_ls
#         return res_ls
# ret = fourSum([-2,-1,0,0,1,2],0)
# print(ret)

# def nextPermutation(nums):
#     temp=0
#     for i in range(len(nums)-2):
#         j=i+1
#         k=j+1
#         if nums[j]>=nums[i]:
#             i+=1
#             j+=1
#             continue
#         if nums[i]>nums[j]:
#             if j==len(nums)-2:
#                 nums.unshift(nums[-1])
#                 nums.pop(-1)
#                 return nums
#             if nums[j]<nums[k]:
#                 temp=nums[k]
#                 nums[k]=nums[j]
#                 nums[j]=temp
#                 return nums
#             else:
#                 temp=nums[k]
#                 nums[k]=nums[i]
#                 nums[i]=temp
#                 return nums  

# def nextPermutation2(nums):
#     temp=0
#     for i in range(len(nums)-1,-1,-1):
#         print(nums[i])
#         j=i-1
#         print(nums[j])
#         if nums[j]<nums[i]:
#             temp=nums[j]
#             nums[j]=nums[i]
#             nums[i]=temp
#             return nums
#         else: 
#             while nums[j]>=nums[i]:
#                 if j>0:
#                     j-=1 
#                 else:
#                     break 
#             #part = list(nums[j+1:i]).sort()
#             part = sorted(nums[j+1:i+1])
#             print(part)
#             a=part[-1]
#             b=nums[j]
#             nums[j]=a
#             part[-1]=b
#             # nums[j] = part[-1]
#             # part[-1]=nums[j]
#             # print(nums[j])
#             nums = nums[:j+1]+part
#             # nums.unshift(nums[j-1])  
#             # nums.pop(j+1)
#             # temp=nums[j]
#             return nums
#     return nums              
# ret = nextPermutation2([
#     3,2,1
# ])
# print(ret)


# def sortColors(nums):
#         k=0
#         j=k+1
#         while k< len(nums)-2:
#             i=k
#             while j<len(nums)-1:
#                 if nums[j]<nums[i]:
#                     nums[i], nums[j] = nums[j],nums[i]
#                     j+=1
#                     i+=1
#                 if nums[j]==nums[i]:
#                     i+=1
#                     j+=1
#                 else:
#                     j+=1

#             k+=1     
#             j=i+1

        
#         return nums

# rt = sortColors([1,0,1,2,0,2])
# print(rt)

# a= [1,2,3,3,3,4,5,5]     
# def removeDuplicates(nums):
#         if len(nums) < 2: return len(nums)
#         slow, fast = 2, 2

#         while fast < len(nums):
#             if nums[slow - 2] != nums[fast]:
#                 nums[slow] = nums[fast]
#                 slow += 1
#             fast += 1
#         print(nums)    
#         return slow

# ret = removeDuplicates(a)
# print(a)
# print(ret)

# a=[3,2,2,4,3,5]
# def removeElement(nums, val):
#         i=0
#         for j in range(0,len(nums)):
#             print(j)
#             nums[j-i]=nums[j]
#             if nums[j]==val:
#                 i+=1
#         print(nums)    
#         return len(nums)-i

# ret = removeElement(a,3)
# print(ret)
# print(a)

# def strStr(haystack, needle):
#     k=0
#     indx=[]
#     if needle==haystack:
#         return 0

#     for i in range(len(haystack)):
#         if len(indx)==len(needle) and len(indx)!=0:
#             return indx[0]
#         if haystack[i]==needle[k]:
#             indx.append(i)
#             k+=1
#         else:
#             k=0
#     if len(indx)==len(needle):
#         return indx[0]
#     return -1

# ret = strStr('abc','c')
# print(ret)

# def reverseWords(s):
#     st = s.split(' ')
#     print(st)
#     i=0
#     j=len(st)-1
#     while i<j:
#         st[i],st[j]=st[j],st[i]
#         i+=1
#         j-=1
#     print(st) 
#     print(' '.join(st))   
# reverseWords("dog is cat")

# def reverseVowels(s):
#         p=list(s)
#         print(p)
#         l=0
#         r=len(p)-1
#         vowels='aeiouAEIOU'
#         while l<r:
#             if p[l] not in vowels:
#                 l+=1
#             if p[r] not in vowels:
#                 r-=1   
#             if p[l] in vowels and p[r] in vowels:
#                 p[l],p[r]=p[r],p[l]
#                 l+=1
#                 r-=1
#         return ''.join(p)
# ret = reverseVowels('aA')
# print(ret)

# def merge(nums1, m, nums2, n):
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     mr = []
#     t = min(n,m)
#     q=max(n,m)
#     i=0
#     j=0
#     print(t)
#     while i<t:
#         print(i)
#         if nums1[i]<nums2[j]:
#             mr.append(nums1[i])
#             i+=1
#             continue
#         if nums1[i]>nums2[j]:
#             mr.append(nums2[j])
#             j+=1
#             continue
#         if nums1[i]==nums2[j]:
#             mr.append(nums1[i])
#             mr.append(nums2[j])
#             i+=1
#             j+=1
#             continue
#     if n>m:
#         mr.extend(nums1[j:])
#     else:
#         mr.extend(nums2[j:]) 
#     print(mr)   

# merge([1,2,4,5,7,0,0,0],5,[2,4,5],3)
# def teer(nums):
#     if len(nums) < 2: return len(nums)
#     slow, fast = 2, 2

#     while fast < len(nums):
#         if nums[slow - 2] != nums[fast]:
#             nums[slow] = nums[fast]
#             slow += 1
#         fast += 1
#     return slow

# nums = [1,1,1,2,2,3]
# p = teer(nums)
# print(p)
# print(nums)

# def rotate(nums, k):
#     nums.reverse()
#     ab= nums[:k]
#     ab.reverse()
#     cd= nums[k:]
#     cd.reverse()
#     ad = ab+cd
#     return ad


# numss = [1,2,3,4,5,6,7]
# rt = rotate(numss,3)
# print(rt)


def kad(nums):
    maxSum = float("-inf")
    currSum=0
    for i in range(len(nums)):
        currSum += nums[i]
        currSum = max(currSum,0)
        maxSum = max(maxSum,currSum)
    return maxSum    


kt = kad([4,-1,2,-7,3,4])
print(kt)
