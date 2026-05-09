# Operators in Python

**Relevant script:** [`scripts/basics/operators.py`](../scripts/basics/operators.py)  
**Source:** [python.datalumina.com/basics/operators](https://python.datalumina.com/basics/operators)

---

## What are operators?

Operators are symbols that perform operations on values — the "verbs" of the language. Python groups them into four categories.

---

## Arithmetic operators

| Operator | Example | Result | Note |
|---|---|---|---|
| `+` | `10 + 5` | `15` | |
| `-` | `20 - 7` | `13` | |
| `*` | `6 * 4` | `24` | |
| `/` | `10 / 2` | `5.0` | Always returns a float |
| `//` | `10 // 3` | `3` | Floor division — rounds down |
| `%` | `10 % 3` | `1` | Modulo — returns the remainder |
| `**` | `5 ** 2` | `25` | Exponentiation |

Python follows PEMDAS order of operations. Use parentheses to override:

```python
2 + 3 * 4     # 14 — multiplication first
(2 + 3) * 4   # 20 — parentheses first
```

---

## Comparison operators

Comparison operators always return a boolean (`True` or `False`):

```python
5 == 5    # True  — equal to
5 != 3    # True  — not equal to
5 > 3     # True  — greater than
5 < 3     # False — less than
5 >= 5    # True  — greater than or equal
5 <= 4    # False — less than or equal
```

`=` assigns, `==` compares — confusing them is one of the most common Python bugs.

---

## Logical operators

Logical operators combine boolean conditions. From `scripts/basics/operators.py`:

```python
age = 15
has_license = True
drunk = False

can_drive = age >= 16 and has_license   # False — age fails
can_drink = age >= 21 and has_license and not drunk  # False — age fails
is_adult  = age >= 18 or has_license    # True  — has_license saves it
```

| Operator | Rule | Example |
|---|---|---|
| `and` | Both conditions must be `True` | `age >= 18 and has_id` |
| `or` | At least one condition must be `True` | `is_admin or is_owner` |
| `not` | Reverses the boolean value | `not drunk` |

---

## Assignment shortcuts

Rather than writing `x = x + 5`, Python supports compound assignment for all arithmetic operators:

```python
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x /= 4    # x = 6.0
x //= 2   # x = 3.0
x **= 3   # x = 27.0
x %= 5    # x = 2.0
```
