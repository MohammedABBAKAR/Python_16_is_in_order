# Is the String in Order?

# Create a function that takes a string and returns True or False,
# depending on whether the characters are in order or not.
# Examples

# is_in_order("abc") ➞ True

# is_in_order("edabit") ➞ False

# is_in_order("123") ➞ True

# is_in_order("xyzz") ➞ True


# *************************************************

# def is_in_order(txt):
 
#     txt.sort()
#     return txt
# print(is_in_order("edabit"))


def order(txt):
    sorted_txt = sorted(txt)
    return ''.join(sorted_txt)

print(order("edabit"))

# *************************************************
# sorted():

# Returns a new sorted list.
# Does not change the original iterable.
# Can be used with any iterable.
# sort():

# Sorts the list in place.
# Changes the original list.
# Can only be used with lists.
# *************************************************

def is_in_order(txt):
    sorted_txt = sorted(txt)
    newstr = ''.join(sorted_txt)
    if txt == newstr:
        return True
    else:
        return False

print(is_in_order("abc"))

# *************************************************

def is_in_order(txt):
    return txt == ''.join(sorted(txt))

# Examples
print(is_in_order("abc"))     # ➞ True
print(is_in_order("edabit"))