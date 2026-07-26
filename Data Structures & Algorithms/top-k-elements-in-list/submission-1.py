class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for items in count.keys():
            freq[count[items]].append(items)

        ans = []
        for i in range(len(freq)-1,-1,-1):
            if(freq[i]):
                for j in freq[i]:
                    if(k == 0):
                        break
                    else:
                        ans.append(j)
                        k = k-1


        return ans        

        
        