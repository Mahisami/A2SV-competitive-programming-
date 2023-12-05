class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()

        max_length = 0
        for word in words:
            max_length = max(max_length, len(word))

        result = []
        for i in range(max_length):
            result.append('')
            

      
        for i in range(max_length):
            for word in words:
                if i < len(word):
                    result[i] += word[i]
                else:
                    result[i] += ' '

        for i in range(max_length):
            result[i] = result[i].rstrip()

        return result