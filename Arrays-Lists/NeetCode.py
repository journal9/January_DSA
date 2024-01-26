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
# from functools import reduce
# nums= [1,2,0,3,4]
# product = reduce((lambda x, y: x * y), nums)
# res = []
# for i,n in enumerate(nums):
#     if n!=0:
#         res.append(product//n)  
#     else:
#         temp =nums.copy()
#         temp.pop(i)
#         res.append(reduce((lambda x, y: x * y), temp))     
# print(res)

# res = [1] * (len(nums))
# for i in range(1, len(nums)):
#     res[i] = res[i-1] * nums[i-1]
# postfix = 1
# print(len(nums)-1)
# for i in range(len(nums) - 1, -1, -1):
#     res[i] *= postfix
#     postfix *= nums[i]
# print(res)


# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]

# r_dict= {k: [] for k in range(9)}
# c_dict = {k: [] for k in range(9)}
# for i,n in enumerate(board):
#     for j,m in enumerate(n):
#         if m!= '.':
#             c_dict[j].append(m)
#             r_dict[i].append(m)
# print(r_dict)
# print(c_dict)
# a={'abc':34,"acb":24,"fgh":98}

# B = {i:j*2 for i, j in a.items()}
# print(B)

# xz = "This is my page"
# ab = xz.split('s')
# print(ab)