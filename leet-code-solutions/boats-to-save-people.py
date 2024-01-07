class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l = 0
        r = len(people) - 1
        cnt = 0
        
        while r >= l and l < len(people)-1:
            
            if people[r] == limit:
                cnt += 1
                r -= 1
            if people[r] + people[l] <= limit:
                cnt += 1
                r -= 1
                l += 1
            else:
                cnt += 1
                r -= 1
          
        return cnt
                
                
                
         
        

        