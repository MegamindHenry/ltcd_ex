class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        f = list()
        for x in range(len(nums)):
            for y in f:
                if nums[y] + nums[x] == target:
                    return [x,y]
            f.append(x)

nums = [2,7,11,15]
target = 9

s = Solution()
r = s.twoSum(nums,target)
print(r)