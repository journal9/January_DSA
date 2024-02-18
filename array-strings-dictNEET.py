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

#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
from math import floor
def isPalindrome(s: str) -> bool:
        s = s.lower()
        d = [i for i in s if i.isalnum()]
        for i in range(floor(len(d)/2)):
            if d[i]!=d[-i-1]:
                return False
        return True
        #return s[:] == s[::-1]

def isPalindrome(s: str) -> bool:
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        return s[:] == s[::-1]

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

maxArea([1,8,6,2,5,4,8,3,7])

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
