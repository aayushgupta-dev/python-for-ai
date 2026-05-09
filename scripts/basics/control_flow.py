temperature = 35
age = 20
has_license = True
score = 72

# --- Basic if ---
if temperature > 30:
    print("It's hot!")

# --- if-else ---
if temperature > 30:
    print("Turn on AC")
else:
    print("No AC needed")

# --- if-elif-else chain ---
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# --- Logical operators in conditions ---
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

if age >= 16 or has_license:
    print("Eligible for provisional license")

if not has_license:
    print("Needs to get a license first")

# --- Nested conditions ---
if age >= 18:
    if has_license:
        print("Can drive independently")
    else:
        print("Adult but no license yet")
else:
    print("Too young to drive")
