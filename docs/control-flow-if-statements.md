# Control Flow & If Statements

**Relevant script:** [`scripts/basics/control_flow.py`](../scripts/basics/control_flow.py)  
**Sources:** [python.datalumina.com/control-flow](https://python.datalumina.com/control-flow) · [python.datalumina.com/control-flow/if-statements](https://python.datalumina.com/control-flow/if-statements)

---

## What is control flow?

By default, Python executes code line by line from top to bottom. Control flow breaks that linearity — it lets programs make decisions and respond differently depending on conditions. This is what makes code behave intelligently rather than just running the same fixed sequence every time.

Real-world examples: a banking app checking credentials before granting access, a weather app picking the right icon based on temperature, a game deciding win/loss conditions.

Prerequisites before this section: variables, data types, comparison operators, and booleans.

---

## If statements

The building block of all control flow in Python. A condition is evaluated; if it is `True`, the indented block runs.

### Basic `if`

```python
if temperature > 30:
    print("It's hot!")
```

The colon `:` is required. The indented block belongs to the `if`. When the condition is `False`, the block is skipped entirely.

### `if-else`

```python
if temperature > 30:
    print("Turn on AC")
else:
    print("No AC needed")
```

`else` is the fallback — it runs when every condition above it is `False`.

### `if-elif-else` chains

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

Python evaluates from top to bottom and executes **only the first matching block** — the rest are skipped. Order matters: put the most specific conditions first.

---

## Logical operators in conditions

Combine multiple conditions in a single `if` using `and`, `or`, and `not`:

```python
# and — both must be True
if age >= 18 and has_license:
    print("Can drive independently")

# or — at least one must be True
if age >= 16 or has_license:
    print("Eligible for provisional license")

# not — reverses the boolean
if not has_license:
    print("Needs to get a license first")
```

---

## Nested conditions

Put `if` statements inside other `if` statements when a secondary check only makes sense after a first condition passes:

```python
if age >= 18:
    if has_license:
        print("Can drive independently")
    else:
        print("Adult but no license yet")
else:
    print("Too young to drive")
```

Each nested level adds one extra level of indentation (4 spaces per level). Deep nesting is a signal to simplify logic with `and`/`or` where possible.

---

## Common errors

| Mistake | Example | Fix |
|---|---|---|
| Missing colon | `if x > 5` | `if x > 5:` |
| Assignment instead of comparison | `if x = 5:` | `if x == 5:` |
| Wrong indentation | Mixed spaces/tabs | Use 4 spaces consistently |
| Wrong condition order in `elif` | Broad check before narrow | Put specific conditions first |
