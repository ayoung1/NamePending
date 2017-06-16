class npo(object):
  def __init__(self, value=None):
    self.value = None

  def add(self, other):
    return self.value + other.value

  def subtract(self, other):
    return self.value - other.value

  def multiply(self, other):
    return self.value * other.value

  def divide(self, other):
    return self.value / other.value

  def bracket(self, *indexes):
    return [self.value[x] for x in indexes]

  def equals(self, other):
    return self.value == other.value

  def toString(self):
    return str(self.value)

  def clone(self):
    return Object(self.value)
