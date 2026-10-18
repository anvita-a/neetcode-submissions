class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        lst = []
        for i in range(len(arr)):
            if (i != 0) and (arr[i] == arr[i-1]):
                continue
            fixed = i
            sum_two = -arr[fixed]
            l = i + 1
            r = len(arr) - 1

            while (l < r):
                if (arr[l] + arr[r]) > sum_two:
                    r -= 1
                elif (arr[l] + arr[r]) < sum_two:
                    l += 1
                else:
                    lst.append([arr[l], arr[r], arr[fixed]])
                    r -= 1
                    l += 1

                    while (arr[l] == arr[l-1]) and l < r:
                        l += 1
                    while (l < r) and (arr[r] == arr[r+1]) :
                        r -= 1
        return lst
       


        
        