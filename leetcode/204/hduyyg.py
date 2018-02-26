# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/278

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, prime = 0, []
        for i in range(2, n):
            if self.is_prime(prime, i):
                prime.append(i)
                res += 1
        return res

    def is_prime(self, prime, n):
        limit = int(math.sqrt(n))
        for x in prime:
            if x > limit: return True
            if n % x == 0: return False
        return True
