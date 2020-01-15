"""
Write an interpreter that handles arithmetic expressions like “7 - 3 + 2 - 1”
from scratch. Use any programming language you’re comfortable with and write it
off the top of your head without looking at the examples.

When you do that, think about components involved:
- a lexer that takes an input and converts it into a stream of tokens;
- a parser that feeds off the stream of the tokens provided by
the lexer and tries to recognize a structure in that stream and;
- an interpreter that generates results after the parser has successfully
parsed (recognized) a valid arithmetic expression.

String those pieces together. Spend some time translating the knowledge you’ve
acquired into a working interpreter for arithmetic expressions.
"""

from operator import add, sub, mul, truediv

INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
    def __init__ (self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, expression):
        self.expression = expression
        self.pos = -1
        self.current_token = None

    def lexer(self):
        self.pos += 1

        if self.pos >= len(self.expression):
            return EOF

        current_char = self.expression[self.pos]

        if current_char.isdigit():
            return Token(INTEGER, int(current_char))

        if current_char == '+':
            return Token(PLUS, '+')

        self.error()


    def eat(self, expected_token):
        if self.current_token.type == expected_token:
            self.current_token = self.lexer()
        else:
            self.error()

    def expr(self):
        self.current_token = self.lexer()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        return left.value + right.value


    def error(self):
        raise Exception('Error Parsing Input')


def main():
    while True:
        expression = input("calc>")
        interpreter = Interpreter(expression)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()
