class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        image = [[[image[i][j], False] for j in range(len(image[0]))] for i in range(len(image))]

        def check_nearest_pixels(r, c):
            color = image[r][c][0]
            image[r][c] = newColor, True
            for i in [1, -1]:
                if 0 <= r + i < len(image) and image[r + i][c] == [color, False]:
                    check_nearest_pixels(r + i, c)
            for j in [1, -1]:
                if 0 <= c + j < len(image[0]) and image[r][c + j] == [color, False]:
                    check_nearest_pixels(r, c + j)

        check_nearest_pixels(sr, sc)
        image = [[image[i][j][0] for j in range(len(image[0]))] for i in range(len(image))]
        return image


image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))  # [[2,2,2],[2,2,0],[2,0,1]]

image = [[0, 0, 0],
         [0, 0, 0]]
sr = 0
sc = 0
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))  # [[2,2,2],[2,2,2]]

image = [[0, 0, 0],
         [1, 0, 0]]
sr = 1
sc = 0
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))  # [[0,0,0],[2,0,0]]
