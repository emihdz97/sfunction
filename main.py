from lexer import Lexer
from parser import Parser
import sys


#Open file with code
f = open(sys.argv[1],"r")
text_input = f.read()
f.close()

#Runs code through lexer
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

#Runs tokens from lexer into parser
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
