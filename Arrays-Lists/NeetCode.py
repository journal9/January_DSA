# from collections import Counter
words = ["eat","tea","tan","ate","nat","bat"]
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

anagram_dict = {}
for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]
print(list(anagram_dict.values()))
       


