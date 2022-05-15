# Python Truth Values 

# False and None evaluate to false
# Numeric zro values: 0, 0.0, 0j
# Decimal (0), Fraction(0,x)
# Empty sequences/collections: "", (), [], {}
# Empty seets and ranges: set(), range()


# Custom objects are default set to True... unless they over-ride 
# bool function and return a false value (Return Falsee)
# len function and return an object of 0 (Return 0)

class myClass:
    def __bool__(self):
        return False
    def __len__(self):
        return 0

# Boolean Operators 
x = 1; y = 5

x and y == 1 # True if x and y are both true
x or y == 1  # True if either x or y are true 
not x        # if X is false, then true, else false 


