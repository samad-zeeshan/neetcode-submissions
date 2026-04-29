class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        if self.capacity > 0:
            self.array = [None]*self.capacity
        else:
            raise Exception("Capacity has to be greater than zero.")


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        val = self.array[self.size - 1]
        self.size -= 1
        self.array[self.size] = None  
        return val
 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_array = [None]*new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity    

        
    def getSize(self) -> int:
        return self.size

        
    
    def getCapacity(self) -> int:
        return self.capacity
