# S-Function

S-Function is a functional programming language, based on the popular functional programming paradigm. S-Function focuses on operations over strings as well as common mathematical operations. This makes S-Function useful for text-based algorithms and database query construction. 

Specific project reach and documentation can be found inside SFunction_Documentation.pdf

Project based on "Writing your own programming language and compiler with Python" [(Andrade, 2018)](https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)

## Requirements

- [Anaconda](https://www.anaconda.com/products/individual)
- [LLC](https://llvm.org/docs/CommandGuide/llc.html) (LLVM static compiler)
- [GCC](https://gcc.gnu.org/) (Linking tool)
- LLVMlite
```bash
$ conda install --channel=numba llvmlite
```
- RPLY (same as PLY but with a better API)
```bash
$ conda install -c conda-forge rply
```

## Installation

After the above packages are installed, it is only necessary to download
- main.py
- ast.py
- parser.py

It is also recommended to use testcases.sam as reference. 

## Usage

```bash
$ python main.py s_function_code.sam
```
eg: 
```bash
$ python main.py testcases.sam
```
Reading the example usage of the operators and functions inside the testcases.sam should be the first approach to S-Function. 

## Test Cases

Provided example functions and test cases are located in testcases.sam


## Contributing
Pull requests are welcome. For major changes, please send us a mail first to discuss what you would like to change.

## Contact
If any questions about install or usage arise, feel free to send us an e-mail regarding your specific doubt.
- Samantha Barco: A01196844@itesm.mx
- Emilio Hernández: A01336418@itesm.mx

## License
[MIT](https://choosealicense.com/licenses/mit/)
