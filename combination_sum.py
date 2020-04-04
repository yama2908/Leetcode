class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        stack = [(0, 0, [])]
        ans = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                ans.append(res)
            for i in range(start, len(candidates)):
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        return ans
