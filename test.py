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

from ast import List


height = [1,8,6,2,5,4,8,3,7]
def maxArea(height):
    indMax = []
    for i in range(len(height)-1):
        max_pdt = 1
        if height[i]==1:
            max_pdt = ((len(height)-i-1)*1)
            print(max_pdt)
            indMax.append(max_pdt) 
            continue 
        for j in range(i+1,len(height)):
            print(height[i])
            print(height[j])
            if (j-i)*min(height[i],height[j])>max_pdt:
                max_pdt = ((j-i)*min(height[i],height[j]))
        print(max_pdt)
        indMax.append(max_pdt)  
    indMax.sort()
    print(indMax)
    print(indMax[-1])         

                






maxArea(height)



    
    





