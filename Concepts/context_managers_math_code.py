# example of context manager
with open('written.txt') as file:
    content = file.read()
    print(file.closed)
    for c in content:
        print(c)
    print(file.closed)
print(file.closed)

#in-built custom manager

#Function-Based Implementation
from contextlib import contextmanager

@contextmanager
def customContextmanager(text):
    print('statement1')
    try:
        swapped= text.swapcase()
        yield swapped
    except ValueError as e:
        print('an error has occurred')
    finally:
        print('operation is completed')


with customContextmanager('hello WORLD') as ct:
    print(ct)

#class-based implementation
class cloned_list:
    def __init__(self,original:list):
        self.original = original

    def __enter__(self):
        print('entered')
        self.clone = self.original.copy()
        return self.clone
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exiting')
        if exc_type is None:
            print('successfully exiting')
            self.original[:] = self.clone
        else:
            print('Unfortnately, error has occurred.')
        return True

ls = [1,2,3,4]  

with cloned_list(ls) as clst:
    clst.append(1000)
print(ls)

# ts = [3,4,5,6]
# with cloned_list(ts) as clst:
#     clst.append(1000)
#     raise(ValueError)
# print(ts)

import math

w = 4
print(math.ceil(w))
print(math.floor(w))
print(math.pow(w,2))
print(math.sqrt(w))
print(math.isqrt(w))
print(math.factorial(w))


