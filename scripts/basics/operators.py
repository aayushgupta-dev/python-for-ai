age = 15
has_license = True
drunk = False

# Logical operators
can_drive = age >= 16 and has_license
can_drink = age >= 21 and has_license and not drunk
is_adult = age >= 18 or has_license

# Logging the results
print(f"Can drive: {can_drive}")
print(f"Can drink: {can_drink}")
print(f"Is adult: {is_adult}")