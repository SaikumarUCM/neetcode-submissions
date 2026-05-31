from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)
        heap=[]
        topk=[]

        for i in nums:
            res[i]=1+res.get(i,0)

        for key,value in res.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)

        for i in range(k):
            topk.append(heapq.heappop(heap)[1])
        
        return topk
        