#LCS #最長共同子字串 #LCS長度

def lcs(s1, s2):
    #return lcsRC(s1, s2)
    return lcsDP(s1, s2)

def lcsRC(s1, s2):
    '''
    遞迴解，非常慢
    '''
    if len(s1)==0 or len(s2)==0:
        return 0
    elif s1[-1] == s2[-1]:
        return lcs(s1[:-1], s2[:-1]) + 1
    else:
        return max(lcs(s1[:-1], s2[:-1]), lcs(s1, s2[:-1]), lcs(s1[:-1], s2))


def lcsDP(s1, s2):
    '''
    建立一個二維陣列記錄過程
    '''
    row = len(s1)
    col = len(s2)
    dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

    if len(s1)==0:
        return dp[0][len(s2)]
    elif len(s2) == 0:
        return dp[len(s1)][0]

    for i in range(1, row+1):
        for j in range(1, col+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                i1 = dp[i-1][j-1]
                i2 = dp[i][j-1]
                i3 = dp[i-1][j]
                dp[i][j] =  max(i1, i2, i3)
    #for s in dp:
        #print(s)
    return dp[row][col]

def lcs3V(s1, s2):
    pass

import sys
for s in sys.stdin:
    print(lcs(s, input()))


assert 0 == lcs('', 'zz')
assert 4 == lcs('a1b2c3d4e', 'zz1yy2xx3ww4vv')
assert 3 == lcs('abcdgh', 'aedfhr')
assert 14 == lcs('abcdefghijklmnzyxwvutsrqpo', 'opqrstuvwxyzabcdefghijklmn')
assert 26 == lcs('abcdefghijklmnopqrstuvwxyz', 'a0b0c0d0e0f0g0h0i0j0k0l0m0n0o0p0q0r0s0t0u0v0w0x0y0z0')

