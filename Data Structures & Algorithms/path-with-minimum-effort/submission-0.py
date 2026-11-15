class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        heap = [[0, 0, 0]] # [difference, i, j]
        visit = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while heap:
            diff, i, j = heapq.heappop(heap)
            if (i, j) in visit:
                continue
            visit.add((i, j))
            if (i, j) == (ROWS - 1, COLS - 1):
                return diff
            for dr, dc in directions:
                newr, newc = i + dr, j + dc
                if (newr < 0 or newc < 0) or newr == ROWS or newc == COLS or (newr, newc) in visit:
                    continue
                newdiff = max(diff, abs(heights[i][j] - heights[newr][newc]))
                heapq.heappush(heap, [newdiff, newr, newc])