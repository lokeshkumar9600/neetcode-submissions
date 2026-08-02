class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        result = []

        for val,freq in count.items():
            bucket[freq].append(val)
        
        for i in range(len(bucket)-1,-1,-1):
            if k == 0:
                break
            
            if len(bucket[i]) > 0:
                for i in bucket[i]:
                    if(k > 0):
                        result.append(i)
                        k -= 1


        return result

        
        