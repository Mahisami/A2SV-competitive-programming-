class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        min_len = float("inf")

        for i, card in enumerate(cards):
            if card in d:
                min_len = min(min_len, i - d[card] + 1)
            d[card] = i

        return min_len if min_len != float("inf") else -1