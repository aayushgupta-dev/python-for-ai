fruits = ["apple", "banana", "cherry"]

# --- for loop with range ---
for i in range(5):
    print(i)                        # 0 1 2 3 4

# range with start and stop
for i in range(1, 6):
    print(i)                        # 1 2 3 4 5

# range with step
for i in range(0, 10, 2):
    print(i)                        # 0 2 4 6 8

# --- iterating over a string ---
for char in "Python":
    print(char)                     # P y t h o n

# --- iterating over a list ---
for fruit in fruits:
    print(fruit)

# --- while loop ---
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1                      # without this the loop runs forever

# --- while loop with a condition ---
password = "secret"
attempts = 0

while attempts < 3:
    guess = "wrong"                 # simulating a wrong guess
    attempts += 1
    if guess == password:
        print("Access granted")
        break
    print(f"Wrong password. Attempt {attempts} of 3")
