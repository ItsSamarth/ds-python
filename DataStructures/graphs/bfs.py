# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

from collections import defaultdict


class Graph:

    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to a graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        # mark all the vertices as non visited
        visited = [False] * (len(self.graph))

        # create a queue for bfs
        queue = []

        # mark the source node as visisted and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex from the queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # get all the adjacent vertices of the dequeue vetex
            # If adjacent is not visited then enqueue it and mark it visited
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)
