class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dct = collections.defaultdict(int)
        sum = 0
        cnt = 0
        dct[0] = 1
        
        for num in nums:
            sum += num
            cnt += dct[sum - k]
            dct[sum] += 1
        return cnt
