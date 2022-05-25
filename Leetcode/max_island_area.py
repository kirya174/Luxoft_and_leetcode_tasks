class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        X, Y = len(grid[0]), len(grid)
        max_area = 0
        checked_coordinates = []

        def check_pixels(x, y, cur_size):
            if grid[y][x] == 1 and (x, y) not in checked_coordinates:
                checked_coordinates.append((x, y))
                cur_size += 1
                if x >= 1: cur_size = check_pixels(x - 1, y, cur_size)
                if x + 1 < X: cur_size = check_pixels(x + 1, y, cur_size)
                if y >= 1: cur_size = check_pixels(x, y - 1, cur_size)
                if y + 1 < Y: cur_size = check_pixels(x, y + 1, cur_size)
            return cur_size

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                size = 0
                size = check_pixels(x, y, size)
                if size > max_area:
                    max_area = size
        return max_area


grid = [[0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(grid))  # 1

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(grid))  # 6
