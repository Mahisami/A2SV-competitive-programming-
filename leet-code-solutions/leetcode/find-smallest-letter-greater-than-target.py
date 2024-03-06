class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x = bisect_right(letters, target)
        print(x)
        if x == 0 or x >= len(letters):
            return letters[0]
        
        
        return letters[x]