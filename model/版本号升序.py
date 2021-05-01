class Solution:
    def sortVersion(self, versions):
        # write code here
        nums = versions.split(' ')
        # res = []
        # for i in nums:
        #     res.append(i)

        nums.sort()
        return nums

# s ="3.1 2.2 1.0 6.4 4.5 5.2"
dd = Solution()


print(dd.sortVersion("3.x.0.0 2.y 3.y 6.4 4.5 5.2"))`