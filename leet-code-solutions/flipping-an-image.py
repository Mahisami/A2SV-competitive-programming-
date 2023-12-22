class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            image[r].reverse()
            for c in range(len(image)):
                image[r][c] = 0 if image[r][c] == 1 else 1
        return image

        