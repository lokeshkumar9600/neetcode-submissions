class Solution:
    def numDecodings(self, s: str) -> int:

        ways = 0
        def dynamic(i,dp):
            if i == 0:
                return 1
            
            ways = 0

            if dp[i] != -1:
                return dp[i]

            if s[i-1] != '0':
                ways += dynamic(i-1,dp)
            if i >=2 and 10 <= int(s[i-2:i]) <= 26:
                ways += dynamic(i-2,dp)
            
            dp[i] = ways
            return ways


    

        dp = [-1] * (len(s) + 1)
        return dynamic(len(s),dp)











        