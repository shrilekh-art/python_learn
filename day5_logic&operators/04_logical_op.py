# logical operators are used to combine multiple conditions and return a boolean result based on the combined conditions

# Logical Operators → combine conditions

cpu_usage = 70
memory_usage = 50

# Check if system is under pressure
print(cpu_usage > 90 or memory_usage > 90)   # False (both below 90)

# Example with one condition True
cpu_usage = 95
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)   # True (CPU > 90)

# Example with both True
cpu_usage = 95
memory_usage = 92
print(cpu_usage > 90 or memory_usage > 90)   # True (both > 90)


# Example: Movie Night Decision

is_weekend = True
has_popcorn = False
friend_available = True

# Condition: Can watch a movie if it's weekend OR friend is available
print(is_weekend or friend_available)   # True

# Condition: NOT allowed if no popcorn AND no friend
print(not (has_popcorn and friend_available))   # True (since popcorn = False)

# Condition: Perfect movie night if (weekend OR friend available) AND popcorn
print((is_weekend or friend_available) and has_popcorn)   # False (no popcorn)


# Preference using parentheses in logical operators

is_member = True
has_coupon = False
is_holiday = True

# Without parentheses → evaluated left to right
print(is_member or has_coupon and is_holiday)   # True (because 'and' runs first)

# With parentheses → changes priority
print((is_member or has_coupon) and is_holiday) # True (both grouped, then AND holiday)

# Another variation
print(is_member or (has_coupon and is_holiday)) # True (coupon+holiday grouped first)
