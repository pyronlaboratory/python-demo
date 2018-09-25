class Pet(object):
  
  num_pets=0

  def __init__(self, name):
    self.name = name
    #self.num_pets += 1
    #num_pets += 1
    Pet.num_pets += 1

  def speak(self):
    print("I'm %s and I've got %d other cute pets along with me in this list"  %(self.name, self.num_pets - 1))


#tuffy = Pet("Tuffy")
#snowy = Pet("Snowy")

#tuffy.speak()
#snowy.speak()

#buggzy = Pet("Bug-Z")

#buggzy.speak()
#tuffy.speak()
