class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        out = []
        min_val = float('inf') 
       

        for i in range(len(list1)):
            for j in range(len(list2)): 
                if list1[i] == list2[j]:
                    current_sum = i + j
                    if current_sum < min_val:
                        min_val = current_sum
                        out = [list1[i]]
                        
                    elif current_sum == min_val:
                        out.append(list1[i])

        return out
