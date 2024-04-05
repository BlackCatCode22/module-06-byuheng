"""
class PartyAnimal:

  def __init__(self):
    self.x = 0
    print('I am constructed')

  def party(self):
    self.x = self.x + 1
    print('So far', self.x)

  def __del__(self):
    print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
"""
class PartyAnimal:

  def __init__(self, nam):
    self.x = 0
    self.name = nam
    print(self.name, 'constructed')

  def party(self):
    self.x = self.x + 1
    print(self.name, 'party count', self.x)


s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jim')

j.party()
s.party()