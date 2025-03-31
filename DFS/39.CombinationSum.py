from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res


"""
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                dfs(i, target - candidates[i], path + [candidates[i]])
        
        candidates.sort()
        dfs(0, target, [])
        return res
"""      