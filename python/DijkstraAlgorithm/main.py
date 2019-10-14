class Graph:
    
    def __init__(self, n_v, src, dest, g):
        self.v = n_v
        self.s = src
        self.d = dest
        self.g = g


    def findShortestPath(self):

        distances = [] 
        visited = [False] * self.v 

        for i in range(self.v): 
                distances.append(float("inf"))
        distances[self.s] = 0 

        for x in range(self.v):
            minimum = float("inf")
            for i in range(len(distances)):
                if visited[i] == False and distances[i] < minimum:
                    minimum = distances[i]
                    min_idx = i
            visited[min_idx] = True
    
            if minimum == float("inf"):
                flag = True
                break
    
            for vert in range(len(distances)):
                if not visited[vert]:
                    if distances[vert] > distances[min_idx]+self.g[min_idx][vert] \
                            and self.g[min_idx][vert] != 0:
                        distances[vert] = distances[min_idx]+self.g[min_idx][vert]
            if self.d == min_idx:
                break
        return distances[self.d]


    def printShortestPath(self):
        print("Shortest distance from source vertex {} to destination vertex {} is {}.".format(self.s, self.d, self.findShortestPath()))

    def retShortestPath(self):
        return self.findShortestPath()



if __name__ == '__main__':
    g =  [
            [0, 4, 0, 0, 0, 0, 0, 8, 0], 
            [4, 0, 8, 0, 0, 0, 0, 11, 0], 
            [0, 8, 0, 7, 0, 4, 0, 0, 2], 
            [0, 0, 7, 0, 9, 14, 0, 0, 0], 
            [0, 0, 0, 9, 0, 10, 0, 0, 0], 
            [0, 0, 4, 14, 10, 0, 2, 0, 0], 
            [0, 0, 0, 0, 0, 2, 0, 1, 6], 
            [8, 11, 0, 0, 0, 0, 1, 0, 7], 
            [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
    
    gr = Graph(9,0,4,g)
    gr.printShortestPath()



