class GeneralFunction():
    
    def __init__(self, a, b):
        try:
            self._a = float(a)
            self._b = float(b)
        except (ValueError, TypeError) as error:
            exit(f"A {error} was thrown")
      
    
    # Here is an example of how a function in a class can be used both as a class method
    # or as a class function, externally.
    # Note, self is not used anymore, here. Use cls, and it serves the double purpose
    # as demonstrated at the bottom of the code. 
    # The classmethod decorator appears to be necessary for enabling this versatility.
    # This is pretty straight forwards, otherwise. Go to the bottom to see
    # the usage...
    @classmethod
    def multiplier(cls, a, b):
        try:
            return float(a) * float(b)
        except (ValueError, TypeError) as error:
            exit(f"{error} in input values")

    
    @classmethod
    def divider(cls, a, b):
        try:
            return float(a) / float(b)
        except (ValueError, TypeError, ZeroDivisionError) as error:
            exit(f"{error} in input values")
        
    
    @classmethod
    def adder(cls, a, b):
        try:
            return float(a) + float(b)
        except (ValueError, TypeError) as error:
            exit(f"{error} in input values")

    
    @classmethod
    def subtractor(cls, a, b):
        try:
            return float(a) - float(b)
        except (ValueError, TypeError) as error:
            exit(f"{error} in input values")

    
    @classmethod
    def squarer(cls, a):
        try:
            return float(a) * float(a)
        except (ValueError, TypeError) as error:
            exit(f"{error} in input values")

    
    @classmethod
    def powerer(cls, a, b):
        try:
            return float(a) ** float(b)
        except (ValueError, TypeError) as error:
            exit(f"{error} in input values")

            
    @property
    def value_a(self):
        return self._a
        
    @value_a.setter
    def value_a(self, a):
        try:
            self._a = float(a)
        except ValueError:
            pass
            
    @property
    def value_b(self):
        return self._b
    
    @value_b.setter
    def value_b(self, b):
        try:
            self._b = float(b)
        except ValueError:
            pass
            

# Here, the functions are being used externally to perform
# operations on any numbers passed to it. No instance of a class
# has been made, it is called directly from the class for one off use.
# Note that with cls in the function arguments (above), there is
# no need to supply a parameter for the object, as it should be.
# If self were used, the function expects an argument, and throws an error.          
print(GeneralFunction.adder(2, 3))
print(GeneralFunction.divider(10.5, 10))
print(GeneralFunction.powerer(6.8, 5.7))

# Here an instance of GeneralFunction is created, and then the function is
# used as a method, instead.
mathemat = GeneralFunction(2, 10)

# The method may then use other methods to define parameters, or
# accept the arguments directly.
print(mathemat.adder(mathemat.value_a, mathemat.value_b))
print(mathemat.multiplier(5, 4))
mathemat.value_a = 6
mathemat.value_b = 2
print(mathemat.divider(mathemat.value_a, mathemat.value_b))
