class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum=0
        res=0
        preSum=defaultdict(int)

        preSum[0]=1

        for num in nums:
            currSum+=num
            diff = currSum-k

            res+=preSum.get(diff,0)

            preSum[currSum]=1+preSum.get(currSum,0)

        return res

