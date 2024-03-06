class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        d = [0]*(n+1)

        d[0] = customers.count("Y")
        for i in range(n):
            if customers[i] == "N":
                d[i+1] = d[i] + 1
            else:
                d[i+1] = d[i] - 1
        return d.index(min(d))
        