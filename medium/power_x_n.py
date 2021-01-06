class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        if n == 3:
            return x*x*x
        if n == 4:
            return x*x*x*x
        if n < 0:
            n = -n
            x = 1/x
        r = self.myPow(x, n//2)
        if n%2 == 0:
            return r*r
        else:
            return r*r*x

s = Solution()
r = s.myPow(2.0,10)
print(r)
r = s.myPow(2.0,-2)
print(r)