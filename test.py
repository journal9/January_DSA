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

# def firstMissingPositive(A): 

#     def swap(arr, i, j):
#             arr[i], arr[j] = arr[j], arr[i]

#     for i in range(0,len(A)):
#         while A[i] in range(1,len(A)) and A[i]!=i+1 and A[i] != A[A[i]-1]:
#             swap(A, i, A[i] - 1)
    
#     for i in range(len(A)):
#         if A[i] != i + 1:
#             return i + 1
    
#     return len(A) + 1
#     # i=0
#     # while i<len(A):
#     #     if A[i] in range(1,len(A)) and A[i]!=i+1 and A[i]!=A[A[i]-1]:
#     #         A[i],A[i-1] = A[i-1],A[i]
#     #     i+=1     
#     # for i in range(0,len(A)):
#     #     if not A[i]-i==1:
#     #         return i+1
#     # i=0
#     # while i<len(A):
#     #     if A[i] in range(1,len(A)) and A[i]!=i+1:
#     #         if i==0 or A[i]!=A[A[i]-1]:
#     #             # A[i],A[A[i]-1] = A[A[i]-1],A[i]
#     #             temp = A[i]
#     #             A[i] = A[A[i]-1]
#     #             A[A[i]-1] = temp
#     #     i+=1
#     # print(A)
#     # for i in range(0,len(A)):
#     #     if not A[i]-i==1:
#     #         return i+1

# A = [3,6,1,2]
# r = firstMissingPositive(A)
# print(r)

# def solve(A):
#     Ab = []
#     for i in sorted(A, key=lambda k: k[0]):
#         if Ab and i[0] <= Ab[-1][1]:
#             Ab[-1][1] = max(Ab[-1][1], i[1])
#         else:
#             Ab.append(i)
#     # for a in Aa:
#     #     print(a)
#     #     if a not in ans:
#     #         ans.append(a)   
#     print(Ab)                   

#     #     print(i)
#     #     ans = []
#     #     start  = A[i][0]
#     #     end = A[i][1]
#     #     if(A[i][0]<A[i-1][1]):
#     #         start = A[i-1][0]
#     #     if(A[i][1]<A[i-1][1]):
#     #         end = A[i-1][1]
#     #     else:
#     #         end = A[i][1]
#     #     A[i][0] = start
#     #     A[i][1] = end   
#     #     if A[i][0] == A[i-1][0]:
#     #         ed = max(A[i][1],A[i-1][1])
#     #         A[i][1] = ed
#     #         A[i-1][1] = ed
#     #     if A[i][1] == A[i-1][1]:
#     #         st = min(A[i][0],A[i-1][0])
#     #         A[i][0] = st
#     #         A[i-1][0] = st  
    
#     # print(ans) 

# A = [[1,17],[1,32],[3,13],[4,100],[5,31],[5,63],[6,11],[6,57],[7,24],[7,76],[8,36],[9,15],[9,44],[10,26],[10,71],[10,76],[10,87],[11,12],[12,24],[12,28],[13,67],[14,29],[15,88],[16,21],[17,31],[17,85],[18,29],[18,42],[18,47],[21,35],[21,35],[21,72],[24,67],[25,62],[25,78],[27,100],[29,37],[29,83],[29,94],[30,63],[30,95],[31,73],[31,78],[32,70],[33,40],[33,51],[36,53],[37,90],[39,70],[40,73],[44,59],[45,90],[46,93],[47,74],[48,79],[48,94],[49,68],[51,63],[53,55],[56,70],[56,87],[58,71],[58,79],[62,68],[63,73],[64,74],[66,83],[67,100],[68,75],[68,78],[69,94],[70,73],[78,83]]
# solve(A)

# def insert(A, B):
#     ans=[]
#     n = len(A)
#     if n==0:
#         ans.append(B)
#     elif B[1]<A[0][0]:
#         ans.append(B)
#         ans.extend(A) 
#     elif B[0] > A[-1][1]:
#         ans.extend(A)
#         ans.append(B) 
#     else:
#         i = 0
#         while i<n:
#             if A[i][1]<B[0]:
#                 ans.append(A[i])
#             else:
#                 break
#             i+=1

#         start = B[0]
#         end = B[1] 
#         i=0
#         while i< n:
#             if not (start>A[i][1] or end<A[i][0]):
#                 start = min(start,A[i][0])
#                 end = max(end,A[i][1])
#             else:
#                 break
#             i+=1
#         ans.append([start,end])    
#         while i<n:
#             ans.append(A[i])   
#             i+=1 
#     print(ans) 



# A = [[6037774,6198243],[6726550,7004541],[8842554,10866536],[11027721,11341296],[11972532,14746848],[16374805,16706396],[17557262,20518214],[22139780,22379559],[27212352,28404611],[28921768,29621583],[29823256,32060921],[33950165,36418956],[37225039,37785557],[40087908,41184444],[41922814,45297414],[48142402,48244133],[48622983,50443163],[50898369,55612831],[57030757,58120901],[59772759,59943999],[61141939,64859907],[65277782,65296274],[67497842,68386607],[70414085,73339545],[73896106,75605861],[79672668,84539434],[84821550,86558001],[91116470,92198054],[96147808,98979097]]
# B = [36210193,61984219]
# insert(A,B)   

# def solve(A):
#     n = len(A)
#     t_sum=0
#     for i in range(n+3):
#         t_sum^=i
#     for i in range(n):
#         t_sum^=A[i]
#     print(t_sum)

#     for i in range(31):
#         if t_sum & (1<<i) >0:
#             idx = i
#             break
#     n1,n2=0,0
#     for i in range(0,len(A)):
#         if A[i]&(1<<idx)>0:
#             n1^=A[i]     
#         else:
#             n2^=A[i]  
#     lsit = [n1,n2] 
#     lsit.sort()       
#     print(lsit)   

# solve([3, 2, 4])

# def solved(A):
#     ans = 0
#     for k in range(31,-1,-1):
#         c=0
#         for i in range(len(A)):
#             if A[i]&(1<<k)>0:
#                 c+=1
#         if c>=2:
#             ans |= 1<<k
#             for j in range(0,len(A)):
#                 if A[j] & (1<<k)==0:
#                     A[j]=0  
#     print(ans)

    # def solve(self, A):
    #     ans = 0
    #     for bit in range(30, -1, -1):
    #         count = 0
    #         for val in A:
    #             # count = count + (1 if (val & (1 << bit)) else 0)  – shorthand code for below loop
    #             if (val & (1 << bit)):
    #                 count = count + 1
    #         if count >= 2:
    #             ans = ans | 1 << bit
    #             # A = [a if (a & (1 << bit)) else 0 for a in A] – shorthand code for below loop
    #             for i in range(0, len(A), 1):
    #                 if (A[i] & (1 << bit)) == 0:
    #                     A[i] = 0
    #     return ans

# solved([21,18,24,17,16])


# def solve(A):
#     ans = 0
#     mod = 10**9 + 7
#     for i in range(31):
#         index = -1
#         for j in range(len(A)):
#             if A[j]&(1<<i)>0:
#                 c = pow(2,i)
#                 ans+=(len(A)-j)*c*(j-index)
#                 index=j
#     print(ans % mod)

# solve([347148,221001,394957,729925,276769,40726,552988,29952,184491,146773,418965,307,219145,183037,178111,81123,109199,683929,422034,346291,11434,7327,340473,316152,364005,359269,170935,105784,224044,22563,48561,165781,9329,357681,169473,175031,605611,374501,6607,329965,76068,836137,103041,486817,195549,107317,34399,56907,37477,189690,36796,376663,39721,177563,174179,183646,217729,408031,429122,631665,282941,526797,262186,306571,63613,57501,70685,226381,1338,9360,130360,20300,400906,87823,180349,108813,18181,119185,1,102611,63591,12889,311185,383896,8701,76077,75481,386017,153553,304913,383455,105948,142885,1,12610,137005,119185,16948,66171,123683])

# def rangeSum(A, B):
#     item = A[0]
#     for i in range(1,len(A)):
#         A[i]+=item
#         item = A[i]
#     ans = []
#     for j in range(len(B)):
#         start = B[j][0]
#         end = B[j][1]
#         if start ==0:
#             ans.append(A[end])
#         else:
#             ans.append(A[end]-A[start-1])
#     print(ans)    

# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]
# rangeSum(A,B)

def solve(A):
    ans = -1
    sum_left = 0
    sum_right = 0
    for i in range(len(A)):
        sum_right+=A[i]
    for i in range(0,len(A)):
        if i==0:
            sum_right=sum_right - A[i]
            if sum_left==sum_right:
                return i
        else:
            sum_left += A[i-1]
            sum_right=sum_right - A[i]
            if sum_left==sum_right:
                return i+1
    return ans   

A = [1,2,3,7,1,2,3]
a = solve(A)
print(a)