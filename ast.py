# Dudas:
# Esta bien tener init y eval de todos nuestros tipos de dato?
# Básicamente estamos usando funciones de python

#En la documentación de rply indica que las variables tienen que ser en diccionario https://rpython.readthedocs.io/en/latest/rpython.html#object-restrictions
variables = {}

#Variables
class SetVariable():
	def __init__(self, name, type, value):
		self.name = name
		self.type = type
		self.value = value

	def eval(self):
		print("trying to store variable name ",self.name," type ",self.type," value ",self.value.eval())
		if self.name in variables:
			return
		else:
			variables[self.name] = {"type": type(self.value.eval()), "value":self.value.eval()}
			for x, y in variables.items():
				print(x,y)

class Variable():
	def __init__(self, name):
		self.name = name

	def eval(self):
		print("trying to get variable name ",self.name)
		if self.name in variables:
			return variables.get(self.name).get("value")
		else:
			return


#Last Added
class Program():
	def __init__(self,lines):
		self.lines = lines

	def eval(self):
		for line in self.lines:
			line.eval()
		return

class Lines():
	def __init__(self, statements):
		self.statements = statements

	def eval(self):
		for statement in self.statements:
			statement.eval()
		return

# Data Types
class Bool():
	def __init__(self,value):
		self.value = value

	def eval(self):
		return str(self.value)

class Integer():
	def __init__(self,value):
		self.value = value

	def eval(self):
		return int(self.value)

class Float():
	def __init__(self,value):
		self.value = value

	def eval(self):
		return float(self.value)

class String():
	def __init__(self,value):
		self.value = value

	def eval(self):
		return str(self.value[1:(len(self.value)-1)])

class Char():
	def __init__(self,value):
		self.value = value

	def eval(self):
		return str(self.value[1])

# Data comparators
class Comparator():
	def __init__(self, left, right):
		self.left = left
		self.right = right

class Equal(Comparator):
	def eval(self):
		if self.left.eval() == self.right.eval():
			return "#t"
		else:
			return "#f"

class GreaterEqual(Comparator):
	def eval(self):
		if self.left.eval() >= self.right.eval():
			return "#t"
		else:
			return "#f"

class LessEqual(Comparator):
	def eval(self):
		if self.left.eval() <= self.right.eval():
			return "#t"
		else:
			return "#f"

class NotEqual(Comparator):
	def eval(self):
		if self.left.eval() != self.right.eval():
			return "#t"
		else:
			return "#f"

class Greater(Comparator):
	def eval(self):
		if self.left.eval() > self.right.eval():
			return "#t"
		else:
			return "#f"

class LessThan(Comparator):
	def eval(self):
		if self.left.eval() < self.right.eval():
			return "#t"
		else:
			return "#f"


# Data operations
class BinaryOp():
	def __init__(self, left, right):
		self.left = left
		self.right = right

class Sum(BinaryOp):
	def eval(self):
		return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
	def eval(self):
		return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
	def eval(self):
		return self.left.eval() * self.right.eval()

# Es correcto tener funciones de apoyo??
def Divstring(value, position):
	if int(position.eval()) <= len(value.eval()):
		return str(value.eval()[0:int(position.eval())])
	else:
		return

class Div(BinaryOp):
	def eval(self):
		if type(self.left.eval()) is str and type(self.right.eval()) is int:
			return Divstring(self.left,self.right)
		else:
			return self.left.eval() / self.right.eval()

class Pow(BinaryOp):
	def eval(self):
		return self.left.eval() ** self.right.eval()

# Es correcto tener funciones de apoyo??
def Modstring(value, position):
	if int(position.eval()) < len(value.eval()):
		return str(value.eval()[int(position.eval()):int(position.eval())+1])
	else:
		return

class Mod(BinaryOp):
	def eval(self):
		if type(self.left.eval()) is str and type(self.right.eval()) is int:
			return Modstring(self.left,self.right)
		else:
			return self.left.eval() % self.right.eval()


class Display():
	def __init__(self,value):
		self.value = value

	def eval(self):
		print(self.value.eval())

#Funciones de python

class ToString():
	def __init__(self,value):
		self.value = value

	def eval(self):
		value = self.value.eval()
		return str(value)

class ToFloat():
	def __init__(self,value):
		self.value = value

	def eval(self):
		value = self.value.eval()
		return float(value)


class ToInt():
	def __init__(self,value):
		self.value = value

	def eval(self):
		value = self.value.eval()
		return int(value)



