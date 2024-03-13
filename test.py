def lengthOfLongestSubstring(s):
    l,r = 0,0
    k = []
    k[:] = s
    max_sbstr = 0
    substr = []
    while r<len(k):
        if k[r] in substr:
            ids = substr.index(k[r])
            substr[:] = substr[ids+1:]
            idx = k.index(k[r])
            l=idx+1  
        substr.append(k[r])
        max_sbstr = max(max_sbstr,len(substr))
        r+=1
    print(max_sbstr)
    return True

st= "abcabcdekbb"
kt = lengthOfLongestSubstring(st)
