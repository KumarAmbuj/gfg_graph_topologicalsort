from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topological(self,u,visited,count,l):
        visited[u]=True

        for v in self.graph[u]:
            if visited[v]==False:
                self.topological(v,visited,count,l)
        l[count[0]]=u
        count[0]+=1



    def findtopological(self):
        l=[-1 for i in range(self.v)]
        count=[0]

        visited=[False for i in range(self.v)]

        for i in range(self.v):
            if visited[i]==False:
                self.topological(i,visited,count,l)

        for i in range(len(l)-1,-1,-1):
            print(l[i],end=' ')


g=Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
g.findtopological()


