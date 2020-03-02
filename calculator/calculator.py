import os
from abc import ABC, abstractmethod

print(os.getcwd())

class AverageCalculator(ABC): 

    def average(self): 
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self): 
        pass

    @abstractmethod
    def next_item(self): 
        pass

    def dispose(self): 
        pass


class FileAverageCalculator(AverageCalculator):

    def __init__(self, file): 
        self.file = file
        self.last_line = self.file.readline() 

    def has_next(self):
        return self.last_line != '' 

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline() 
        return result

    def dispose(self):
        self.file.close()


class MemoryAverageCalculator(AverageCalculator):
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.index = 0    

    def has_next(self) -> bool: 
        return len(self.numbers) > self.index

    def next_item(self) -> int: 
        item = self.numbers[self.index]
        self.index += 1
        return item

    def dispose(self):
        self.index = 0
        return 

fac = FileAverageCalculator(open('data.txt'))
print(fac.average()) # Call the template method



mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(mac.average()) # Call the template method
print(mac.average()) # Call the template method


