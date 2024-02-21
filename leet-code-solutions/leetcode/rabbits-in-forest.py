class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # for i in range(len(answers)):
        #     if answers[i] 
        cnt = Counter(answers)
        out = 0

        for key, val in cnt.items():
            group = key + 1
            x = ceil(val/group)
            out += x * group
        return out
        
        
            # print(group)
            # if group not in s:
            #     s.add(group)
            # else:
                
            #     x += s[group]
            #     print(x)
                
                    
                




            
        print(group)
            

        
        # print(x)
        # x = x + 1

        # print(cnt)
        # for i in range(len(answers)):

            

        
        