class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(3)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

#recursive
def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# inorder(node1)

#iterative
def inorderiter(root):
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif len(stack):
            x = stack.pop()
            print(x.val)
            curr = x.right
        else:
            break

# print("----------------------------")
# inorderiter(node1)

#iterative
def preorderiter(root):
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            print(curr.val)
            curr = curr.left
        elif len(stack):
            x = stack.pop()
            curr = x.right
        else:
            break
# print("----------------------------")
# preorderiter(node1)

def postorderiter(root):
    if not root:
        return None
    s1 = []
    s2 = []
    s1.append(root)
    while len(s1):
        x = s1.pop()
        s2.append(x)
        if x.left:
            s1.append(x.left)
        if x.right:
            s1.append(x.right)
    while len(s2):
        x = s2.pop()
        print(x.val)

# print("-----------------------")
# postorderiter(node1)


#construct a binary tree from inorder and preorder
import sys
sys.setrecursionlimit(10**6)

def buildTree(A, B):
    if len(B)==1:
        root = TreeNode(B[0])
        return root
    mp = {x:i for i, x in enumerate(B)}
    return build(B,A,0,len(B)-1,0,len(A)-1,mp)

def build(inr,pre,ist,ie,ps,pe,mp):
    if ist>ie:
        return
    root_val = pre[ps] 
    root = TreeNode(root_val)
    id = mp[root_val]
    cnt = id - ist
    root.left = build(inr,pre,ist,id-1,ps+1,ps+cnt,mp)
    root.right = build(inr,pre,id+1,ie,ps+cnt+1,pe,mp)
    return root

# Inorder = [4,2,5,1,6,3,7]
# Preorder = [1,2,4,5,3,6,7]
# x = buildTree(Preorder,Inorder)


n1 = TreeNode(11)
n2 = TreeNode(12)
n3 = TreeNode(13)
n4 = TreeNode(14)
n5 = TreeNode(15)
n6 = TreeNode(16)
n7 = TreeNode(17)
n8 = TreeNode(18)
n9 = TreeNode(19)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9



# A = n1

def inorderr(A):
    if A==None:
        return None
    inorder(A.left)
    print(A.val)
    inorder(A.right)
    return
# inorderr(A)

def inorderItt(A):
    st = []
    if A==None:
        return None
    curr = A
    st.append(curr)
    curr=curr.left
    while True:
        if curr:
            st.append(curr)
            curr = curr.left
        elif len(st):
            p = st.pop()
            print(p.val)
            curr = p.right
        else:
            break
# inorderItt(A)

def postorderItt(A):
    st = []
    if A==None:
        return None
    curr = A
    st.append(curr)
    curr=curr.left
    while True:
        if curr:
            st.append(curr)
            curr = curr.left
        elif len(st):
            p = st[-1]

            curr = p.right
        else:
            break

from collections import deque,defaultdict
def levelOrder(A):
    queue = deque()
    ans = ''
    queue.append(A)
    while queue:
        size = len(queue)
        for _ in range(size):
            p = queue.popleft()
            ans = ans + ' ' + str(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        ans+='\n'
    return ans


# z = levelOrder(A)
# print(z)

def rightView(A):
    q = deque()
    right = []
    q.append(A)
    while q:
        size = len(q)
        rt = 0
        for _ in range(size):
            a = q.popleft()
            if a.left: q.append(a.left)
            if a.right: q.append(a.right)
            rt = a.val
        right.append(rt)
    return right

# vr = rightView(A)
# print(vr)

def verticalOrderTopView(A):
    position = {A:0}
    v_line = defaultdict(list)
    q = deque()
    q.append(A)
    v_line[0].append(A.val)
    ans=[]
    while q:
        p = q.popleft()
        if p.left:
            position[p.left] = position[p]-1
            v_line[position[p.left]].append(p.left.val)
            q.append(p.left)
        if p.right:
            position[p.right] = position[p]+1
            v_line[position[p.right]].append(p.right.val)
            q.append(p.right)
    disttt = sorted(v_line.keys())
    min = disttt[0]
    max = disttt[-1]
    for dis in range(min,max+1):
        ans.append(v_line[dis][0])
    return ans


# vv = verticalOrderTopView(A)
# print(vv)

def checkHeight(A):
    if A==None:
        return 0
    l = checkHeight(A.left)
    r = checkHeight(A.right)
    ht = max(l,r) + 1
    return ht

# h = checkHeight(A)
# print(h)

def heightbalanced(A):
    if A==None:
        return 0
    l = checkHeight(A.left)
    r = checkHeight(A.right)
    ht = max(l,r) + 1
    if abs(l-r)>1:
        return 'imbalanced'
    return ht

# hb = heightbalanced(A)
# print(hb)



#------------------------------------------------------------------------------------------------------------------
#BST
n10 = TreeNode(20)
n11 = TreeNode(14)
n12 = TreeNode(22)
n13 = TreeNode(12)
n14 = TreeNode(16)
n15 = TreeNode(21)
n16 = TreeNode(25)
n17 = TreeNode(11)
n18 = TreeNode(15)
n19 = TreeNode(18)

n10.left = n11
n10.right = n12
n11.left = n13
n11.right = n14
n12.left = n15
n12.right = n16
n13.left = n17
n14.left = n18
n14.right = n19

A = n10
def bstSearch(A,x):
    while A!=None:
        if x==A.val:
            return True
        if x<A.val:
            A = A.left
        else:
            A = A.right
    return False


# z = bstSearch(A,16)
# print(z)

def solve(A):
    # create tree from preorder traversal
    imin = float('-inf')
    amax = float('inf')
    for i in range(1,len(A)):
        if A[i]>A[i-1]:
            imin = A[i-1]
        if A[i]<=A[i-1]:
            amax = A[i-1]
        if A[i]>=imin and A[i]<=amax:
            continue
        else:
            return "NO" 
    return "YES"
# i = solve([1,5,6,4])
# print(i)

def t2Sum(A, B):
    found = []
    def fill(A,B,stat):
        if A==None or stat==1:
            return
        if B - A.val in found:
            stat=1
        else:
            found.append(A.val)
        fill(A.left,B,stat)
        fill(A.right,B,stat)
        return stat
    return fill(A,B,0)

t = t2Sum(A,30)
print(t)