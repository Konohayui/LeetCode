class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        balance = 0
        gas_usage = 0
        
        for i in range(len(gas)):
            travel_cost = gas[i] - cost[i]
            balance += travel_cost
            gas_usage += travel_cost
            
            if balance < 0:
                balance = 0
                start = i + 1
            
        if gas_usage >= 0:
            return start
        return -1
        
