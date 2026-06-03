# Boolean Values and bool() Function

# True / False are the two Boolean values
print(True)          # True
print(False)         # False
print(type(True))    # <class 'bool'>

# bool() converts values into True/False
print(bool(123))     # True (non-zero number)
print(bool("Hi"))    # True (non-empty string)
print(bool())        # False (empty, default = 0)
print(bool(0))       # False (zero is falsy)
print(bool(""))      # False (empty string is falsy)
print(bool(None))    # False (None is falsy)
