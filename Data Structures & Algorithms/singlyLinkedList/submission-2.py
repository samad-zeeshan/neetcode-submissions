class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        else:
            current = self.head
            count = 0
            
            while count < index:
                current = current.next
                count += 1
            return current.val    

        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        if self.size == 0:
            self.tail = new_node
        
        self.size += 1


    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1


    def remove(self, index: int) -> bool:
        
        if index >= self.size or index < 0:
            return False
        
        else:
            current = self.head
            count = 0

            if index == 0:
                self.head = self.head.next
                if self.size == 1:
                    self.tail = None
                self.size -= 1
                return True
        
            while count < index-1:
                current = current.next
                count += 1
            
            next_node = current.next.next
            current.next = next_node

            if index == self.size-1:
                self.tail = current
            
            self.size -= 1
            return True
    

    def getValues(self) -> List[int]:
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result


            
        
