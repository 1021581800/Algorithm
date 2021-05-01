class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dicts = {}
        for i in answers:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1
        # 把说相同数的   计数

        # 兔子最少 的情况
        res = 0

        for key, value in dicts.items():
            #   整除  3个兔子说了1 ，也就是说 最少有2种颜色兔子， 2+2 =4
            tmp = value // (key + 1)
            #    不等于0说明k+1最少兔子不能满足条件必须+1才能满足
            if value % (key + 1) != 0:
                tmp += 1
                #  真实兔子情况     相加
            res += tmp * (key + 1)
        return res

a = '19'

print(bin(10)[2:])