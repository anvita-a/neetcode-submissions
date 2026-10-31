class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = {}
        for i in nums:
            count_freq[i] = count_freq.get(i,0) + 1
        
        lst_sort = sorted(count_freq, key = count_freq.get, reverse = True)
        most_freq = []
        for i in range(k):
            most_freq.append(lst_sort[i])
        return most_freq