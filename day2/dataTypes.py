# 📒 Python Data Types 
# -----------------------------------
# • Python is dynamically typed → no need to declare types explicitly.
# • Core built-in types:
#   - Numeric: int, float, complex
#   - Sequence: str, list, tuple
#   - Mapping: dict
#   - Set types: set, frozenset
#   - Boolean: bool
#   - Special: NoneType
#
# • Type detection is automatic at assignment.
# • Variables can change type at runtime (flexible but requires caution).
# • Use type() to inspect, isinstance() to validate.
# • Strong typing: operations between incompatible types raise errors.
# • Duck typing: behavior matters more than explicit type.
# • Best practice: keep types consistent for readability and fewer bugs.

# 📒 Python Data Structures 
# ----------------------------------------
# • List → Ordered, mutable, allows duplicates. Ideal for dynamic collections.
# • Tuple → Ordered, immutable, allows duplicates. Good for fixed data sets.
# • Set → Unordered, mutable, unique elements only. Fast membership tests.
# • Frozenset → Immutable version of set. Useful for hashable collections.
# • Dict → Key-value pairs, mutable, unordered (insertion order preserved since 3.7).
#
# • Strings behave like sequences (indexing, slicing).
# • Collections module adds advanced structures:
#   - deque → fast append/pop from both ends
#   - Counter → frequency counts
#   - defaultdict → dict with default values
#   - OrderedDict → dict with guaranteed order (redundant after 3.7)
#
# • Choosing the right structure:
#   - List → general purpose, ordered data
#   - Tuple → fixed records, function returns
#   - Set → uniqueness, fast lookups
#   - Dict → mappings, structured data
#
# • Best practice: prefer immutability (tuple, frozenset) for safety,
#   use mutable types (list, dict, set) for flexibility.

# 📒 Data Types in Python

a = 10        # int
b = 3.15      # float
c = "Hello"   # str
d = 'Hi'      # str
e = "1234"    # str
f = True      # bool
g = False     # bool
h = None      # NoneType
i = ""        # str - blank
j = " "       # str - empty space
