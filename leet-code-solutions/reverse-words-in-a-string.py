class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        words = s.split(" ")
        right = len(words) - 1

        while right >= 0:
            
            stripped_word = words[right].strip() 
            if stripped_word:  
                output += stripped_word + " "
            right -= 1
        return output.strip()  

