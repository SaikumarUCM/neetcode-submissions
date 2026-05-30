class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        
        for key,value in enumerate(nums):
            if target-value in hashmap and hashmap[target-value]!=key:
                return [hashmap[target-value], key]
            hashmap[value]=key

        