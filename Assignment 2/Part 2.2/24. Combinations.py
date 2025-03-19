#Problem 77

class Solution:
    def combine(self, n: int, k: int):
        result = []
        self.backtrack(1, n, k, [], result)
        return result
    
    def backtrack(self, start, n, k, combination, result):
        if len(combination) == k:
            result.append(combination[:])
            return
        
        for i in range(start, n + 1):
            combination.append(i)
            self.backtrack(i + 1, n, k, combination, result)
            combination.pop()