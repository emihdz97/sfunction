from rply import ParserGenerator
from ast import Variable, SetVariable, Bool, ToString, ToFloat, ToInt, Program, Lines, Equal, GreaterEqual, LessEqual, NotEqual, Greater, LessThan, String, Integer, Char, Float, Mul, Div, Sum, Sub, Display, Mod, Pow

class Parser():
	def __init__(self):
		self.pg = ParserGenerator(
			# List of accepted Tokens
			#['IF','DO','WHILE','FOR','SET','DISP','GET','TO-STRING','TO-FLOAT','TO-INT','TO-BOOL','SUM','SUB','MUL','DIV','POW','EQL','MOD','OPEN_BRACKET','CLOSED_BRACKET','OPEN_COMMENT','CLOSED_COMMENT','INT']
			['VAR_NAME','SET_INT','AND', 'TRUE', 'FALSE','TO-STRING','TO-FLOAT','TO-INT','TO-BOOL', 'IF','EQ', 'GE', 'LE','NE','GT','LT','CHAR','FLOAT','STRING','$end','OPEN_BRACKET', 'DISP', 'CLOSED_BRACKET', 'SUM', 'SUB','MUL','DIV','INT','POW','EQL','MOD'],
			precedence =[
				('left', ['SUM','SUB']),
				('left', ['DIV','MUL']),
				('left', ['MOD','POW']),
				('left', ['VAR_NAME']),
				('left', ['SET_INT'])
			]

		)

	def parse(self):
		@self.pg.production('program : lines')
		def program(p):
			return Program(p)

		@self.pg.production('lines : ')
		@self.pg.production('lines : utility lines')
		@self.pg.production('lines : line lines')
		def lines(p): #antes tebía line y no lines 
			return Lines(p)


		@self.pg.production('line : OPEN_BRACKET DISP expression CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET DISP bool CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET DISP comparison CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET DISP utility CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET SET_INT VAR_NAME INT CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET IF comparison OPEN_BRACKET lines CLOSED_BRACKET OPEN_BRACKET lines CLOSED_BRACKET CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET IF comparison OPEN_BRACKET lines CLOSED_BRACKET CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET IF bool OPEN_BRACKET lines CLOSED_BRACKET OPEN_BRACKET lines CLOSED_BRACKET CLOSED_BRACKET')
		@self.pg.production('line : OPEN_BRACKET IF bool OPEN_BRACKET lines CLOSED_BRACKET CLOSED_BRACKET')
		def line(p):
			function = p[1]
			if function.gettokentype() == 'DISP':
				return Display(p[2])
			elif function.gettokentype() == 'IF':
				if p[2].eval() == True or p[2].eval() == "#t":
					return p[4]
				elif p[2].eval() == False or p[2].eval() == "#f":
					if p[6].gettokentype() == 'CLOSED_BRACKET':
						return p[2] #Este return p[2] debería ser rturn none pero no funciona ¿lo podemos dejar así?
					elif p[6].gettokentype() == 'OPEN_BRACKET':
						return p[7]
			elif function.gettokentype() == 'SET_INT':
				#NAME TYPE VALUE
				return SetVariable(p[2].value,p[1].value,Integer(p[3].value))


		@self.pg.production('utility : OPEN_BRACKET TO-STRING expression CLOSED_BRACKET')
		@self.pg.production('utility : OPEN_BRACKET TO-FLOAT expression CLOSED_BRACKET')
		@self.pg.production('utility : OPEN_BRACKET TO-INT expression CLOSED_BRACKET')
#		@self.pg.production('utility : OPEN_BRACKET TO-BOOL expression CLOSED_BRACKET')
		def utility(p):
			function = p[1]
			if function.gettokentype() == 'TO-STRING':
				return ToString(p[2])
			elif function.gettokentype() == 'TO-FLOAT':
				return ToFloat(p[2])
			elif function.gettokentype() == 'TO-INT':
				return ToInt(p[2])
#			elif function.gettokentype() == 'TO-INT':
#				return ToInt(p[2])



		@self.pg.production('comparison : expression EQ expression')
		@self.pg.production('comparison : expression GE expression')
		@self.pg.production('comparison : expression LE expression')
		@self.pg.production('comparison : expression NE expression')
		@self.pg.production('comparison : expression GT expression')
		@self.pg.production('comparison : expression LT expression')
		@self.pg.production('comparison : bool EQ bool')
		@self.pg.production('comparison : bool GE bool')
		@self.pg.production('comparison : bool LE bool')
		@self.pg.production('comparison : bool NE bool')
		@self.pg.production('comparison : bool GT bool')
		@self.pg.production('comparison : bool LT bool')
		def comparison(p):
			left = p[0]
			right = p[2]
			comparator = p[1]
			if comparator.gettokentype() == 'EQ':
				return Equal(left, right)
			elif comparator.gettokentype() == 'GE':
				return GreaterEqual(left, right)
			elif comparator.gettokentype() == 'LE':
				return LessEqual(left, right)
			elif comparator.gettokentype() == 'NE':
				return NotEqual(left, right)
			elif comparator.gettokentype() == 'GT':
				return Greater(left, right)
			elif comparator.gettokentype() == 'LT':
				return LessThan(left, right)


		@self.pg.production('expression : expression SUM expression')
		@self.pg.production('expression : expression SUB expression')
		@self.pg.production('expression : expression MUL expression')
		@self.pg.production('expression : expression DIV expression')
		@self.pg.production('expression : expression POW expression')
		@self.pg.production('expression : expression MOD expression')
		def expression(p):
			left = p[0]
			right = p[2]
			operator = p[1]
			if operator.gettokentype() == 'SUM':
				return Sum(left,right)
			elif operator.gettokentype() == 'SUB':
				return Sub(left,right)
			elif operator.gettokentype() == 'MUL':
				return Mul(left,right)
			elif operator.gettokentype() == 'DIV':
				return Div(left,right)
			elif operator.gettokentype() == 'POW':
				return Pow(left,right)
			elif operator.gettokentype() == 'MOD':
				return Mod(left,right)


		@self.pg.production('expression : INT')
		def integer(p):
			return Integer(p[0].value)

		@self.pg.production('expression : FLOAT')
		def float(p):
			return Float(p[0].value)

		@self.pg.production('expression : STRING')
		def string(p):
			return String(p[0].value)

		@self.pg.production('expression : CHAR')
		def char(p):
			return Char(p[0].value)

		@self.pg.production('expression : VAR_NAME')
		def char(p):
			return Variable(p[0].value)

		@self.pg.production('bool : TRUE')
		@self.pg.production('bool : FALSE')
		def bool(p):
			#return print(p[0].value)
			return Bool(p[0].value)

		@self.pg.production('expression : expression $end')
		def end(p):
			print(p[3])

		@self.pg.error
		def error_handle(token):
			raise ValueError(token)

	def get_parser(self):
		return self.pg.build()
