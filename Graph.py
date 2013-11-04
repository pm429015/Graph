'''
Created on Oct 26, 2013

@author: pm429015
'''

from DQueue import DQueue

class Edge:
    def __init__(self, v1, v2, value):
        self.__v1 = v1
        self.__v2 = v2
        self.__value = value
        
    def v1(self):
        return self.__v1
    def v2(self):
        return self.__v2
    def value(self):
        return self.__value
    def valueset(self, set):
        self.__value = set
    
class Graph:
    def __init__(self):
        self.__dict = {}
        
    def edgeAdd(self, V1, V2, cost):
        # first check if v1 is a key in the dict or not
            # if v1 exist in dict, check if v2 in the v1 dict or not
            # if not exist, add it
        # if v1 isn't exist in the dict, add it and create key for v2
        
        if self.__dict.has_key(V1):
            if self.__dict[V1].has_key(V2) == False:
                self.__dict[V1][V2] = cost
        else:
            self.__dict[V1] = {}
            self.__dict[V1][V2] = cost
        
    def show(self):
        print self.__dict
    
    def __outputCheck(self, output, key):
        # helper function for DFS and BFS to check if the vector has been visited before
        for vector in output:
            if vector == key:
                return True
        return False
    
        
    def DFS(self, start):
        output = []
        stack = []
        if self.__dict.has_key(start):
            stack.append(start)
            while len(stack) > 0:
                # if the laste vector in the stack isn't output yet
                if  self.__outputCheck(output, stack[-1]) == False:
                    output.append(stack[-1])
                    stack.pop()
                    # if the latest item is in the dict 
                    if self.__dict.has_key(output[-1]):
                        for key in self.__dict[output[-1]].keys():
                            if self.__outputCheck(output, key) == False:
                                stack.append(key)

                else:
                    # the vector is already in the output
                    stack.pop()
        else:
            print 'The start point is not exist'
        
        print 'DFS ', output
        
        
    def BFS(self, start):
        queue = DQueue()
        output = []
        if self.__dict.has_key(start):
            queue.add(start)
            while queue.length() > 0:
                # if the laste vector in the queue isn't output yet
                if  self.__outputCheck(output, queue.headItem()) == False:
                    output.append(queue.headItem())
                    queue.delete()
                    if self.__dict.has_key(output[-1]):
                        for key in self.__dict[output[-1]].keys():
                            if self.__outputCheck(output, key) == False:
                                queue.add(key)
                else:
                    # the vector is already in the output
                    queue.delete()
        else:
            print 'The start point is not exist'
        
        print 'BFS ', output
        
    def edgeinsertsort(self, sortedEddge, edge):
        sortedEddge.append(edge)
        i = len(sortedEddge) - 1
        j = len(sortedEddge) - 2
        # if sortedEddge is empty break
        # else start insert sort
        while i > 0:
            if sortedEddge[i].value() > sortedEddge[j].value() :
                # swap
                temp = sortedEddge[i]
                sortedEddge[i] = sortedEddge[j]
                sortedEddge[j] = temp
                i -= 1
                j -= 1
                
            else:
                break

    def findset(self,joinset,key):
        #helper function for Kruskal
        original = 0
        weight = 0
        if joinset[key] < 0:
            return (key,joinset[key])
        else:
            original, weight = self.findset(joinset, joinset[key]) 
            return (original,weight)
         
            
    def Kruskal(self):
        # please visit for more informaion http://www.cs.usfca.edu/~galles/visualization/Kruskal.html
        # create an dict to store disjoint set with all -1
        # add edge to an array and sort it
        joinSet = {}
        sortedEddge = []
        for i in self.__dict.keys():
            if joinSet.has_key(i) == False:
                joinSet[i] = -1
            for j in self.__dict[i].keys():
                edge = Edge(i, j, self.__dict[i][j])
                self.edgeinsertsort(sortedEddge, edge)
                if joinSet.has_key(j) == False:
                    joinSet[j] = -1
        #loop the sorted array until empty          
        while len(sortedEddge) != 0:
            # check cycle
            v1_from, v1_weight = self.findset(joinSet, sortedEddge[-1].v1())
            v2_from, v2_weight = self.findset(joinSet, sortedEddge[-1].v2())
            #if two vectors are not equal
            if v1_from != v2_from:
                # the small weight vector will be assigned to large weight vector
                if v1_weight <= v2_weight:
                    joinSet[v1_from] = v2_from
                    joinSet[v2_from] +=  v1_weight
                else:
                    joinSet[v2_from] = v1_from
                    joinSet[v1_from] +=  v2_weight
                print sortedEddge[-1].v1(), sortedEddge[-1].v2(),sortedEddge[-1].value()
            sortedEddge.pop()
            
    def Prim(self):
        # first sort the edges and gather all vectors  
        joinSet = {}
        sortedEddge = []
        record = []
        for i in self.__dict.keys():
            if joinSet.has_key(i) == False:
                joinSet[i] = -1
            for j in self.__dict[i].keys():
                edge = Edge(i, j, self.__dict[i][j])
                self.edgeinsertsort(sortedEddge, edge)
                if joinSet.has_key(j) == False:
                    joinSet[j] = -1
                    
        edgecheck=[-1]*(len(sortedEddge)-1)
        # in the beginning , insert the smallest edge to record
        length = len(joinSet)
        record.append(sortedEddge[-1].v1())
        record.append(sortedEddge[-1].v2())
        print sortedEddge[-1].v1(), sortedEddge[-1].v2(),sortedEddge[-1].value()
        sortedEddge.pop()

        while len(record) != length:
            # since no direction graph, I check both vectors
            for edge in range(len(sortedEddge)-1,-1,-1):
                if sortedEddge[edge].v1() in record and edgecheck[edge] == -1:
                    record.append(sortedEddge[edge].v2())
                    print sortedEddge[edge].v1(), sortedEddge[edge].v2(),sortedEddge[edge].value()
                    edgecheck[edge] = 1
                    break  
                elif sortedEddge[edge].v2() in record and edgecheck[edge] == -1:
                    record.append(sortedEddge[edge].v1())
                    print sortedEddge[edge].v1(), sortedEddge[edge].v2(),sortedEddge[edge].value()
                    edgecheck[edge] = 1
                    break 



graph = Graph()
graph.edgeAdd(0, 1, 1)
graph.edgeAdd(2, 0, 3)
graph.edgeAdd(0, 4, 1)
graph.edgeAdd(1, 3, 4)
graph.edgeAdd(1, 5, 9)
graph.edgeAdd(1, 6, 7)
graph.edgeAdd(5, 2, 7)
graph.edgeAdd(6, 2, 3)
graph.edgeAdd(4, 7, 6)
graph.edgeAdd(7, 5, 2)

graph.show()

# graph.DFS(1)
# graph.BFS(1)
# graph.Kruskal()
# graph.Prim()


