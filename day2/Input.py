# What is input()?
# A built-in Python function that stops your program to get user input

# ┌───────────────┐        ┌───────────────┐
# │    app.py     │        │    Output     │
# │ input("Enter  │        │ Enter Value:  │
# │ Value:")      │        │ 50            │
# └───────┬───────┘        └───────┬───────┘
#         │                        │
#         │ show                   │ Run
#         │                        │
#         ▼                        ▼
# ┌────────────────────────────────────────┐
# │   User at VS Code terminal             │
# │   Types: 50                            │
# └────────────────────────────────────────┘
#         ▲
#         │ Wait for Your Input
#         │
#       Coding

name = input("Enter a value")
print(f"Entered value is {name}")