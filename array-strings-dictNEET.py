# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
nums=[1,2,3,4,2]
list_num = set(nums)
for i in list_num:
    nums.remove(i)
if len(nums)!=0:
    print(True)
else:
    print(False)  

def containsDuplicate(nums: List[int]) -> bool:
    list_num = set()
    for i in nums:
        if i in list_num:
            return True
        else:
            list_num.add(i)

def containsDuplicate(nums: List[int]) -> bool:
    return len(nums)!=len(set(nums))

def containsDuplicate(nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

from ast import List
from collections import Counter
import collections

#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t) or set(s)!=set(t):
        return False
    tl = list(t)
    for i in list(s):
        if i in tl:
            tl.remove(i)
        else:
            return False
    if len(tl)!=0:
        return False
    else:
        return True  
    
def isAnagram(s: str, t: str) -> bool:
        s_set = set(list(s)).union(set(list(t)))
        for a in s_set:
            if s.count(a) != t.count(a):
                return False
        return True

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)   

def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)  

def isAnagram(s: str, t: str) -> bool:
        return sorted(s)==sorted(t)  

def isAnagram(s: str, t: str) -> bool:
        lex_s = {}
        lex_t = {}

        for c in s:
            if c not in lex_s:
                lex_s[c] = 1
            else:
                lex_s[c] += 1
        for d in t:
            if d not in lex_s:
                return False
            elif d not in lex_t:
                lex_t[d] = 1
            else:
                lex_t[d] += 1
                if lex_t[d] > lex_s[d]:
                    return False
        return lex_s == lex_t

# ok = isAnagram('anagram','gramaan')
# print(ok)

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
def twoSum(nums: List[int], target: int) -> List[int]:
    for i,n in enumerate(nums):
        if target - n in nums[i+1:]:
            return [i,nums.index(target-n,i+1)]

def twoSum(nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

twoSum([1,3,6,4,9,12,4],9)

#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
        return list(anagram_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
def topKFrequent(nums: List[int], k: int) -> List[int]:
        cd ={}
        for n in nums:
            if n in cd.keys():
                cd[n]+=1
            else:
                cd[n]=1      
        kc = dict(sorted(cd.items(), key=lambda item: item[1],reverse=True))
        ans = list(kc.keys())
        return ans[:k]

nums=[1,1,1,3,4,3,3,4,3,5,6,7,7,4]
k=3
topKFrequent(nums,k)

#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * (len(nums))
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    postpr = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postpr
        postpr *= nums[i]
    return res

def productExceptSelf(nums: List[int]) -> List[int]:
        from functools import reduce
        product = reduce((lambda x, y: x * y), nums)
        res = []
        for i,n in enumerate(nums):
            if n!=0:
                res.append(product//n)  
            else:
                temp =nums.copy()
                temp.pop(i)
                res.append(reduce((lambda x, y: x * y), temp))
        return res

productExceptSelf([1,2,3,4])

#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
def isValidSudoku(board: List[List[str]]) -> bool:
        res=[]

        for i in range(9):
            for j in range(9):
                cell=board[i][j]

                if cell != ".":
                    res+=[(i,cell),(cell,j),(i//3,j//3,cell)]

        
        return len(res)==len(set(res))

def isValidSudoku(board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]  

isValidSudoku(board)    

#Problem: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode
"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode( apl):
    res = ''
    strs = apl.split(" ")
    for s in strs:
        encoded = str(len(s)) + '/' + s
        res += encoded
    return res
"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode( str):
    res=[]
    i =  0
    while i < len(str):
        # For example, 12/abc
        e = i
        while e < len(str) and str[e] != '/':
            e += 1
        size = int(str[i:e])
        word = str[e + 1: e + 1 + size]
        i = e + 1 + size
        res.append(word)
    return " ".join(res)

# s = "Hi from here."
# enc = encode(s)
# print(enc)
# dec = decode(enc)
# print(dec)

s = "Arguments can be of many different types."
#encoding
a = s.split(" ")
print(s)
encoded_string_list=[]
for i in a:
    encoded_string_list.append(":;"+str(len(i))+i)
p = "".join(encoded_string_list)
print(p)
#decoding
decoded_list=[]
i=2
while i < len(p):
    length = p[i]
    word = p[i + 1: i+1+int(length)]
    decoded_list.append(word)
    i=i+int(length)+3
decoded_str = " ".join(decoded_list)
print(decoded_str)

#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
nums = [100,4,200,1,1,3,2]
def longestConsecutive(nums: List[int]) -> int:
    if nums == []:
        return 0
    a = sorted(nums)
    count = 1
    lc = []
    print(a)
    for i, n in enumerate(a):
        if i<len(a)-1 and a[i+1]-a[i]==1:
            count+=1
        elif i<len(a)-1 and a[i+1]-a[i]==0:
            continue
        else:
            lc.append(count)
            count=1
    lc.sort(reverse=True)
    res=lc[0]
    return res

def longestConsecutive(nums: List[int]) -> int:
        num_set = set()
        max_length = 0
        #place all items into the set
        for num in nums:
            num_set.add(num)
        
        for num in num_set:
            cur_chain_len = 1
            while num + 1 in num_set:
                cur_chain_len +=1
                num = num + 1
            #if we found a chain as long as the input, were done
            if cur_chain_len == len(num_set):
                return cur_chain_len
            
            #otherwise, update max_length if cur_chain is bigger
            if cur_chain_len > max_length:
                max_length = cur_chain_len
        
        return max_length

def strStr(haystack, needle):
    if needle==haystack:
            return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
def intersection(nums1, nums2):
    res = [x for x in nums1 if x in nums2]
    return set(res)

    set1 = set(nums1)
    set2 = set(nums2)
    return set1 & set2

# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.
# Each element in the result should appear as many times as it appears in both arrays.
# The result can be in any order.
from collections import Counter
def solve(A, B):
    ret = []
    ac = Counter(A)
    bc = Counter(B)
    for i in ac.keys():
        if i in bc.keys():
            minOcc = min(ac[i],bc[i])
            ret.extend([i]*minOcc)
    return ret  

# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1, else return 0.
def solve(self, A):
    count = 0
    set_count = set()
    for a in A:
        count += a
        if count==0 or count in set_count:
            return 1
        set_count.add(count)
    return 0

def customSortString(order, s):
    i=0
    k = []
    k[:] = s
    print(k)
    for o in order:
        if o in s:
            idx = k.index(o)
            print(idx)
            k[i],k[idx] = k[idx],k[i]
            i+=1
    return "".join(k)     
rt = customSortString('cab','abcdef')
print(rt)

def customSortString(order, s):
    result = ""
    mp = {}
    for char in s:
        mp[char] = mp.get(char, 0) + 1
    for char in order:
        if char in mp:
            result += char * mp[char]
            del mp[char]
    for char, count in mp.items():
        result += char * count
    return result

# A beggars sitting in a row and B represents some devotees that give money to beggars from left to right indices(left,right,amount). Find to amount each beggar has at the end.
def solve(A, B):
    arr = [0 for x in range(A)]
    for i in range(0,len(B)):
        left = B[i][0]
        right = B[i][1]
        amount = B[i][2]
        arr[left-1] += amount
        if right!=A:
            arr[right] += -amount
    for i in range(1,len(arr)):
        arr[i]+=arr[i-1]
    print(arr)    

A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
solve(A,B)

#Trapping rain water
def trap(A):
    n = len(A)
    left_max = [0]*n
    left_max[0] = A[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],A[i])
    right_max = [0]*n
    right_max[n-1] = A[n-1]
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],A[i])

    water_trapped = 0
    for i in range(1,n):
        water = min(left_max[i],right_max[i])-A[i]
        water_trapped+=water  
    print(water_trapped)      

A = [1,3,5,4,1,3,2,5,0,5]
trap(A)

# Find the first missing positive integer from an array of unsorted integers both positive and negative in linear time complexity.
def firstMissingPositive(A): 

    def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

    for i in range(0,len(A)):
        while A[i] in range(1,len(A)) and A[i]!=i+1 and A[i] != A[A[i]-1]:
            swap(A, i, A[i] - 1)
    
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    
    return len(A) + 1


#return non-overlapping sorted intervals
def solve(A):
    Ab = []
    for i in sorted(A, key=lambda k: k[0]):
        if Ab and i[0] <= Ab[-1][1]:
            Ab[-1][1] = max(Ab[-1][1], i[1])
        else:
            Ab.append(i)
    return Ab

## return non-overlapping sorted intervals after inserting a new interval into sorted non overlapping intervals.
def insert(A, B):
    ans=[]
    n = len(A)
    if n==0:
        ans.append(B)
    elif B[1]<A[0][0]:
        ans.append(B)
        ans.extend(A) 
    elif B[0] > A[-1][1]:
        ans.extend(A)
        ans.append(B) 
    else:
        i = 0
        while i<n:
            if A[i][1]<B[0]:
                ans.append(A[i])
            else:
                break
            i+=1

        start = B[0]
        end = B[1] 
        i=0
        while i< n:
            if not (start>A[i][1] or end<A[i][0]):
                start = min(start,A[i][0])
                end = max(end,A[i][1])
            else:
                break
            i+=1
        ans.append([start,end])    
        while i<n:
            ans.append(A[i])   
            i+=1 
    print(ans) 

#Range sum queries question
def rangeSum(A, B):
    item = A[0]
    for i in range(1,len(A)):
        A[i]+=item
        item = A[i]
    ans = []
    for j in range(len(B)):
        start = B[j][0]
        end = B[j][1]
        if start ==0:
            ans.append(A[end])
        else:
            ans.append(A[end]-A[start-1])
    print(ans)    

A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
rangeSum(A,B)

#find the equillibrium index where left sum  is equal to right sum
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


#Find sum of all subarray sum in an array { CONTRIBUTION TECHNIQUE }
def subarraySum(A):
    n = len(A)
    total_subarrays_sum = 0
    for num in range(len(A)):
        total_subarrays_sum+=A[num]*(num+1)*(n-num)
    return total_subarrays_sum  


def solve(A):
    ans = []
    prefix = []
    suffix = []
    prefix_product = 1
    suffix_product = 1
    n = len(A)
    for i in range(n):
        prefix_product*=A[i]
        prefix.append(prefix_product)
    for i in range(n):
        suffix_product*=A[n-1-i] 
        suffix.append(suffix_product)
    suffix.reverse()    
    print(prefix)
    print(suffix)
    for i in range(n):
        if i==0:
            ans.append(suffix[i+1])  
        elif i==n-1:
            ans.append(prefix[i-1])    
        else:
            ans.append(prefix[i-1]*suffix[i+1])
    print(ans)        

A = [1, 2, 3, 4, 5]
solve(A)

def solve(A, B):
    left = []
    right =[]
    lsum=0
    rsum = 0
    max_sum = float('-inf')
    for i in range(B):
        lsum+=A[i]
        rsum+=A[-i-1]
        left.append(lsum)
        right.append(rsum)
    for i in range(B+1):
        sum = 0
        if i==0:
            sum = left[-1]
        elif i==B:
            sum = right[-1]  
        else:
            sum = left[B-i-1]  + right[i-1]
        max_sum = max(max_sum,sum)
    print(max_sum)    


A = [5, -2, 3 , 1, 2]
B = 3
solve(A,B)

import math

def solve(A):
    N = len(A)
    pf_even = [0] * N
    pf_odd  = [0] * N
    pf_even[0] = A[0]
    pf_odd[0]  = 0
    
    for i in range(1,N):
        if i & 1:
            pf_even[i] = pf_even[i-1]
            pf_odd[i]  = A[i] + pf_odd[i-1]
        else:
            pf_even[i] = A[i] + pf_even[i-1]
            pf_odd[i]  = pf_odd[i-1]
    print(pf_even)
    print(pf_odd)
    count = 0
    for i in range(N):
        if i == 0:
            even_sum = 0 + (pf_odd[N-1] - pf_odd[i])
            odd_sum  = 0  + (pf_even[N-1] - pf_even[i])
        else:
            even_sum = pf_even[i-1] + (pf_odd[N-1] - pf_odd[i])
            odd_sum  = pf_odd[i-1]  + (pf_even[N-1] - pf_even[i])
        
        if even_sum == odd_sum:
            count += 1
    print(count)
    # odd_sum = []
    # even_sum = []
    # c=0
    # for i in range(len(A)):
    #     if i==0:
    #         even_sum.append(A[i]) 
    #     elif i==1:
    #         odd_sum.append(A[i]) 
    #     elif i%2==0:
    #         even_sum.append(even_sum[-1]+A[i])
    #     else:
    #         odd_sum.append(odd_sum[-1]+A[i])

    # print(even_sum)
    # print(odd_sum)        
    # for i in range(len(A)):
    #     if i==0:
    #         te = odd_sum[-1]
    #         to = even_sum[-1]-even_sum[i]
    #     elif i==1:
    #         te = even_sum[i-1]+odd_sum[-1]-odd_sum[i-1]
    #         to = even_sum[-1]-even_sum[i-1]
    #     else:
    #         te = even_sum[math.ceil((i//2))-1]+odd_sum[-1]-odd_sum[math.ceil((i//2))-1]
    #         to = odd_sum[math.ceil((i//2))-1]+even_sum[-1]-even_sum[math.ceil((i//2))-1]
    #     if to==te:
    #         c+=1
    # print(c)        


# A = [1,1,1]
# solve(A)

# def plusOne(A):
#     strt_z = 0
#     if A==[] or A==[0]:
#         return [1]
#     for i in range(len(A)):
#         if A[i]!=0:
#             break
#         strt_z+=1
#     if A[0]==0 and strt_z==len(A):
#         return [1]  
#     carry = 1
#     for i in range(len(A)-1,-1,-1):
#         sum=A[i]+carry
#         if sum>9:
#             carry=1 
#             if i==0:
#                 A[i] = 1
#                 A.append(0) 
#             else:
#                 A[i] = 0
#         else:
#             carry=0
#             A[i] = sum
#             break
#     ans = A[strt_z:]
#     print(ans)   


# A=[]
# plusOne(A)

def solve(A):
    sum = 0
    mod = pow(10,9)+7
    F=[0]*1001
    print(len(F))
    for k in A:
        F[k]+=1
    for i in range(1,1000):
        for j in range(1,1000):
            val = i % j
            freq = val*F[i]*F[j]
            sum = (sum % mod + freq % mod) % mod
    return sum

f = solve([686,675,758,659,377,965,430,220,599,699])
print(f)