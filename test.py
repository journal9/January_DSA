#leetcode premium questions

# s = "Arguments can be of many different types."
# #encoding
# a = s.split(" ")
# print(s)
# encoded_string_list=[]
# for i in a:
#     encoded_string_list.append(":;"+str(len(i))+i)
# p = "".join(encoded_string_list)
# print(p)
# #decoding
# decoded_list=[]
# i=2
# while i < len(p):
#     length = p[i]
#     word = p[i + 1: i+1+int(length)]
#     decoded_list.append(word)
#     i=i+int(length)+3
# decoded_str = " ".join(decoded_list)
# print(decoded_str)

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

s = "Hi from here."
enc = encode(s)
print(enc)
dec = decode(enc)
print(dec)
    
    





