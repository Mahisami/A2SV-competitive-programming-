class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        total,l, res = 0,0, 0
        for i in range(len(fruits)):
            count[fruits[i]] += 1
            total += 1
            while len(count) > 2:
                f = fruits[l]

                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)
            res = max(res, total)
        return res

                
        