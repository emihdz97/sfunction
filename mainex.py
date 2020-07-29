from lexer import Lexer
from parser import Parser

print(int("87"))

text_input = """
	[ABCDEvc 2 4 2 5442 e 3e12 )!#)!)##!"abd]
	(disp "hola "+"mundo")
	[(disp 9==9)
	(disp 8<3)
	(if 7==9
		(
			(disp "es igual")
		)
		(
			(disp "no es igual")
		)
	)
	(if 9==9
		(
			(disp "es true")
		)
		(
			(disp "es false")
		)
	)
	(if #f
		(
			(disp "es true")
		)
		(
			(disp "es false")
		)
	)
	(disp (intfy "743"))
	(disp (intfy 7-2))
	(disp (intfy 9.3*2))
	(disp (intfy '2'))
	(disp (floatify "743"))
	(disp (floatify 7-2))
	(disp (floatify 9.3*2))
	(disp (floatify '2'))
	(disp (stringify "743"))
	(disp (stringify 7-2))
	(disp (stringify 9.3*2))
	(disp (stringify '2'))
	(disp #f)
	(disp #t)]

	(disp 2+2)
	(disp 2.3+3.4)
	(disp 2+3.5)
	(disp "jaja "+"jajaja")
	(disp "\n")
	(disp 2-2)
	(disp 2.3-1.4)
	(disp 2-3.5)
	[(disp 2-"jaja")]
	(disp "\n")
	(disp 2*2)
	(disp 2.3*3.4)
	(disp 2*3.5)
	[(disp "jaja "* "ja")]
	(disp "jaja"*4)
	(disp "\n")
	(disp 99/3)
	(disp 23.07/2.09)
	(disp "samantha"/5*2)

	(disp "\n")
	(disp 2^3)
	(disp 2.5^2)

	(disp "\n")
	(disp 5%2)
	(disp 5%0.3)
	(disp 2.2%1.1)
	(disp 2.2%2)
	(disp "samantha"%7)

	(disp "\n")
	(disp 98<=9)
	(disp #t<=#t)
	(disp "samy"<="sam")
	(disp 9.2-2+2<=9.20-3+3)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

#for token in tokens:
#	print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
