# from collections import Counter
# words = ["eat","tea","tan","ate","nat","bat"]
# anagrams=[]
# for i,k in enumerate(strs):
#     sc = Counter(k)
#     scl = list(sc)
#     scl.sort()
#     print(scl)
#     for p,q in enumerate(anagrams):
#         if scl in q:
#             anagrams[p].append(strs[i])
#         else:
#             anagrams.append(list(strs[i]))
# print(anagrams)     

# anagram_dict = {}
# for word in words:
#     sorted_word = ''.join(sorted(word))
#     if sorted_word in anagram_dict:
#         anagram_dict[sorted_word].append(word)
#     else:
#         anagram_dict[sorted_word] = [word]
# print(list(anagram_dict.values()))
       
# nums = [1,1,1,1,2,3,4,4,4,3,2,3,5,6,6]
# k=3
# cd ={}
# for n in nums:
#     if n in cd.keys():
#         cd[n]+=1
#     else:
#         cd[n]=1
# print(cd)      
# kc = dict(sorted(cd.items(), key=lambda item: item[1],reverse=True))
# print(kc)
# ans = list(kc.keys())
# print(ans[:k])
#from functools import reduce
nums= [1,2,3,4]
# product = reduce((lambda x, y: x * y), nums)
# res = []
# for i,n in enumerate(nums):
#     pd=1
#     for p,q in enumerate(nums):
#         if p!=i:
#             pd*=q
#     res.append(pd)        
# print(res)

res = [1] * (len(nums))
for i in range(1, len(nums)):
    res[i] = res[i-1] * nums[i-1]
postfix = 1
print(len(nums)-1)
for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
print(res)
