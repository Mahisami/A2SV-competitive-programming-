class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)

        if len_p > len_s: return []
        left, right = 0, len(p)
        p_set = Counter(p)
        s_set = Counter(s[:right])
        sol = []
        if p_set & s_set == p_set: sol.append(0)
        while (right<len_s):
            if s_set[s[left]]==1:
                del s_set[s[left]]
            else:
                s_set[s[left]]-=1

            if s[right] not in s_set:
                s_set[s[right]] = 1
            else:
                s_set[s[right]] += 1
            if p_set & s_set == p_set:
                sol.append(left+1)
            left+=1
            right+=1

        return sol




