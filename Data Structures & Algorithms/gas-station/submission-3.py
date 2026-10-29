class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        for i in gas:
            total_gas += i
        
        for i in cost:
            total_cost += i

        if total_cost > total_gas:
            return -1 
        
        index = 0
        gasx = 0

        for i in range(len(gas)):
            gasx += gas[i] - cost[i]
            if gasx < 0:
                index = i + 1
                gasx = 0
        

        
        return index


        
        