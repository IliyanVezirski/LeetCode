class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        costumer = []
        costumer_sum = 0
        for i in accounts:
            costumer_sum = 0
            for n in i:
                costumer_sum += n
            costumer.append(costumer_sum)
        return max(costumer)



