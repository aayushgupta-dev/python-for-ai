message = "  I love Python programming and Python is great!  "

# --- Case methods ---
print(message.strip().lower())
print(message.strip().upper())
print(message.strip().title())

# --- Whitespace and character stripping ---
padded = "  hello world  "
print(padded.strip())          # removes both sides

price = "$19.99"
print(price.strip("$"))        # removes leading $

# --- Search methods ---
clean = message.strip()
print(clean.find("Python"))    # index of first occurrence
print(clean.count("Python"))   # total occurrences

# --- Replace ---
print(clean.replace("Python", "JavaScript"))

# --- Starts / ends with ---
print(clean.startswith("I"))
print(clean.endswith("!"))

# --- Membership test ---
print("Python" in clean)
print("Ruby" in clean)

# --- Concatenation and f-strings ---
first = "John"
last = "Doe"
full = first + " " + last
print(f"Full name: {full}")
print(f"Message length: {len(clean)}")
