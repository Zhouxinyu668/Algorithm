from typing import List

class Solution:
    def __init__(self):
        self.res = []
    def permute(self , num: List[int]) -> List[List[int]]:
        row = []
        self.backrack(row, num)
        print(self.res)


    def backrack(self, row, num):
        if len(row) == len(num):
            self.res.append(row.copy())
            return 
        
        for i in range(len(num)):
            if num[i] in row:
                continue
            row.append(num[i])
            self.backrack(row,num)
            row.pop()
s = Solution()
s.permute([1])