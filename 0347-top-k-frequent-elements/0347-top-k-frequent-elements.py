class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        c = dict(sorted(c.items(), key = lambda item:item[1],reverse = True))
        print(c)
        arr = []
        for key in c.keys():
            if k > 0:
                arr.append(key)
                k -= 1
        return arr
            