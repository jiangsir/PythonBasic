#最大子序列(Maximum Subarray) #Maximum Subsequence
'''

MSS 法
while (scanf("%d", &N) && N) {
        int Max = 0;
        int MSS = -1;
        while (N--) {
            scanf("%d", &num);
            if (MSS < 0) MSS = num;
            else MSS += num;

            if (MSS > Max) Max = MSS;
        }
        if (Max > 0) printf("The maximum winning streak is %d.\n", Max);
        else puts("Losing streak.");
}
'''

'''
http://mypaper.pchome.com.tw/zerojudge/post/1322986827
非 DP 解法
while(scanf("%d", &n) == 1 && n) {
        int ans = 0, x, tmp = 0;
        while(n--) {
            scanf("%d", &x);
            tmp += x;
            if(tmp < 0)
                tmp = 0;
            if(tmp > ans)
                ans = tmp;
        }
        if(ans)
            printf("The maximum winning streak is %d.\n", ans);
        else
            printf("Losing streak.\n");
'''

'''
DP 解法

'''
import sys

for s in sys.stdin:
    n = int(s)
    if n == 0:
        break
    li = [int(x) for x in input().split()]
    dp = [0 for _ in li]

    dp[0] = li[0]
    for i, x in enumerate(li):
        if i > 0:
            dp[i] = max(x, x + dp[i-1])

    maxn = max(dp)
    if maxn > 0:
        print('The maximum winning streak is ' + str(maxn)+'.')
    else:
        print('Losing streak.')
