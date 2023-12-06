class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        rows = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}

        lst = []
        for word in words:
            if word.lower()[0] in rows[1]:
                key = rows[1]
            elif word.lower()[0] in rows[2]:
                key = rows[2]
            else:
                key = rows[3]
            flag = True
            for letter in word.lower():
                if letter not in key:
                    flag = False
            if flag:
                lst.append(word)
        return lst
            










        #     flag = True
        #     for letter in word.lower():
        #         print(letter)
        #         if letter not in key:
        #             flag = False
        #     if flag:
        #         print(word)
        #         lst.append(word)
        # return lst

                
            
            
                
