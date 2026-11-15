class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, prev):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and prev <= heights[r][c]:
                visited.add((r, c))
                dfs(r + 1, c, heights[r][c])
                dfs(r - 1, c, heights[r][c])
                dfs(r, c + 1, heights[r][c])
                dfs(r, c - 1, heights[r][c])

        # Atlantic
        visited = set()
        for r in range(rows):
            dfs(r,  0, -1)
        for c in range(cols):
            dfs(0, c, -1)
        atlantic_visited = visited.copy()
        # Pacific
        visited = set()
        for r in range(rows):
            dfs(r, cols - 1, -1)
        for c in range(cols):
            dfs(rows - 1, c, -1)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlantic_visited and (r, c) in visited:
                    res.append([r, c])
        return res