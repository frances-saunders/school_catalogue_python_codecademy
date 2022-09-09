#This fulfills the reqs for the "School Catalogue" project in Python in Codecademy

class School:
  
  def __init__(self, name, level, numberOfStudent):
    self.name = name
    self.level = level
    self.numberOfStudent = numberOfStudent

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudent

  def set_numberOfStudents(self, new_amount):
    self.numberOfStudents = new_amount

  def __repr__(self):
    return f"A {self.level} school named {self.name} has {self.numberOfStudent} students."



class PrimarySchool(School):
  def __init__(self, name, numberOfStudent, pickuppolicy):
    super().__init__(name, 'primary', numberOfStudent)
    self.pickuppolicy = pickuppolicy

  def get_policy(self):
    return self.pickuppolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "\nThe pickup policy is as follows: {pickupPolicy}".format(pickupPolicy = self.pickuppolicy)


mySchool = School("Washington High", "high", "647")
print(mySchool)
print("Name of School: " + mySchool.get_name())
print("School Level: " + mySchool.get_level() + " school")
print("Number of Students: " + mySchool.get_numberOfStudents())

print('\n')

testSchool = PrimarySchool("Jones Elementary", 258, "Pickup must be done by a parent or guardian over the age of 16.")
print(testSchool)
print('\n')

class HighSchool(School):
  def __init__(self, name, numberOfStudent, sportsTeams):
    super().__init__(name, 'high', numberOfStudent)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    return self.sportsTeams
  def __repr__(self):
    parent = super().__repr__()
    return parent + f" We currently offer the following sports - {self.sportsTeams}"

testSchool2 = HighSchool("Thomasville High", 500, ["Tennis", "Basketball", "Baseball"])
print(testSchool2)
