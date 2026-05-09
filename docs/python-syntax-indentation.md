# Python Syntax & Indentation

**Source:** [python.datalumina.com/basics/python-syntax](https://python.datalumina.com/basics/python-syntax)

## What is syntax?

Syntax is the set of rules governing how code must be written — the grammar of a programming language. Python is known for being clean and readable, but it is strict about structure.

## Indentation: Python's defining feature

Most languages (including JavaScript) use curly braces `{}` to define code blocks. Python uses **indentation** instead. This is not a style preference — it is enforced by the interpreter.

**JavaScript:**
```javascript
if (temperature > 30) {
    console.log("It's hot!");
    console.log("Turn on AC");
}
```

**Python equivalent:**
```python
if temperature > 30:
    print("It's hot!")
    print("Turn on AC")
```

The colon `:` opens a block; everything indented beneath it belongs to that block. When indentation returns to the previous level, the block ends.

## Rules to follow

- **Always use 4 spaces** — not tabs, not 2 spaces. 4 spaces is the Python community standard.
- **Be consistent** — never mix indentation amounts within the same block or nested structure.
- **Wrong indentation = broken code** — Python will refuse to run it, raising an `IndentationError`. This is the #1 beginner mistake.

## PEP 8 — the style guide

PEP 8 (Python Enhancement Proposal 8) is the official style guide for Python code. It covers indentation and much more:

| Rule | Standard |
|---|---|
| Indentation | 4 spaces |
| Max line length | 79 characters |
| Variable naming | `snake_case` (`user_name`, not `userName`) |
| Spacing around operators | `x = 1 + 2`, not `x=1+2` |

PEP 8 compliance is not required for code to run, but it is expected in professional Python. Tools like Ruff (covered later in the course) enforce it automatically.
