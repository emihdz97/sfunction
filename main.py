from lexer import Lexer
from parser import Parser
import sys


f = open(sys.argv[1],"r")
text_input = f.read()
f.close()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

#for token in tokens:
#	print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
