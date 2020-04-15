"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("vertex not found")

    def get_neighbors(self, vertex_id):
        
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        qq.enqueue([starting_vertex])

        visited = set()

        while qq.size() > 0:
            path = qq.dequeue()

            if path[-1] not in visited:
                print(path[-1])

                visited.add(path[-1])

                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        st = Stack()
        st.push(starting_vertex)
        
        visited = set()

        while st.size() > 0:
            current = st.pop()
            if current not in visited:
                neighbors = self.get_neighbors(current)
                for neighbor in neighbors:
                      st.push(neighbor)
                print(current)
                visited.add(current)

    def dft_recursive(self, starting_vertex, visited=set(), st=0):
        if st == 0:
            st = Stack()
            st.push(starting_vertex)
        if st.size() > 0:
            current = st.pop()
            if current not in visited:
                neighbors = self.get_neighbors(current)
                for neighbor in neighbors:
                      st.push(neighbor)
                print(current)
                visited.add(current)
            self.dft_recursive(0, visited, st)


    def bfs(self, starting_vertex, destination_vertex):
        qq = Queue()
        qq.enqueue([starting_vertex])

        visited = set()

        while qq.size() > 0:
            path = qq.dequeue()
            if path[-1] == destination_vertex:
                return path

            if path[-1] not in visited:
                print(path[-1])

                visited.add(path[-1])

                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        st = Stack()
        st.push([starting_vertex])
        
        visited = set()

        while st.size() > 0:
            path = st.pop()
            if path[-1] == destination_vertex:
                return path

            if path[-1] not in visited:
                print(path[-1])

                visited.add(path[-1])

                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    st.push(new_path)

    def dfs_ancestor(self, starting_vertex):
      st = Stack()
      st.push([starting_vertex])
      
      visited = set()
      longest_path = []

      while st.size() > 0:
          path = st.pop()
          if len(self.get_neighbors(path[-1])) == 0 and len(path) > len(longest_path):
              if len(longest_path) > 0:
                  longest_path = path
              elif len(longest_path) == 0:
                  longest_path = path
          if len(self.get_neighbors(path[-1])) == 0 and len(path) == len(longest_path):
              if path[-1] < longest_path[-1]:
                  longest_path = path
          if path[-1] not in visited:

              visited.add(path[-1])

              for next_vert in self.get_neighbors(path[-1]):
                  new_path = list(path)
                  new_path.append(next_vert)
                  st.push(new_path)
      return longest_path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), st=0):
        if st == 0:
            st = Stack()
            st.push([starting_vertex])
        
        if st.size() > 0:
            path = st.pop()
            if path[-1] == destination_vertex:
                return path
            if path[-1] not in visited:
                print(path[-1])

                visited.add(path[-1])

                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    st.push(new_path)
            return self.dfs_recursive(0, destination_vertex, visited, st)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
