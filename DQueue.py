'''
Created on Oct 22, 2013

@author: pm429015
'''

class Node:
    
    def __init__(self, value):
        self._value = value
        self._next = None
        self._before = None
        
class DQueue:
    #Dynamic Queue
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def add(self,value):
        #create a new node 
        #check size 
        #if size = 0, head and tail point to the new node
        #else add the new node to the current tail node if have
        #the tail pointer point to the new node
        #size +1
        
        nodeNew = Node(value);
        if self.size == 0:
            self.__tail = nodeNew
            self.__head = nodeNew
        else:
            self.__tail._next = nodeNew
            self.__tail = nodeNew

            
        self.size += 1
        
    def delete(self):
        #check size first
        #if queue isn't empty, head pointer point to its next node
        #size -1
        
        if self.size > 0 :  
            self.__head = self.__head._next
            self.size -=1
        else:
            print "The Queue is empty"
            
    def show(self):
        #check size
        #create a temp pointer call iter that point to head
        #keep loop the next of iter and save the values
        if self.size >0:
            iter = self.__head
            item = ""
            while iter:
                item += " " +str(iter._value)
                iter = iter._next 
            print item
        else:
            print "The Queue is empty"
    
    def tailItem(self):
        tail = self.__tail
        return tail._value
    
    def headItem(self):
        head = self.__head
        return head._value
    
if __name__ == '__main__':
    queue = DQueue()
    queue.add(5)
    queue.add(7)
    queue.add(4)
    queue.add(2)
    queue.delete()
    queue.show()
