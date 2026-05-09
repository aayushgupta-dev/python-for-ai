# String Manipulation

**Relevant script:** [`scripts/basics/string_manipulation.py`](../scripts/basics/string_manipulation.py)  
**Source:** [python.datalumina.com/basics/string-manipulation](https://python.datalumina.com/basics/string-manipulation)

---

## Concatenation and f-strings

Join strings with `+`, or embed variables directly with f-strings (preferred):

```python
first = "John"
last  = "Doe"

full = first + " " + last          # concatenation
print(f"Full name: {full}")        # f-string interpolation
```

f-strings are cleaner and handle type conversion automatically — no need for `str()` calls.

**Common mistake:** forgetting the `f` prefix:

```python
print("Hello {first}")    # prints literally: Hello {first}
print(f"Hello {first}")   # prints: Hello John
```

---

## Case methods

```python
message = "  I love Python programming!  "

message.strip().lower()    # "i love python programming!"
message.strip().upper()    # "I LOVE PYTHON PROGRAMMING!"
message.strip().title()    # "I Love Python Programming!"
```

Methods can be chained — each returns a new string, leaving the original unchanged.

---

## Stripping whitespace and characters

```python
"  hello world  ".strip()    # "hello world" — removes both sides
"$19.99".strip("$")          # "19.99"        — removes a specific character
```

---

## Searching inside strings

```python
clean = "I love Python programming and Python is great!"

clean.find("Python")     # 7  — index of first occurrence (-1 if not found)
clean.count("Python")    # 2  — total number of occurrences
```

---

## Replacing text

```python
clean.replace("Python", "JavaScript")
# "I love JavaScript programming and JavaScript is great!"
```

`replace()` substitutes every occurrence by default. The original string is not modified.

---

## Starts / ends with

```python
clean.startswith("I")       # True
clean.endswith("!")         # True
clean.startswith("Python")  # False
```

Useful for validation — checking file extensions, URL prefixes, command prefixes, etc.

---

## Membership test with `in`

```python
"Python" in clean    # True
"Ruby"   in clean    # False
```

`in` returns a boolean, so it works directly in `if` conditions:

```python
if "Python" in clean:
    print("Found it")
```

---

## Quick reference

| Method | What it does |
|---|---|
| `lower()` | All lowercase |
| `upper()` | All uppercase |
| `title()` | Capitalise each word |
| `strip()` | Remove edge whitespace (or a given char) |
| `find(x)` | Index of first `x`, or `-1` |
| `count(x)` | Number of times `x` appears |
| `replace(a, b)` | Replace all `a` with `b` |
| `startswith(x)` | `True` if string begins with `x` |
| `endswith(x)` | `True` if string ends with `x` |
| `len(s)` | Number of characters in `s` |
| `x in s` | `True` if `x` is found anywhere in `s` |
