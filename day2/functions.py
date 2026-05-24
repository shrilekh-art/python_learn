# 📒 Functions in Python 
# -------------------------------------
# • Functions "do something to data" → input value goes in, new value comes out.
#
# ┌───────────────┐
# │   Value In    │
# └───────┬───────┘
#         │
#         ▼
#     ┌───────────┐
#     │ Function  │
#     └───────┬───┘
#             │
#             ▼
# ┌───────────────┐
# │  New Value    │
# └───────────────┘
#
# • Sources of functions:
#   - User Defined → functions you write yourself (def …)
#   - Standard Library → built-in modules (math, os, sys, etc.)
#   - 3rd-Party Libraries → e.g., Pandas, NumPy, TensorFlow
#
# • Categories of functions:
#   - Standalone functions → e.g., print(), type()
#   - Methods of class → e.g., "Hello".upper(), "Hi".replace("i","o")
#   - Operations (magic methods) → e.g., +, -, >, <, ==, in, or
#
# • Key points:
#   - Functions encapsulate logic → reusable, modular code.
#   - Methods are tied to objects → object-oriented behavior.
#   - Magic methods enable operator overloading → customize behavior of built-ins.
#   - Libraries extend functionality → leverage community and standard tools.
# 📒 Python Standard Library — Expert Notes
# -----------------------------------------
# • The Standard Library is Python’s built-in toolkit → no extra install needed.
# • Covers a wide range of functionality:
#   - System & OS: os, sys, pathlib, shutil
#   - Math & Numbers: math, decimal, fractions, random
#   - Data & Time: datetime, time, calendar
#   - Data Structures: collections, heapq, array
#   - File & I/O: io, csv, json, pickle
#   - Networking & Internet: socket, urllib, http
#   - Concurrency: threading, multiprocessing, asyncio
#   - Utilities: re (regex), logging, functools, itertools
#
# • Advantages:
#   - Reliable, maintained with Python itself
#   - Portable across platforms
#   - Saves time → avoids reinventing common tools
#
# • Best practice:
#   - Prefer stdlib before external libraries
#   - Import only what you need (avoid clutter)
#   - Read official docs → many hidden gems
#
# • Example:
#   import math
#   print(math.sqrt(16))   # 4.0
