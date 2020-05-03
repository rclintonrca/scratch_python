from calculator import FileAverageCalculator

"""
Here we use an Adapter pattern to allow a generator object "adapt" to the FileAverageCalculator Class's interface
Notice how we wrapped the object in a class that creates the same interface as the FAC.
"""

class GeneratorAdapter(object):
    def __init__(self, generated_numbers):
        self.generated_numbers = generated_numbers
        
    def close(self):
        pass

    def readline(self):
        try:
            return next(self.generated_numbers)
        except StopIteration:
            return ''

if __name__ == '__main__':
    g = (i  for i in range(1000000))
    ga = GeneratorAdapter(g)
    
    fac_ga = FileAverageCalculator(ga)
    print(fac_ga.average())