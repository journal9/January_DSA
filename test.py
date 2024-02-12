# from math import floor


# s = "A man, a plan, an canal: Panama"
# s2 = s.lower()
# print(s2)
# d = [i for i in s2 if i.isalnum()]
# print(d)
# for i in range(floor(len(d)/2)):
#     if d[i]!=d[-i-1]:
#         print('false')
# print('true')

numbers = [2,7,7,15]
target = 14  
for i , n in enumerate(numbers):
    o = target-n
    numbers[i]=" "
    if o in numbers:
        print(i+1,numbers.index(o)+1)    

    
    





