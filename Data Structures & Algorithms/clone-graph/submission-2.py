"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        visited = set()
        stack = [node]
        old_to_new = {} # Node(old) -> Node(new)

        while stack:
            cur = stack.pop()
            visited.add(cur)
            old_to_new[cur] = Node(cur.val)

            for nei in cur.neighbors:
                if nei in visited: continue
                stack.append(nei)
        
        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])

        return old_to_new[node]