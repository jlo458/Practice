# Simple OOP Introduction 
# Makes "Fish" class and gradually feeds fish until it becomes "Big" 

class Fish():
  def __init__(self, size, state):
    self.state = state
    self.size = size

  def feed(self): 
    self.size += 1
    if self.size == 5: 
      self.state = "Big"

    print("fish fed")

  def getState(self): 
    return self.state 

  def getSize(self): 
    return self.size


bob = Fish(1, "Small")

print(bob.getState(), "is the size of bob")

while bob.getState() != "Big":
  bob.feed()

print(bob.getState(), "is how big bob is")
