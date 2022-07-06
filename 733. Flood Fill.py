from typing import List


def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)            

class Solution:
    def neighbour(self, x, y, n, m):
        _neighbour = []
        if x - 1 >= 0:
            _neighbour.append((x - 1, y))
        if x + 1 < n:
            _neighbour.append((x + 1, y))
        if y - 1 >= 0:
            _neighbour.append((x, y - 1))
        if y + 1 < m:
            _neighbour.append((x, y + 1))
        return _neighbour
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        mask_color = image[sr][sc]
        image[sr][sc] = newColor
        m = len(image[0])
        n =  len(image)

        queue = []
        visited = [(sr, sc)]
        queue.append((sr, sc))
        while len(queue):
            point = queue.pop()
            image[point[0]][point[1]] = newColor

            for neighbour in self.neighbour(point[0], point[1],  n, m):
                if neighbour not in visited:
                    visited.append(neighbour)
                    if image[neighbour[0]][neighbour[1]] == mask_color:
                        queue.append(neighbour)      
        return image
s = Solution()

# r = s.floodFill(image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, newColor=2 )
# print(r)
# assert(r == [[2,2,2],[2,2,0],[2,0,1]])

r = s.floodFill(image=[[0,0,0],[0,0,0]], sr=0, sc=0, newColor=2 )
print(r)
assert(r == [[2,2,2],[2,2,2]])