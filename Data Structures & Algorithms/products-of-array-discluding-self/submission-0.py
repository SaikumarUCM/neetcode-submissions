class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        previous=[1]
        further=[1]

        for i in range(l-1):
            previous.append(previous[-1]*nums[i])

        for i in range(l-1,0,-1):
            further.append(further[-1]*nums[i])
        further=further[::-1]

        res=[]
        for i in range(len(previous)):
            res.append(previous[i]*further[i])

        return res


        