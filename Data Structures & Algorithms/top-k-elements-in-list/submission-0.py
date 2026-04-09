class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1

        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)


    # Step 3: take top k numbers
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result