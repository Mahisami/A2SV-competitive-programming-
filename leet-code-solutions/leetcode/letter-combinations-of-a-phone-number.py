
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def phone(i,path):
            if i == len(digits):
                combination.append("".join(path))
                return
            cur = digits[i]

            for j in digit_mapping[cur]:
                path.append(j)
                phone(i+1, path)
                path.pop()
                

        combination = []
        path = []
        phone(0, path)
        return combination

