class TestClass:

    varbon = 5
    
    def __init__(self):
        self.varbee = 10
        
    def changevar(self):
        self.varbon = 15
        
    @classmethod
    def changevarM(cls):
        cls.varbon = 20
        
    @classmethod
    def changeinstancevarNM(cls):
        cls.varbee = 30
        

TestClass.changevar = classmethod(TestClass.changevar)
    
TestClass.changevar()
print(TestClass.varbon)

TestClass.changevarM()
print(TestClass.varbon)

testtest = TestClass()

testtest.changeinstancevarNM()
print(testtest.varbee)