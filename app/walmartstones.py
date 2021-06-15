n=int(input())
a=list(map(int,input().split()))
b=[9999999]*n
b[0]=0
b[1]=abs(a[1]-a[0])
for i in range(2,n):
	for j in range(i-1,-1,-1):




    for(int i = 2; i < n; i++){
      for(int j = i - 1, jump = 0; j  >= 0 && jump < k; j--, jump++){
        dp[i] = min(dp[i], dp[j] + abs(h[j] - h[i]));
      }
    }	