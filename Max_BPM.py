import copy

class ResidualGraph:
    # Attribute graph is adjacency matrix representation of the residual graph (with capacity values).
    # Attribute s is source node, and t is sink node
    def __init__(self, graph, s, t):
        self.graph = graph
        self.numVertices = len(graph)
        self.s = s
        self.t = t

    def get_augmenting_path(self, parent):
        """Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path."""

        # Mark all the vertices as not visited
        visited = [False] * self.numVertices

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        visited[self.s] = True
        queue.append(self.s)
        # Standard BFS loop
        while len(queue) > 0:
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] is False) and (val > 0):
                    visited[ind] = True
                    queue.append(ind)
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[self.t]

    def ford_fulkerson(self):
        """Returns the maximum flow from s to t in the given graph"""

        # This list is filled by get_augmenting_path to store path
        parent = [-1] * self.numVertices

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.get_augmenting_path(parent):

            # Find minimum residual capacity of the edges along the
            # path obtain via get_augmenting_path. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            x = self.t
            while x != self.s:
                path_flow = min(path_flow, self.graph[parent[x]][x])
                x = parent[x]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and the reverse edges
            # along the path
            v = self.t
            while v != self.s:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


class BipartiteGraph:
    def __init__(self, graph, L, R):
        # incidence matrix representation (note: edges only go from L to R, not from R to L!)
        self.graph = graph
        # L is the list of vertices in the left partite set and this set of vertices is [0,|L| - 1]
        self.L = L
        # R is the list of vertices in the right partite set and this set of vertices is [|L|, |L| + |R| - 1]
        self.R = R


    def get_flow_network_rep(self) -> ResidualGraph:
        """Gets the flow network representation of the current bipartite graph"""
        # The row of the (newly-added) source node that will be added to IM
        source_row = [0]*(len(self.graph) + 2)
        # The row of the (newly-added) sink node that will be added to IM
        sink_row = [0]*(len(self.graph) + 2)
        for x in self.L:
            source_row[x] = 1

        for idx, _ in enumerate(self.graph):
            self.graph[idx] = self.graph[idx] + [0, 0]

        self.graph.append(source_row)
        self.graph.append(sink_row)

        for x in self.R:
            self.graph[x][len(self.graph) - 1] = 1

        return ResidualGraph(self.graph, len(self.graph) - 2, len(self.graph) - 1)

    def get_max_bpm(self):
        """Returns maximum bipartite matching"""
        graph_IM_copy = copy.deepcopy(self.graph)
        max_bpm = [-1]*len(self.L)
        FNR = self.get_flow_network_rep()
        FNR.ford_fulkerson()
        for x in self.L:
            for idx in range(len(self.L), len(self.L) + len(self.R)):
                if graph_IM_copy[x][idx] == 1 and FNR.graph[x][idx] == 0:
                    max_bpm[x] = idx

        return max_bpm
