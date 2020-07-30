from itertools import chain
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
#		print("trying to store variable name ",self.name," type ",self.type," value ",self.value.eval())
		if self.name in variables:
			return
		else:
			variables[self.name] = {"type": type(self.value.eval()), "value":self.value.eval()}
			for x, y in variables.items():
				print(x,y)

class ChangeVariable():
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def eval(self):
		#print("aqui 3")
		#print("trying to store variable name ", self.name," value ", self.value.eval())
		#if self.name in variables:
			#print("old",variables[self.name]["type"],"new",type(self.value.eval()))
		#	if variables[self.name]["type"]==type(self.value.eval()):
				#print("se puede")
		#		variables[self.name]["value"] = self.value.eval()
				#for x, y in variables.items():
				#	print(x,y)
		#		return
		#	else:
		#		print("Tipo no compatible")
		if self.name in variables:
			#print("old ",variables[self.name]["value"]," new ", self.value.eval())
			if variables[self.name]["type"]==type(self.value.eval()) and type(self.value.eval()) is str:
				if (variables[self.name]["value"]=="#t" or variables[self.name]["value"]=="#f") and (self.value.eval()=="#t" or self.value.eval()=="#f"):
					variables[self.name]["value"] = self.value.eval()
#					print("era bool")
				elif len(variables[self.name]["value"])==1 and len(self.value.eval())==1:
					variables[self.name]["value"] = self.value.eval()
#					print("era char")
				elif variables[self.name]["value"][0]!='#' and self.value.eval()[0]!='#' and len(variables[self.name]["value"])>1:
					variables[self.name]["value"] = self.value.eval()
#					print("era string ", len(variables[self.name]["value"]))
			elif variables[self.name]["type"]==type(self.value.eval()):
				variables[self.name]["value"] = self.value.eval()
#				print("era int float")
			else:
				return
#				print("Tipo no compatible")
		else:
			print("No existe la variable")
#		for x, y in variables.items():
#			print(x,y)


class Variable():
	def __init__(self, name):
		self.name = name

	def eval(self):
#		print("trying to get variable name ",self.name)
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


# Arrays
class Array():
	def __init__(self, elements, type):
		self.elements = elements
		self.type = type

	def eval(self):
		print(self.elements)
		output = []

		def reemoveNestings(l):
			# function used for removing nested
			# lists in python.
			for i in l:
				print(type(i.value()))
				if type(i) == list:
					reemovNestings(i)
				else:
					output.append(i)


		# Driver code
		print ('The original list: ', self.elements)
		reemoveNestings(self.elements)
		print ('The list after removing nesting: ', output)
		return output

class SetArray():
	def __init__(self,string,type, name):
		self.string = string
		self.type = type
		self.name = name

	def eval(self):
		reslist = list(self.string.value[1:len(self.string.value)-1].split(",")) 
		finlist = []
		# Checks for all elements to be the same type
		if type(self.type) is int:
			for element in reslist:
				finlist.append(int(element))
		elif type(self.type) is float:
			for element in reslist:
				finlist.append(float(element))
		elif type(self.type) is str:
			for element in reslist:
				finlist.append(str(element)[1:len(element)-1])
		print(finlist)
		print(type(self.type))
		# If variable name doesn-t exists adds array
		if self.name in variables:
			return
		else:
			variables[self.name] = {"type": type(finlist), "value":finlist}
			print("array added")
			print(variables[self.name])
			print(type(finlist))
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

# Loops functions
class LoopData():
	def __init__(self, left, right, comparator, lines):
		self.left = left
		self.right = right
		self.lines = lines

class LoopComparator():
	def __init__(self, left, comparator, right):
		self.left = left
		self.right = right
		self.comparator = comparator

	def eval(self):
#		print([self.left, self.comparator, self.right])
		return [self.left, self.comparator, self.right]

class WhileLoop():
	def __init__(self, comparison, lines):
		self. comparison = comparison
		self.lines = lines

	def eval(self):
		# Comparison tiene un arreglo con los valores del comparator (izq, comp, der )
		comparator = self.comparison.eval()[1].value
		#left = self.comparison.eval()[0].eval()
		#right = self.comparison.eval()[2].eval()
		left = self.comparison.eval()[0]
		right = self.comparison.eval()[2]
		lines = self.lines
#		print(left, comparator, right)

		if comparator == '==':
#			print("is equal")
			comparison = Equal(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>=':
#			print("is >=")
			comparison = GreaterEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<=':
#			print("is <=")
			comparison = LessEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '!=':
#			print("is !=")
			comparison = NotEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>':
#			print("is >")
			comparison = Greater(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<':
#			print("is <")
			comparison = LessThan(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			while comparison.eval()=='#t':
				lines.eval()
		return self.comparison.eval()[0]


class DoWhileLoop():
	def __init__(self, comparison, lines):
		self. comparison = comparison
		self.lines = lines

	def eval(self):
		# Comparison tiene un arreglo con los valores del comparator (izq, comp, der )
		comparator = self.comparison.eval()[1].value
		#left = self.comparison.eval()[0].eval()
		#right = self.comparison.eval()[2].eval()
		left = self.comparison.eval()[0]
		right = self.comparison.eval()[2]
		lines = self.lines
#		print(left, comparator, right)

		if comparator == '==':
#			print("is equal")
			comparison = Equal(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>=':
#			print("is >=")
			comparison = GreaterEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<=':
#			print("is <=")
			comparison = LessEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '!=':
#			print("is !=")
			comparison = NotEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>':
#			print("is >")
			comparison = Greater(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<':
#			print("is <")
			comparison = LessThan(self.comparison.eval()[0], self.comparison.eval()[2])
			#print("evaluation is ", equal.eval())
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		return self.comparison.eval()[0]


class ForLoop():
	def __init__(self, iteratorName, arrayName, lines):
		self.iteratorName = iteratorName
		self.arrayName = arrayName
		self.lines = lines

	def eval(self):
		lines = self.lines
#		print("iterator ",self.iteratorName.value, " array ",self.arrayName.value)
#		lines.eval()
#		for key,variable in variables.items():
#			print(key,variable)
		if self.arrayName.value in variables:
			if variables[self.arrayName.value]["type"] is list:
#				print("es iterable")
				name = self.iteratorName.value
				value = variables[self.arrayName.value]["value"][0]
				variables[name] = {"type": type(value), "value":value}
#		for x, y in variables.items():
#			print(x,y)

				for a in variables[self.arrayName.value]["value"]:
					variables[name] = {"type": a, "value":a}
#					print(variables[name])
					lines.eval()

				del variables[name]
#		for x, y in variables.items():
#			print(x,y)


		return
