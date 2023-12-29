class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        li = []
        if num == 0:
            return 0
        if num <= 0:
            for i in str(num)[1:]:
                li.append(int(i))
            
            li.sort(reverse = True)
            smallest_num = 0-int(''.join(map(str, li))) 
            return smallest_num    
        else:
            for i in str(num):
                li.append(int(i))
            li.sort()
            if li[0]==0:
                for i in range(1,len(li)):
                    if li[i] != 0:
                        li[0], li[i] = li[i], li[0]
                        break
        smallest_num = int(''.join(map(str, li)))
        return smallest_num

           