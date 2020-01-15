# Part 1

## Compiler and Interpreter

If a translator translates a source code program into machine language, it is a
compiler. If a translator processes and executes the source program without
translating it into machine language first, it is an interpreter.

![compiler-interpreter](https://ruslanspivak.com/lsbasi-part1/lsbasi_part1_compiler_interpreter.png)

## Token

When you enter an expression 3+5 on the command line your interpreter gets a
string “3+5”. In order for the interpreter to actually understand what to do
with that string it first needs to break the input “3+5” into components called
tokens. A token is an object that has a type and a value. For example, for the
string “3” the type of the token will be INTEGER and the corresponding value
will be integer 3.

## Lexical Analyzer

The process of breaking the input string into tokens is called lexical analysis.
he part of the interpreter that does it is called a lexical analyzer, or lexer for
short. It is also known as scanner or tokenizer. They all mean the same: the part
of your interpreter or compiler that turns the input of characters into a stream of
tokens.

## References

https://ruslanspivak.com/lsbasi-part1/
