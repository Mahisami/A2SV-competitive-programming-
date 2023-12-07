

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            other = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if other <= dist:
                return False
        
        return True
