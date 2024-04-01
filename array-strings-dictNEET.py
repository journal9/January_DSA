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