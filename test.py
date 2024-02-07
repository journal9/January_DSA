nums = [100,4,200,1,1,3,2]
if nums == []:
    print(0)
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
print(lc)
print(res)

    
    





