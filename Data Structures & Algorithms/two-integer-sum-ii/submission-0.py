class Solution:
    def twoSum(self, number: List[int], target: int) -> List[int]:
        l,r = 0,len(number) - 1

        while l<r:
            curSum = number[l] + number[r]
             
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1,r+1]
        return []
        