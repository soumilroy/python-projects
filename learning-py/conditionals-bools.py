print (4 == 3) # False
print (4 != 3) # True
print ("soumil" == "soumil") # True

print ("4" == 4) # False
# print ("10" <= 10) # Error

print (5.6 > 5.4) # True
print (1.23456789 > 1.23456788) # True
print (-1.23456789 < -1.23456788) # True
print (11.000001 > 11.0) # False

print (7.0 == 7) # True ? but why? coersion?
print (10.0 == 10.0) # True
print (11.000001 == 11.0) # False
print (12.3 != 12.3) # False

# Truthy & Falsey values
# Falsey: Empty string ("", ''), 0, 0.0, None, False, (), [], {}
# Truthy: Anything else

print (bool("")) # Falsey
print (bool(0)) # Falsey
print (bool(0.0)) # Falsey
print (bool(None)) # Falsey
print (bool(False)) # Falsey
print (bool(())) # Falsey
print (bool([])) # Falsey
print (bool({})) # Falsey

print (bool(" ")) # True
print (bool(1)) # True
print (bool(1.0)) # True
print (bool(True)) # True
