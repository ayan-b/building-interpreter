# Part 2

## Lexeme

A lexeme is a sequence of characters that form a token.

![lexeme](https://ruslanspivak.com/lsbasi-part2/lsbasi_part2_lexemes.png)

## Parser

The process of finding the structure in the stream of tokens, or put differently,
the process of recognizing a phrase in the stream of tokens is called parsing.
The part of an interpreter or compiler that performs that job is called a parser.

The `expr` method is the part of the interpreter where both parsing and interpreting
happens - the expr method first tries to recognize (parse) the INTEGER -> PLUS -> INTEGER
or the INTEGER -> MINUS -> INTEGER phrase in the stream of tokens and after it
has successfully recognized (parsed) one of those phrases, the method interprets
it and returns the result of either addition or subtraction of two integers to
the caller.

## References

https://ruslanspivak.com/lsbasi-part2/ 
