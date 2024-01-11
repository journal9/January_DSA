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