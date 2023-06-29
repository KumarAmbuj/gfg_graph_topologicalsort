def Stack():
    stack=[]
    return stack
def isEmpty(s):
    return len(s)==0
def Push(s,data):
    s.append(data)
def Pop(s):
    return s.pop()
def size(s):
    return len(s)

from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalsortutil(self,u,visited,stack):
        visited[u]=True

        for v in self.graph[u]:
            if visited[v]==False:
                self.topologicalsortutil(v,visited,stack)
        Push(stack,u)

    def topologicalsort(self):
        visited=[False]*self.v
        stack=Stack()

        for i in range(self.v):
            if visited[i]==False:
                self.topologicalsortutil(i,visited,stack)

        while(size(stack)):
            print(Pop(stack),end=' ')


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Following is a Topological Sort of the given graph")
g.topologicalsort()