#DUDAS: Es mejor dejarlos ordenados para setear prioridad o también prioridad en parser?

from rply import LexerGenerator

class Lexer():
	def __init__(self):
		self.lexer = LexerGenerator()

	def _add_tokens(self):
		# Funciones definidas
		self.lexer.add('IF', r'if')
		self.lexer.add('DO', r'do')
		self.lexer.add('WHILE', r'while')
		self.lexer.add('FOR', r'for')
		self.lexer.add('SET', r'set')

		# Utilidades
		self.lexer.add('DISP', r'disp')
		self.lexer.add('GET', r'get')
		self.lexer.add('TO-STRING', r'stringify')
		self.lexer.add('TO-FLOAT', r'floatify')
		self.lexer.add('TO-INT', r'intfy')
		self.lexer.add('TO-BOOL', r'boolfy')

		# Almacenamiento de variables
		self.lexer.add('SET_INT', r'integer')
		self.lexer.add('SET_CHAR', r'char')
		self.lexer.add('SET_FLOAT', r'float')
		self.lexer.add('SET_ARRAY', r'array')
		self.lexer.add('SET_STRING', r'string')
		self.lexer.add('SET_BOOL', r'bool')

		# Operadores 
		self.lexer.add('EQ', r'==')
		self.lexer.add('GE', r'>=')
		self.lexer.add('LE', r'<=')
		self.lexer.add('NE', r'!=')
		self.lexer.add('SUM', r'\+')
		self.lexer.add('SUB', r'\-')
		self.lexer.add('MUL', r'\*')
		self.lexer.add('DIV', r'\/')
		self.lexer.add('POW', r'\^')
		self.lexer.add('EQL', r'\=')
		self.lexer.add('MOD', r'\%')
		self.lexer.add('GT', r'>')
		self.lexer.add('LT', r'<')
		self.lexer.add('AND',r'&&')
		self.lexer.add('OR', r'\|\|')
		self.lexer.add('NOT', r'!')

		# Parentesis y corchetes
		self.lexer.add('OPEN_BRACKET', r'\(')
		self.lexer.add('CLOSED_BRACKET', r'\)')

		# Tipo de datos
		self.lexer.add('FLOAT', r'-?\d+\.\d+')
		self.lexer.add('INT', r'-?\d+')
		self.lexer.add('STRING', r'\"[^"]*\"')
		self.lexer.add('TRUE', r'#t')
		self.lexer.add('FALSE', r'#f')
		self.lexer.add('VAR_NAME', r'[a-zA-Z0-9_-]+')
		self.lexer.add('CHAR', r'\'[^ ]{1}\'')

		# Ignorar espacios
		self.lexer.ignore('\s+')
		self.lexer.ignore('\[[^\[\]]*\]')

	def get_lexer(self):
		self._add_tokens()
		return self.lexer.build()
