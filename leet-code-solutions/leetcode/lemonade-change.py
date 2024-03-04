class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        c5,c10,c20 = 0,0,0
        
        for i in bills:
            if i == 5:
                c5 += 1
            elif i == 10:
                if c5 > 0:
                    c5 = c5-1
                    c10 = c10+1
                else:
                    return False
            else:
                if c5 > 0 and c10 > 0:
                    c20 += 1
                    c5 -= 1
                    c10 -= 1
                elif c5 >= 3:
                    c5 -= 3
                else:
                    return False                
        return True