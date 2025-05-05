# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 


class SubsetGenerator:
    def get_subsets(self, nums):
        result = []
        self._backtrack(nums, 0, [], result)
        return result

    def _backtrack(self, nums, index, path, result):
        result.append(path[:]) 
        for i in range(index, len(nums)):
            path.append(nums[i])  
            self._backtrack(nums, i + 1, path, result)  
            path.pop()  
            
generator = SubsetGenerator()
print(generator.get_subsets([1,2, 5, 6]))