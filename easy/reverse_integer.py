class Solution:
    def reverse(self, x: int) -> int:
        n = False
        r = 0
        if x < 0:
            x = -x
            n = True
        while x > 9:
            j = x % 10
            r = r*10+j
            x = x//10
        r = r*10+x
        if n:
            r = -r
        if r > 2**31 - 1 or r < -2**31:
            return 0
        return r


s = Solution()
r = s.reverse(1534236469)
print(r)
r = s.reverse(111)
print(r)
r = s.reverse(120)
print(r)
r = s.reverse(-10)
print(r)
r = s.reverse(-111)
print(r)
r = s.reverse(-120)
print(r)