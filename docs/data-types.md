# Data Types in Python

**Relevant script:** [`scripts/basics/datatypes.py`](../scripts/basics/datatypes.py) *(currently covers strings; numbers and booleans to be added)*  
**Sources:** [overview](https://python.datalumina.com/data-types) · [numbers](https://python.datalumina.com/data-types/numbers) · [strings](https://python.datalumina.com/data-types/strings) · [booleans](https://python.datalumina.com/data-types/booleans)

---

## Why data types exist

Python organises values into distinct categories because different types follow different rules. You can add two numbers together, and you can concatenate two strings — but you cannot add a number directly to a string without converting one of them first.

Use `type()` to inspect any value at runtime:

```python
type(42)       # <class 'int'>
type(3.14)     # <class 'float'>
type("Hello")  # <class 'str'>
type(True)     # <class 'bool'>
```

---

## Numbers

Python has two numeric types:

| Type | Example | When to use |
|---|---|---|
| `int` | `age = 25` | Whole numbers |
| `float` | `price = 19.99` | Decimal numbers |

### Arithmetic operators

```python
10 + 5    # 15
20 - 7    # 13
6 * 4     # 24
10 / 2    # 5.0  — division always returns float
10 // 3   # 3    — floor division, drops the decimal
5 ** 2    # 25   — exponentiation
```

### Gotchas

**Division always returns a float** — even `10 / 2` gives `5.0`, not `5`. Use `//` when you need an integer result.

**Commas create tuples, not numbers** — `1,000,000` is a tuple of three values. Use underscores for readability:

```python
million = 1_000_000   # correct
million = 1,000,000   # wrong — this is a tuple (1, 0, 0)
```

**Dot is the decimal separator** — `3,14` creates a tuple, not the float `3.14`.

---

## Strings

A string is any sequence of characters wrapped in quotes. Python accepts single or double quotes — pick one and stay consistent.

```python
name = "Alice"
language = 'Python'
message = "It's easy!"   # use double quotes when text contains apostrophes
```

### f-strings (preferred for interpolation)

```python
age = 25
print(f"I am {age} years old")   # "I am 25 years old"
```

f-strings are cleaner than concatenation and handle type conversion automatically — no need to call `str()` manually.

### Concatenation and repetition

```python
"Hello" + " World"   # "Hello World"
"*" * 5              # "*****"
```

### Useful built-ins

```python
len("Hello")         # 5
str(42)              # "42" — convert other types to string
```

### Common errors

- Mismatched quotes: `"Hello'` → `SyntaxError`
- Concatenating string + number: `"Age: " + 25` → `TypeError` — use an f-string or `str(25)`
- Forgetting quotes: `name = Alice` → `NameError` (Python looks for a variable named `Alice`)

---

## Booleans

Booleans hold exactly one of two values: `True` or `False`. Capitalisation is mandatory — `true` and `false` are not valid Python.

```python
is_logged_in = True
has_access = False
can_vote = age >= 18   # evaluates to True or False at runtime
```

### Comparison operators

```python
5 == 5    # True  — equality
5 != 3    # True  — not equal
5 > 3     # True  — greater than
5 < 3     # False — less than
5 >= 5    # True  — greater than or equal
5 <= 4    # False — less than or equal
```

### `=` vs `==`

`=` assigns a value. `==` compares two values. Mixing them up is one of the most common early bugs:

```python
age = 25       # assignment — stores 25 in age
age == 25      # comparison — evaluates to True
```

### Using booleans in conditions

When a variable already holds a boolean, don't compare it to `True` explicitly — it's redundant:

```python
# verbose
if is_logged_in == True:
    ...

# idiomatic
if is_logged_in:
    ...
```

---

## Type conversion

Convert between types with the built-in conversion functions:

```python
int("25")      # 25
float("3.14")  # 3.14
str(42)        # "42"
bool(0)        # False — 0 is falsy; any non-zero number is truthy
```
