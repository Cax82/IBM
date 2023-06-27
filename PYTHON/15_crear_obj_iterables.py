

rep = Repetidor(3, )
def __init__(self, veces, item):
      self.veces = veces
      self.item = item
      self.counter = 0

def __next__(self):
      if self.counter == self.veces:
            raise StopIteration('Iterador consumido')
            
      self.counter += 1
      return self.item

      def __iter__(self):
            return self

for r in Repetidor(3, 'Python!'):
     print(r, end=' ')