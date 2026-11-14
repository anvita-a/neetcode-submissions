class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i,0) + 1
        freq_sort = sorted(count_dict, key = count_dict.get, reverse = True)
        return freq_sort[0:k] 