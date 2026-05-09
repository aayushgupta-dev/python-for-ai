# Loops

**Relevant script:** [`scripts/basics/loops.py`](../scripts/basics/loops.py)  
**Source:** [python.datalumina.com/basics/loops](http://python.datalumina.com/basics/loops)

---

## What are loops?

Loops repeat a block of code either a fixed number of times (`for`) or until a condition becomes `False` (`while`). Without loops, repeating an action 100 times would mean writing 100 lines of code.

---

## `for` loops

A `for` loop iterates over a sequence — a range of numbers, a string, a list, or any iterable.

### With `range()`

`range()` generates a sequence of numbers. Python counts from `0` by default (zero-indexing).

```python
for i in range(5):
    print(i)        # 0 1 2 3 4
```

**Three forms of `range()`:**

| Form | Example | Produces |
|---|---|---|
| `range(stop)` | `range(5)` | `0 1 2 3 4` |
| `range(start, stop)` | `range(1, 6)` | `1 2 3 4 5` |
| `range(start, stop, step)` | `range(0, 10, 2)` | `0 2 4 6 8` |

The `stop` value is always excluded — `range(1, 6)` goes up to `5`, not `6`.

### Iterating over a string

```python
for char in "Python":
    print(char)     # P y t h o n
```

### Iterating over a list

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

---

## `while` loops

A `while` loop keeps running as long as its condition is `True`. Use it when you don't know in advance how many iterations you'll need.

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

**Always update the variable** that the condition checks — forgetting to do so creates an infinite loop that never exits.

### Real-world pattern: limiting attempts

```python
attempts = 0

while attempts < 3:
    attempts += 1
    if guess == password:
        print("Access granted")
        break
    print(f"Wrong password. Attempt {attempts} of 3")
```

`break` exits the loop immediately regardless of the condition — useful when you've found what you needed.

---

## `for` vs `while` — when to use each

| Scenario | Use |
|---|---|
| Known number of iterations | `for` with `range()` |
| Iterating over a collection | `for` |
| Repeat until something changes | `while` |
| User input / retry logic | `while` |

---

## Common errors

| Mistake | What happens | Fix |
|---|---|---|
| Missing colon | `SyntaxError` | `for i in range(5):` |
| Wrong indentation | Block runs outside the loop | 4 spaces consistently |
| Off-by-one in `range` | Wrong number of iterations | Remember `stop` is excluded |
| No update in `while` loop | Infinite loop | Always increment/update the condition variable |
