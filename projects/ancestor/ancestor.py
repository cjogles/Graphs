from util import Stack, Queue  
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
    def __repr__(self):
        return f"nodes = {self.vertices}"
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertice doesn't exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex_id)

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push a starting vertex
            # create a set to store the visited vertices
            # while the stack is not empty
                # pop the first vertex
                # if vertex has not been visited
                    # mark the vertex as visited
                    # print it for debug
                    # add all of it's neighbors to the top of the stack
        s = Stack()
        s.push(starting_vertex_id)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # s = Stack()
        # s.push(starting_vertex_id)
        # visited = set()
        # while s.size() > 0:
        #     v = s.pop()
        #     if v not in visited:
        #         visited.add(v)
        #         print(v)
        #         for next_vertex in self.get_neighbors(v):
        #             s.push(next_vertex)
        print(starting_vertex)
        for index in self.get_neighbors(starting_vertex):
            if index > starting_vertex:
                self.dft_recursive(index)

    def bfs(self, starting_vertex_id, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue PATH To the Starting Vertex ID
            # create a set to store visited vertices
            # while the queue is not empty
            # dequeue the first PATH
            # print("path",path)
                # grab the last vertex from the Path
                # check if the vertex has not been visited
                    # is this vertex the target?
                        # return the path
                    # mark it as visited
                    # then add A Path to its neighbors to the back of the queue
                        # make a copy of the path
                        # append the neighbor to the back of the path
                        # enqueue out new path
                # return none

        q = Queue()
        q.enqueue([starting_vertex_id])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        return None

    def dfs(self, starting_vertex_id, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push PATH To the Starting Vertex ID
            # create a set to store visited vertices
            # while the stack is not empty
                # pop the first PATH
                # grab the last vertex from the Path
                # check if the vertex has not been visited
                    # is this vertex the target?
                        # return the path
                    # mark it as visited
                    # then add A Path to its neighbors to the top of the stack
                        # make a copy of the path
                        # append the neighbor to the back of the path
                        # push out new path
            # return none
        s = Stack()
        s.push([starting_vertex_id])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        path = path + [starting_vertex]
        print(path)
        # whats my base case?
        if path[-1] == destination_vertex:
            return path
        for vertex in self.vertices[starting_vertex]:
            if vertex not in path:
                traced_path = self.dfs_recursive(vertex, destination_vertex, path)
                if traced_path:
                    return traced_path

def earliest_ancestor(ancestors, starting_node):
    # BUILD GRAPH
    graph = Graph()
    created_verteces = set()
    for i in ancestors:
        if i[0] not in created_verteces:
            graph.add_vertex(i[0])
            created_verteces.add(i[0])
        if i[1] not in created_verteces:
            graph.add_vertex(i[1])
            created_verteces.add(i[1])
        graph.add_edge(i[0], i[1])
    print(graph)

    # TRAVERSE GRAPH
    graph.bft(1)

earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 1)

    
    