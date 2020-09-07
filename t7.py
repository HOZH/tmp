from __future__ import annotations

from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        tree = defaultdict(list)
        back = defaultdict(list)
        v = set()
        order = dict()
        low = dict()
        self.current_order = 0

        for i, j in connections:

            if i not in graph[j]:
                graph[j].append(i)
            if j not in graph[i]:
                graph[i].append(j)

            v.add(i)
            v.add(j)

        visited = set()

        v = list(v)

        # stack = deque([v.pop()])

        def dfs(c):
            # print(c)
            order[c] = self.current_order
            self.current_order += 1
            for i in graph[c]:

                if i not in visited:
                    if i not in tree[c] and c not in tree[i]:
                        tree[c].append(i)

                        visited.add(i)
                        dfs(i)

        def helper(current, limit, reached):
            if current in reached:
                return 1e9
            reached.add(current)

            for current_node in graph[current]:
                if order[current_node] <= limit:
                    return order[current_node]
                else:
                    temp_reachable = helper(current_node, limit, reached)
                    if temp_reachable <= limit:
                        return temp_reachable

            return 1e9

        result = []

        temp = v.pop()
        visited.add(temp)
        dfs(temp)
        for i in tree.keys():
            for j in tree[i]:
                graph[i].remove(j)
                graph[j].remove(i)

                flag = helper(j, order[i], set())
                if flag == 1e9:
                    result.append([i, j])

                graph[i].append(j)
                graph[j].append(i)
        return result

        # do dfs to construct a tree

        # for every tree edge if the lower level it points to doesn't have a back edge jumps higher than its higher level
        # then it's a critical edge


t = Solution()
# print(t.criticalConnections(3, [[1, 2], [2, 0], [1, 3]]
#                             ))

# print(t.criticalConnections(6,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))

from time import time

t1=time()
print(t.criticalConnections(10000,aa))
print(time()-t1)