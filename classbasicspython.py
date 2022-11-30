class BasePlatform():
    
    total_number = 0
    
    def __init__(self, x, y, spd, hdg):
        self._x = x
        self._y = y
        self._spd = spd
        self._hdg = hdg
        BasePlatform.total_number += 1
    
    def __del__(self):
        BasePlatform.total_number -= 1
    
    # CREATE A DEFAULT
    @classmethod
    def create_default(cls):
        return BasePlatform(100.0, 100.0, 12.0, 45.0)
    
    # GET ATTRIBUTES
    def _get_x(self):
        return self._x
    
    def _get_y(self):
        return self._y
        
    def _get_spd(self):
        return self._spd
    
    def _get_hdg(self):
        return self._hdg
    
    # SET ATTRIBUTES
    # Note, some basic error checking should always be included for setters.
    # Users may somehow input strings of characters, and this needs filtering.
    def _set_x(self, x):
        try:
            self._x = float(x)
        except ValueError:
            pass
    
    def _set_y(self, y):
        try:
            self._y = float(y)
        except ValueError:
            pass
    
    def _set_spd(self, spd):
        try:
            self._spd = float(spd)
        except ValueError:
            pass
    
    def _set_hdg(self, hdg):
        try:
            self._hdg = float(hdg)
        except ValueError:
            pass
    
    # DELETE ATTRIBUTES
    def _del_x(self):
        del self._x
    
    def _del_y(self):
        del self._y
    
    def _del_spd(self):
        del self._spd
    
    def _del_hdg(self):
        del self._hdg
    
    # ATTRIBUTE PROPERTIES
    x_pos = property(
        fget = _get_x,
        fset = _set_x,
        fdel = _del_x,
        doc = "self._x property"
        )
    
    y_pos = property(
        fget = _get_y,
        fset = _set_y,
        fdel = _del_y,
        doc = "self._y property"
        )
    
    speed = property(
        fget = _get_spd,
        fset = _set_spd,
        fdel = _del_spd,
        doc = "self._spd property"
        )
    
    heading = property(
        fget = _get_hdg,
        fset = _set_hdg,
        fdel = _del_hdg,
        doc = "self._hdg property"
        )
    

# Class made with inheritance from BasePlatform
# This class adds a z axis position attribute to the base class, so that aircraft altitude can be represented.
# Instances derived from this class should have access to all the base class attributes and methods,
# as well as the new attribute.
class CombatAircraft(BasePlatform):
    
    # The first init is the general one, for the new class.
    def __init__(self, x, y, z, spd, hdg):
        # super() is used to give access to all the attributes and methods in the base class.
        # What it does is initialize the BasePlatform class that is inherited.
        # Then, the new attribute is initialized separately.
        # To see how it works, comment the line out and try to run the program.
        # Despite being an inherited class, there is no access to x_pos, for example,
        # without super().
        super().__init__(x, y, spd, hdg)
        self._z = z
        # Do note something important. There is no need to place self in the init call for a super().__init__().
        # The self belongs to the inherited class.
    
        
    @classmethod
    def create_aircraft_default(cls):
        return CombatAircraft(50, 50, 50, 100, 345)
        
    def _get_z(self):
        return self._z
        
    def _set_z(self, z):
        try:
            self._z = float(z)
        except ValueError:
            pass
        
    def _del_z(self):
        del self._z
        
    z_pos = property(
        fget = _get_z,
        fset = _set_z,
        fdel = _del_z,
        doc = "self._z property"
        )
    
# Now, decorators...
# The above can be written again using decorators, as such.
# It replaces the need to collect functions in a property, and puts them in directly.

class ComabtAircraftMod(BasePlatform):
    
    def __init__(self, x, y, z, spd, hdg):
        super().__init__(x, y, spd, hdg)
        self._z = z
            
     
    @property
    def z_pos(self):
        # Here, some error checking is added to the getter. Why?
        # If the user deleted the attribute, and then tried to call it, 
        # an AttributeError would be thrown.
        # This is the better way to handle it, inside the class.
        try:
            "self._z property"
            return self._z
        except AttributeError:
            print("No attribute")

        
    @z_pos.setter
    def z_pos(self, z):
        try:
            self._z = float(z)
        except ValueError:
            print("Cannot convert to float.")
    
    @z_pos.deleter
    def z_pos(self):
        try:
            del self._z
        except AttributeError:
            print("Attribute already deleted.")
        
        
   
        
A10CAS = CombatAircraft(250.0, 175.0, 22.5, 75.0, 210.0)
# Get the id of the instance
print(f"The id of this instance is {id(A10CAS)}")
# Test if it is an instance of the class...
print(f"A10CAS is an instance of CombatAircrat class: {isinstance(A10CAS, CombatAircraft)}")
print(A10CAS.z_pos)
print(A10CAS.x_pos)
# Recover the name of the class...
print(f"Here is the class name:\n{CombatAircraft.__name__}\n")
# Print what the class contains in its dict...
print(f"Here is the class dict:\n{CombatAircraft.__dict__}\n")

A10CASM = ComabtAircraftMod(300.0, 375.0, 52.5, 245.0, 100.0)
print(f"The id of this instance is {id(A10CASM)}")
print(f"A10CASM is an instance of CombatAircrat class: {isinstance(A10CASM, CombatAircraft)}\n")
print(A10CASM.z_pos)
print(A10CASM.x_pos)
A10CASM.x_pos = "100"
print(A10CASM.x_pos)

# Note, deleting attributes should be handled with error checking.
# Here is an example, using hasattr to look for the attribute.
# Be careful not to confuse properties and attributes, here...
# x_pos is the property,
# but...
# _x is the attribute.
# Also note, when looking for an attribute with hasattr, express the attribute as a string.
for _ in range(2):
    if hasattr(A10CAS, "_x"):
        print("The x_pos attribute exists.\nDeleting it now.")
        del A10CAS.x_pos
    else:
        print("The x_pos attribute does not exist.")
        
A10CASM.z_pos = "one hundred and fifty"
print(A10CASM.z_pos)

# Here, to make the coding tidier, the attribute error checking is placed in the 
# deleter property in the code for the class.
# It is now not necessary to use hasattr() anymore. 
del A10CASM.z_pos
print(A10CASM.z_pos)
del A10CASM.z_pos

# delete the whole instance...
del A10CAS

# Double deletion is not a good thing, throws a NameError...
try:
    del A10CAS
except NameError:
    print("Already deleted.")
    

    