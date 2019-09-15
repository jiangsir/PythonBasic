# 遞迴 #permutation #排列 #排列組合

'''
perm(abc):


'''

ans = []


def perm(L, R):
    '''
    遞迴法
    '''
    if L == R:
        ans.append(s[:R])
        return
    else:
        for i in range(L, R):
            s[L], s[i] = s[i], s[L]
            perm(L+1, R)
            s[L], s[i] = s[i], s[L]

s = ['A', 'B', 'C', 'D']
perm(0, 4)

for a in ans:
    print(*a)
