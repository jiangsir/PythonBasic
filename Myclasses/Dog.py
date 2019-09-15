class Dog():
    #-------------------    
    # __init__ 建構元
    #-------------------
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def humanage(self):
        return 22+(self.age - 2) * 5
