from pprint import pprint

class Pilots:

    total_pilots = 0
    
    def __init__(self, name, surname, cert_no, hours):
        
        self.__name = name.strip().capitalize()
        self.__surname = surname.strip().capitalize()
        self.__cert_no = cert_no.strip().upper()
        self.__hours = hours
        

    def __str__(self):
        return f"{self.__name} {self.__surname}, Lic No. {self.__cert_no}, with {self.__hours:,} hours."
    
    @property
    def pilot_name(self):
        return self.__name
        
    @pilot_name.setter
    def pilot_name(self, name):
        self.__name = name.strip().capitalize()
        
    @property
    def pilot_surname(self):
        return self.__surname
        
    @pilot_surname.setter
    def pilot_surname(self, surname):
        self.__surname = surname.strip().capitalize()
        
    @property
    def cert_number(self):
        return self.__cert_no
        
    @cert_number.setter
    def cert_number(self, cert_no):
        self.__cert_no = cert_no
        
    @property
    def hours(self):
        return self.__hours
        
    @hours.setter
    def hours(self, hours):
        try:
            self.__hours = int(hours)
        except ValueError as error:
            self.__hours = None
    
    
if __name__ == "__main__":
    # Set the data in each new instance.
    p1 = Pilots("hugh", "asgard", "PTLA1876", 7543)
    p2 = Pilots("james", "wharsnot", "PC1986", 3495)
    p3 = Pilots("grace", "padino", "PTLA2012", 6934)
    
    # Print out the actual __dict__ for each instance...
    print()
    pprint(p1.__dict__)
    pprint(p2.__dict__)
    pprint(p3.__dict__)
    print()
    
    # Copy the __dict__ attribute and access it. Doing this is okay.
    # You cannot work directly with the __dict__, however. It is reserved for the class inner workings.
    p1_dict = p1.__dict__.copy()
    print(f"{p1_dict['_Pilots__name']} {p1_dict['_Pilots__surname']}, License Number: {p1_dict['_Pilots__cert_no']}, with {p1_dict['_Pilots__hours']:,} hours.")
    
    print("\n")