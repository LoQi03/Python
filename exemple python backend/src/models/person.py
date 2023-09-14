class Person:
  def __init__(self, name, age):
    self._id = None
    self.name = name
    self.age = age
    
  def to_dict(self):
      return {
          "name": self.name,
          "age": self.age
      }
      
  def from_dict(self, dict):
      self._id = dict["_id"]["$oid"]
      self.name = dict["name"]
      self.age = dict["age"]
      return self

