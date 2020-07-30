from itertools import chain

#En la documentación de rply indica que las variables tienen que ser en diccionario https://rpython.readthedocs.io/en/latest/rpython.html#object-restrictions
variables = {}


# Input
class IntInput():
	def __init__(self, name):
		self.name = name

	def eval(self):
		try:
			x = int(input())
		except ValueError:
			print("Input integer: el valor ingresado no es un entero")
			exit()
		if self.name in variables:
			print("Input integer: la variable ", self.name," ya existe")
			exit()
		else:
			variables[self.name] = {"type": type(x), "value":x}
		return x

class FloatInput():
	def __init__(self, name):
		self.name = name

	def eval(self):
		try:
			x = float(input())
		except ValueError:
			print("Float integer: el valor ingresado no es un float")
			exit()
		if self.name in variables:
			print("Float integer: la variable ", self.name," ya existe")
			exit()
		else:
			variables[self.name] = {"type": type(x), "value":x}
		return x


class StringInput():
	def __init__(self, name):
		self.name = name

	def eval(self):
		try:
			x = input()
		except ValueError:
			print("String integer: el valor ingresado no es valido")
			exit()
		if self.name in variables:
			print("String integer: la variable ", self.name," ya existe")
			exit()
		else:
			variables[self.name] = {"type": type(x), "value":x}
		return x


class CharInput():
	def __init__(self, name):
		self.name = name

	def eval(self):
		try:
			x = input()
		except ValueError:
			print("Char integer: el valor ingresado no es valido")
			exit()
		if self.name in variables:
			print("Char integer: la variable ", self.name," ya existe")
			exit()
		else:
			variables[self.name] = {"type": type(x[0]), "value":x[0]}

		return x



#Variables
class SetVariable():
	def __init__(self, name, type, value):
		self.name = name
		self.type = type
		self.value = value

	def eval(self):
		if self.name in variables:
			print("SetVariable: la variable ", self.name," ya existe")
			exit()
		else:
			variables[self.name] = {"type": type(self.value.eval()), "value":self.value.eval()}

class ChangeVariable():
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def eval(self):
		if self.name in variables:
			if variables[self.name]["type"]==type(self.value.eval()) and type(self.value.eval()) is str:
				if (variables[self.name]["value"]=="#t" or variables[self.name]["value"]=="#f") and (self.value.eval()=="#t" or self.value.eval()=="#f"):
					variables[self.name]["value"] = self.value.eval()
				elif len(variables[self.name]["value"])==1 and len(self.value.eval())==1:
					variables[self.name]["value"] = self.value.eval()
				elif variables[self.name]["value"][0]!='#' and self.value.eval()[0]!='#' and len(variables[self.name]["value"])>1:
					variables[self.name]["value"] = self.value.eval()
			elif variables[self.name]["type"]==type(self.value.eval()):
				variables[self.name]["value"] = self.value.eval()
			else:
				print("ChangeVariable: la variable ", self.name," no es valida con el tipo ",type(self.value.eval()))
				exit()
		else:
			print("Variable: la variable ", self.name," no existe")
			exit()


class Variable():
	def __init__(self, name):
		self.name = name

	def eval(self):
		if self.name in variables:
			return variables.get(self.name).get("value")
		else:
			print("Variable: la variable ", self.name," no existe")
			exit()

class ArrayPosition():
	def __init__(self, position, name):
		self.name = name
		self.position = position

	def eval(self):
		if self.name in variables:
			array = variables.get(self.name).get("value")
			position = self.position.eval()
			if type(array) is list:
				if position < len(array):
					return array[position]
				else:
					print("ArrayPosition: la posición ", position," supera la longitud de la lista")
					exit()
			else:
				print("ArrayPosition: la variable ", self.name," no es una lista")
				exit()
		else:
			print("ArrayPosition: la variable ", self.name," no ha sido declarada")
			exit()


class SetArrayPosition():
	def __init__(self, position, name, value):
		self.name = name
		self.position = position
		self.value = value

	def eval(self):
		if self.name in variables:
			array = variables.get(self.name).get("value")
			position = self.position.eval()
			if type(array) is list:
				if position < len(array):
					#print(variables.get(self.name))
					#print(array[position], self.value.eval())
					if type(array[position]) == type(self.value.eval()):
						variables.get(self.name).get("value")[position] = self.value.eval()
						return
					else:
						print("SetArrayPosition: el dato ", type(self.value.eval())," no es compatible con la lista")
						exit()
				else:
					print("SetArrayPosition: la posición ", position," supera la longitud de la lista")
					exit()
			else:
				print("SetArrayPosition: la variable ", self.name," no es una lista")
				exit()
		else:
			print("SetArrayPosition: la variable ", self.name," no ha sido declarada")
			exit()



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
		# If variable name doesn-t exists adds array
		if self.name in variables:
			print("SetArray: la variable ", self.name," ya existe")
			exit()
		else:
			variables[self.name] = {"type": type(finlist), "value":finlist}
			return

# Data Types
class Bool():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			return str(self.value)
		except ValueError:
			print("Bool: el valor ingresado no es un bool valido")
			exit()


class Integer():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			return int(self.value)
		except ValueError:
			print("Int: el valor ingresado no es un integer valido")
			exit()

class Float():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			return float(self.value)
		except ValueError:
			print("Float: el valor ingresado no es un float valido")
			exit()

class String():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			return str(self.value[1:(len(self.value)-1)])
		except ValueError:
			print("String: el valor ingresado no es un string valido")
			exit()
class Char():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			return str(self.value[1])
		except ValueError:
			print("Char: el valor ingresado no es un char valido")
			exit()


# Data comparators

class Comparator():
	def __init__(self, left, right):
		self.left = left
		self.right = right


class Equal(Comparator):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			if self.left.eval() == self.right.eval():
				return "#t"
			else:
				return "#f"
		else:
			print("==: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()



class GreaterEqual(Comparator):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			if self.left.eval() >= self.right.eval():
				return "#t"
			else:
				return "#f"
		else:
			print(">=: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()

class LessEqual(Comparator):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			if self.left.eval() <= self.right.eval():
				return "#t"
			else:
				return "#f"
		else:
			print("<=: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()

class NotEqual(Comparator):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			if self.left.eval() != self.right.eval():
				return "#t"
			else:
				return "#f"
		else:
			print("!=: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()

class Greater(Comparator):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			if self.left.eval() > self.right.eval():
				return "#t"
			else:
				return "#f"
		else:
			print(">: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()


class LessThan(Comparator):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			if self.left.eval() < self.right.eval():
				return "#t"
			else:
				return "#f"
		else:
			print("<: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()


# Data operations
class BinaryOp():
	def __init__(self, left, right):
		self.left = left
		self.right = right

class Sum(BinaryOp):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			return  left + right
		elif type(left) is float and type(right) is int:
			return  left + right
		elif type(left) is int and type(right) is float:
			return  left + right
		else:
			print("Suma: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()

class Sub(BinaryOp):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) is str or type(right) is str:
			print("Resta: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()
		else:
			return  left - right


class Mul(BinaryOp):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) == type(right):
			return  left * right
		elif type(left) is float and type(right) is int:
			return  left * right
		elif type(left) is int and type(right) is float:
			return  left * right
		elif type(left) is str and type(right) is int:
			return  left * right
		elif type(left) is int and type(right) is str:
			return  left * right
		else:
			print("Multiplicacion: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()


def Divstring(value, position):
	if int(position.eval()) <= len(value.eval()):
		return str(value.eval()[0:int(position.eval())])
	else:
		return

class Div(BinaryOp):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) is str and type(right) is int:
			return Divstring(self.left,self.right)
		elif type(left) is int and type(right) is int:
			return self.left.eval() / self.right.eval()
		elif type(left) is float and type(right) is float:
			return self.left.eval() / self.right.eval()
		else:
			print("Division: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()

class Pow(BinaryOp):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) is str:
			print("Potencia: Tipo", type(left)," no compatible")
			exit()
		elif type(right) is str:
			print("Potencia: Tipo", type(right)," no compatible")
			exit()
		elif type(left) == type(right):
			return  left ** right
		elif type(left) is float and type(right) is int:
			return  left ** right
		elif type(left) is int and type(right) is float:
			return  left ** right
		else:
			print("Potencia: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()


def Modstring(value, position):
	if int(position.eval()) < len(value.eval()):
		return str(value.eval()[int(position.eval()):int(position.eval())+1])
	else:
		return

class Mod(BinaryOp):
	def eval(self):
		left = self.left.eval()
		right = self.right.eval()
		if type(left) is str and type(right) is int:
			return Modstring(self.left,self.right)
		elif type(right) is str or type(left) is str:
			print("Modulo: Tipo", type(left)," no compatible")
			exit()
		elif type(left) == type(right):
			return  left % right
		elif type(left) is float and type(right) is int:
			return  left % right
		elif type(left) is int and type(right) is float:
			return  left % right
		else:
			print("Modulo: Tipos", type(left)," y ",type(right)," no compatibles")
			exit()


class Display():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			print(self.value.eval())
		except ValueError:
			print("Display: El tipo de dato", type(self.value.eval())," no puede ser impreso")
			exit()

#Funciones de python

class ToString():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			if type(self.value.eval()) is str:
				print("ToString: El tipo de dato", type(self.value.eval())," no puede ser convertido a string")
				exit()
			value = str(self.value.eval())
			return value
		except ValueError:
			print("ToString: El tipo de dato", type(self.value.eval())," no puede ser convertido a string")
			exit()

class ToFloat():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			value = float(self.value.eval())
			return value
		except ValueError:
			print("ToFloat: El tipo de dato", type(self.value.eval())," no puede ser convertido a float")
			exit()

class ToInt():
	def __init__(self,value):
		self.value = value

	def eval(self):
		try:
			value = int(self.value.eval())
			return value
		except ValueError:
			print("ToFloat: El tipo de dato", type(self.value.eval())," no puede ser convertido a float")
			exit()

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
		return [self.left, self.comparator, self.right]

class WhileLoop():
	def __init__(self, comparison, lines):
		self. comparison = comparison
		self.lines = lines

	def eval(self):
		comparator = self.comparison.eval()[1].value
		left = self.comparison.eval()[0]
		right = self.comparison.eval()[2]
		lines = self.lines
		if comparator == '==':
			comparison = Equal(self.comparison.eval()[0], self.comparison.eval()[2])
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>=':
			comparison = GreaterEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<=':
			comparison = LessEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '!=':
			comparison = NotEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>':
			comparison = Greater(self.comparison.eval()[0], self.comparison.eval()[2])
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<':
			comparison = LessThan(self.comparison.eval()[0], self.comparison.eval()[2])
			while comparison.eval()=='#t':
				lines.eval()
		return self.comparison.eval()[0]


class DoWhileLoop():
	def __init__(self, comparison, lines):
		self. comparison = comparison
		self.lines = lines

	def eval(self):
		comparator = self.comparison.eval()[1].value
		left = self.comparison.eval()[0]
		right = self.comparison.eval()[2]
		lines = self.lines

		if comparator == '==':
			comparison = Equal(self.comparison.eval()[0], self.comparison.eval()[2])
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>=':
			comparison = GreaterEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<=':
			comparison = LessEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '!=':
			comparison = NotEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>':
			comparison = Greater(self.comparison.eval()[0], self.comparison.eval()[2])
			lines.eval()
			while comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<':
			comparison = LessThan(self.comparison.eval()[0], self.comparison.eval()[2])
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
		if self.arrayName.value in variables:
			if variables[self.arrayName.value]["type"] is list:
				name = self.iteratorName.value
				value = variables[self.arrayName.value]["value"][0]
				variables[name] = {"type": type(value), "value":value}

				for a in variables[self.arrayName.value]["value"]:
					variables[name] = {"type": a, "value":a}
					lines.eval()

				del variables[name]

		return

# If
class If():
	def __init__(self, comparison, lines):
		self.comparison = comparison
		self.lines = lines

	def eval(self):
		comparator = self.comparison.eval()[1].value
		left = self.comparison.eval()[0]
		right = self.comparison.eval()[2]
		lines = self.lines

		if comparator == '==':
			comparison = Equal(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>=':
			comparison = GreaterEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<=':
			comparison = LessEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				lines.eval()
		elif comparator == '!=':
			comparison = NotEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				lines.eval()
		elif comparator == '>':
			comparison = Greater(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				lines.eval()
		elif comparator == '<':
			comparison = LessThan(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				lines.eval()
		return self.comparison.eval()[0]


# IfElse
class IfElse():
	def __init__(self, comparison, linesTrue, linesFalse):
		self.comparison = comparison
		self.linesTrue = linesTrue
		self.linesFalse = linesFalse

	def eval(self):
		comparator = self.comparison.eval()[1].value
		left = self.comparison.eval()[0]
		right = self.comparison.eval()[2]
		linesTrue = self.linesTrue
		linesFalse = self.linesFalse

		if comparator == '==':
			comparison = Equal(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				linesTrue.eval()
			else:
				linesFalse.eval()
		elif comparator == '>=':
			comparison = GreaterEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				linesTrue.eval()
			else:
				linesFalse.eval()
		elif comparator == '<=':
			comparison = LessEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				linesTrue.eval()
			else:
				linesFalse.eval()
		elif comparator == '!=':
			comparison = NotEqual(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				linesTrue.eval()
			else:
				linesFalse.eval()
		elif comparator == '>':
			comparison = Greater(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				linesTrue.eval()
			else:
				linesFalse.eval()
		elif comparator == '<':
			comparison = LessThan(self.comparison.eval()[0], self.comparison.eval()[2])
			if comparison.eval()=='#t':
				linesTrue.eval()
			else:
				linesFalse.eval()
		return self.comparison.eval()[0]
