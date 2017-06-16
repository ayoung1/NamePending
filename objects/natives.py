class npo(object):
  def __init__(self, value=None):
    self.value = value 

  def call(self, env, evil, exp, *args):
    raise TypeError('Cannot call {}'.format(self.getType()))

  def add(self, other):
    return self.value + other.value

  def subtract(self, other):
    return self.value - other.value

  def multiply(self, other):
    return self.value * other.value

  def divide(self, other):
    return self.value / other.value

  def index(self, *indexes):
    if len(indexes) == 1:
      return self.value[indexes[0]]
    else:
      v = vect()
      for i in indexes:
        v.add(self.value[i])
      return v

  def equals(self, other):
    return self.value == other.value

  def toString(self):
    return str(self.value)

  def clone(self):
    return Object(self.value)

  def getType(self):
    return 'object'

class null(npo):
  def __init__(self):
    super(null, self).__init__()

  def add(self, other):
    raise TypeError('Cannot apply operation on a null reference')

  def subtract(self, other):
    raise TypeError('Cannot apply operation on a null reference')

  def multiply(self, other):
    raise TypeError('Cannot apply operation on a null reference')

  def divide(self, other):
    raise TypeError('Cannot apply operation on a null reference')

  def index(self, *indexes):
    raise TypeError('Cannot index a null reference')

  def equals(self, other):
    return self.value == other.value

  def toString(self):
    return 'null'

  def clone(self):
    raise TypeError('Cannot clone a null reference')

  def getType(self):
    return 'null'


class number(npo):
  def __init__(self, value):
    super(number, self).__init__(value=float(value))

  def getType(self):
    return 'number'


class string(npo):
  def __init__(self, value):
    super(string, self).__init__(value=str(value))

  def getType(self):
    return 'string'

class function(npo):
  def __init__(self, value):
    self.value = value

  def call(self, env, evil, exp, *args):
    func = evil(exp['func'], env)
    params = [evil(x, env) for x in exp['args']]
    return func(*params)

  def getType(self):
    return 'function'

class vect(npo):
  def __init__(self, *values):
    self.value = []
    self.size = 0
    for i in values:
      self.add(i)

  def add(self, other):
    self.value.append(other)
    return self

  def subtract(self, other):
    self.value.remove(other)
    return self

  def multiply(self, other):
    if other.getType() is not 'number':
      raise TypeError('Cannot multiply vectors by {}'.format(other.getType()))
    self.value = self.value * other.value
    return self

  def divide(self, other):
    raise TypeError('Cannot divide a vector')

  def toString(self):
    string = '['
    for i in self.value:
      string = string + i.toString() + ', '
    string = string[:len(string)-2] + ']'
    return string

  def clone(self):
    temp = vect()
    for i in self.value:
      temp.add(i.clone())
    return temp

  def getType(self):
    return 'vector'


class boolean(npo):
  def __init__(self, value):
    if type(value) is bool:
      super(boolean, self).__init__(value)

  def add(self, other):
    raise TypeError('Cannot add boolean values')

  def subtract(self, other):
    raise TypeError('Cannot subtract boolean values')

  def multiply(self, other):
    raise TypeError('Cannot multiply boolean values')

  def divide(self, other):
    raise TypeError('Cannot divide boolean values')

  def index(self, *indexes):
    raise TypeError('Cannot index boolean values')

  def getType(self):
    return 'bool'
