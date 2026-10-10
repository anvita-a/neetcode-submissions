class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count [i] = count.get (i, 0) + 1

        sort_lst = sorted(count, key = count.get)
        print(sort_lst)
        lst = []
        for _ in range(k):
            lst.append(sort_lst.pop())
        return lst


        