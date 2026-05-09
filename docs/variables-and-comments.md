# Variables & Comments

**Relevant script:** [`scripts/basics/variables.py`](../scripts/basics/variables.py)  
**Sources:** [python.datalumina.com/basics/variables](https://python.datalumina.com/basics/variables) · [python.datalumina.com/basics/comments](https://python.datalumina.com/basics/comments)

---

## Variables

A variable is a named container for storing a value. You create one with the assignment operator `=`:

```python
name = "Alice"
age = 25
is_student = True
```

Variables are mutable — you can reassign them at any time:

```python
score = 0
score = 10
score = score + 5   # score is now 15
```

### Naming rules

| Pattern | Valid? | Note |
|---|---|---|
| `user_name` | Yes | Python standard (`snake_case`) |
| `userName` | Yes | Works, but non-idiomatic — that's JS convention |
| `age2` | Yes | Numbers allowed, just not at the start |
| `_private` | Yes | Leading underscore is permitted |
| `2age` | No | Cannot start with a number |
| `my-name` | No | Hyphens not allowed |
| `my name` | No | Spaces not allowed |
| `class` | No | Reserved keyword |

### Common mistakes

- Forgetting quotes around strings: `name = Alice` → `NameError`
- Using a variable before assigning it → `NameError`
- Confusing `=` (assignment) with `==` (comparison)

---

## Comments

Comments are notes for humans — Python ignores them entirely.

### Single-line

Use `#`. Can sit on its own line or trail after code:

```python
# Store user's age
age = 25

score = score + 5  # Accumulate points
```

### Multi-line

Python has no true multi-line comment syntax. The convention is triple-quoted strings that are never assigned — Python parses them as a string but discards them:

```python
"""
This spans multiple lines.
Useful for longer explanations.
"""
```

### Docstrings

A triple-quoted string placed immediately after a function definition becomes its docstring — built-in documentation accessible via `help()`:

```python
def calculate_tip(bill):
    """Calculate 20% tip. Takes bill amount, returns tip value."""
    return bill * 0.20
```

### When to comment (and when not to)

Good comments explain **why**, not **what**. The code already shows what:

```python
# ✓ Explains a non-obvious value
tax_rate = 1.0625  # CA sales tax is 6.25%

# ✗ Just restates the code
score = score + 5  # Add 5 to score
```

Prefer clear naming over comments wherever possible — `days_in_week = 7` needs no comment; `d = 7` does.
