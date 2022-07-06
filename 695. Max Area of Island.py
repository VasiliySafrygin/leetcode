from typing import List, Tuple


class Solution:
    def neighbour(self, i, j, ni, nj):
        _neighbour = []
        if i - 1 >= 0:
            _neighbour.append((i - 1, j))
        if i + 1 < ni:
            _neighbour.append((i + 1, j))
        if j - 1 >= 0:
            _neighbour.append((i, j - 1))
        if j + 1 < nj:
            _neighbour.append((i, j + 1))
        yield _neighbour

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island_sizes: List[int] = []
        islands: List[List[Tuple[int, int]]] = []
        ni = len(grid)
        nj = len(grid[0]) 

        queue: List[Tuple[int, int]] = []
        visited = dict()
        n = 0
        while n <= ni * nj - 1:
            if grid[n // nj][n % nj] == 1 and (n // nj, n % nj) not in visited:
                queue.append((n // nj, n % nj))
                island_sizes.append(0)
                islands.append([])
            n += 1

            while len(queue):
                point = queue.pop()
                visited[point] = 1
                islands[-1].append(point)
                island_sizes[-1] += 1

                for neighbour in self.neighbour(point[0], point[1],  ni, nj):
                    if neighbour not in visited:
                        visited[neighbour] = 1
                        if grid[neighbour[0]][neighbour[1]] == 1:
                            queue.append(neighbour)
        try:
            return max(island_sizes)
        except ValueError:
            return 0


s = Solution()

# r = s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
# print(r)
# assert(r == 6)

r = s.maxAreaOfIsland([[1]])
print(r)
assert(r == 1)

r = s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]])
print(r)
assert(r == 0)

r = s.maxAreaOfIsland([[]])
print(r)
assert(r == 0)