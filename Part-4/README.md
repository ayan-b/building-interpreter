# Part 4

## Context-free Grammers

It is another widely used notation for specifying the syntax of a programming
language and called context-free grammars (grammars, for short) or BNF (Backus-Naur
Form). For the purpose of this article we will not use pure [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
notation butmore like a modified [EBNF (Extended BNF)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)
notation.

Reasons of using grammer:

1. A grammar specifies the syntax of a programming language in a concise manner.
Unlike syntax diagrams, grammars are very compact.
2. Grammers can serve as great documentation.
3. A grammar is a good starting point even if one manually write your parser
from scratch. Quite often one can just convert the grammar to code by following
a set of simple rules.
4. There is a set of tools, called parser generators, which accept a grammar as
an input and automatically generate a parser for you based on that grammar.

## Mechanical Aspects of Grammer

Here's a grammer that describes arithmetic expressions like `7 * 4 / 2 * 3`:

```bash
expr: factor (( MUL | DIV) factor)*
factor: INTEGER
```

A grammar consists of a sequence of rules, also known as productions. Here there
are 2 rules:

![rules](https://ruslanspivak.com/lsbasi-part4/lsbasi_part4_bnf2.png)

A rule consists of a *non-terminal*, called the ***head*** or ***left-hand*** side of the
production, a colon, and a sequence of terminals and/or non-terminals, called
the ***body*** or ***right-hand side*** of the production:

![rules-head-body](https://ruslanspivak.com/lsbasi-part4/lsbasi_part4_bnf3.png)

In the grammar shown above, tokens like MUL, DIV, and INTEGER are called terminals
and variables like expr and factor are called non-terminals. Non-terminals usually
consist of a sequence of terminals and/or non-terminals:

![rules-terminals](https://ruslanspivak.com/lsbasi-part4/lsbasi_part4_bnf4.png)

The non-terminal symbol on the left side of the first rule is called the start
symbol. In the case of our grammar, the start symbol is *expr*:

![start-symbol](https://ruslanspivak.com/lsbasi-part4/lsbasi_part4_bnf5.png)

One can read the rule expr as “An expr can be a factor optionally followed by a
multiplication or division operator followed by another factor, which in turn is
optionally followed by a multiplication or division operator followed by another
factor and so on and so forth.”

What is a factor? For the purpose of this article a factor is just an integer.

Symbols used in the grammar and their meaning:

1. | - Alternatives. A bar means “or”. So (MUL | DIV) means either MUL or DIV.
2. ( … ) - An open and closing parentheses mean grouping of terminals and/or
   non-terminals as in (MUL | DIV).
3. ( … )* - Match contents within the group zero or more times.

The symbols |, (), and (…)* are similar to the ones used in Regular Expression.

A grammar defines a language by explaining what sentences it can form. This is
how one can derive an arithmetic expression using the grammar: first one begins
with the start symbol expr and then repeatedly replace a non-terminal by the
body of a rule for that non-terminal until a sentence has been generated consisting
solely of terminals. Those sentences form a language defined by the grammar.

If the grammar cannot derive a certain arithmetic expression, then it doesn’t
support that expression and the parser will generate a syntax error when it tries
to recognize the expression.

## Examples

Expression `3`:

```bash
expr
factor ((MUL | DIV) factor)*
factor
INTEGER
3
```

Expression `3 * 7`:

```bash
expr
factor ((MUL | DIV) factor)*
factor MUL factor
INTEGER MUL factor
3 * 7
```

Expression `3 * 7 / 2`:

```bash
expr
factor ((MUL | DIV) factor)*
factor MUL factor ((MUL | DIV) factor)*
factor MUL factor DIV factor
INTEGER MUL INTEGER DIV INTEGER
3 * 7 / 2
```

Translating grammer to a parser:

1. Each rule, **R**, defined in the grammar, becomes a method with the same
   name, and references to that rule become a method call: `R()`. The body of
   the method follows the flow of the body of the rule using the very same
   guidelines.
2. Alternatives `(a1 | a2 | aN)` become an `if-elif-else` statement.
3. An optional grouping `(…)*` becomes a `while` statement that can loop over zero
   or more times.
4. Each token reference `T` becomes a call to the method eat: `eat(T)`. The way
   the eat method works is that it consumes the token `T` if it matches the current
   lookahead token, then it gets a new token from the lexer and assigns that token
   to the current_token internal variable.

Visually:

![grammer-to-parser](https://ruslanspivak.com/lsbasi-part4/lsbasi_part4_rules.png)

## References

<https://ruslanspivak.com/lsbasi-part4/>
