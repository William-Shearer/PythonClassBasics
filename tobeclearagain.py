
class TestClass:

    # Create a class with two attributes. The first is mangled.    
    def __init__(self):
        self.__c = 0
        self._b = 0
    
    
    # Create the properties, which are decorated functions.
    # property by itself is a getter...
    @property
    def c_value(self):
        try:
            return float(self.__c)
        except ValueError:
            pass
    
    
    # The name of the function with setter creates the setter.     
    @c_value.setter
    def c_value(self, c):
        try:
            self.__c = float(c)
        except (ValueError, TypeError) as error:
            print(f"There was this error: {error}")
        
        
    @property
    def d_value(self):
        try:
            return float(self._d)
        except ValueError:
            pass
        
        
    @d_value.setter
    def d_value(self, d):
        try:
            self._d = float(d)
        except (ValueError, TypeError) as error:
            print(f"There was this error: {error}")
            
    
    # First a static method.
    # Static methods DO NOT need self passing, and can work as class or instance methods.
    # Note, no reference to the class or instance.
    @staticmethod
    def adder(c, d):
        try:
            return c + d
        except ValueError as error:
            return error
            
            
    # Finally, a class method.
    # This differs in that it has the class (cls) as the first argument instead of the instance (self).
    @classmethod
    def subtractor(cls, c, d):
        try:
            return c - d
        except ValueError as error:
            return error
            
    
    # First, a vanilla method.
    def multiplier(self, c, d):
        try:
            return c * d
        except ValueError as error:
            return error
            
            
print("\nClass tester\n")
# Time to test it all...
# Let's not make an instance, yet.
# First test, as a static method.
print("Static Method:      ", TestClass.adder(5, 5))

# Now, test a class method...
print("Class Method:       ", TestClass.subtractor(15, 5))

# Finally, try a normal function contained in a class.
try:
    print("Class Function:     ", TestClass.multiplier(2, 5))
except TypeError as error:
    print("Class Function:      Cannot access class functions this way. Needs the instance.")
    
# Try one it one more time, attempting to cheat it with a fake instance...
try:
    print("Class Function:     ", TestClass.multiplier(self, 2, 5))   
except NameError as error:
    print("Class Function:      Cannot access with faked instance. Needs the real instance.")
    
# So, let us make an instance.
calculator = TestClass()

# Use the properties to set the attributes, as we should.
calculator.c_value = 2
calculator.d_value = 7
# Does not matter if it is mangled or not, if you use the correct property to set the attribute.
print("calculator.c_value: ", calculator.c_value)
print("calculator.d_value: ", calculator.d_value) 

# Now, test each of the methods and the function in turn.
# First, the static method...
print("Static Method:      ", calculator.adder(calculator.c_value, calculator.d_value))

# Use the properties to set the attributes...
calculator.c_value = 15
calculator.d_value = 5

# Now test the class method...
print("Class Method        ", calculator.subtractor(calculator.c_value, calculator.d_value))

# Use the properties to set the attributes...
calculator.c_value = 2
calculator.d_value = 5

# Finally, test the function, which now should work because it passes itself an instance...
print("Class Function:     ", calculator.multiplier(calculator.c_value, calculator.d_value))

# As a last exercise, try to do things the way they should not be done.
# Here, we attempt to change the values of __c and _d with a direct access...
# Remember, the last value of __c was 2, and _d was 5
# If both are changed successfully, the answer will be 10.
# If .__c was changed successfully but not ._d, the answer will be 13.
# and if ._d was changed successfully, but not .__c, the answer will be -6.
calculator.__c = 18
calculator._d = 8

# Note that trying (unsuccessfully) to alter the value of a mangled attribute does NOT require
# any error trapping sequences, like try/except. It is handled automatically. 
# That is, there was no need for...
# try:
#     calculator.__c = 18
# It just ignores the attempt, without altering or throwing an error.

# And we will use the class method of subtractor to see if we had any effect...
print("Class Method        ", calculator.subtractor(calculator.c_value, calculator.d_value))


# Everything works fine, like this. Study this for a summary on class attributes, functions and methods.
    
print()