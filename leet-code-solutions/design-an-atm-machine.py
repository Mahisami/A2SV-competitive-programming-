
class ATM:
    def __init__(self):
        
        self.cnt = [0, 0, 0, 0, 0]
        self.val = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        
        for i in range(len(banknotesCount)):
            self.cnt[i] += banknotesCount[i]
            # print(self.cnt[i]) // cnt = 0 0 1 2 1

    def withdraw(self, amount: int) -> List[int]:
        
        result = [0, 0, 0, 0, 0]
        
        for j in range(4, -1, -1):
            if self.val[j] <= amount:
                can = amount // self.val[j]
                
                if self.cnt[j] >= can:
                    result[j] = can
                else:
                    result[j] = self.cnt[j]
                    
                amount -= result[j] * self.val[j]

        if amount != 0:
            return [-1]

        for j in range(5):
            self.cnt[j] -= result[j]
        return result

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
