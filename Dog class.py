class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

    def get_info(self):
        print("Coat Color: ", self.coat_color)

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, size):
        super().__init__(name, age, coat_color)
        self.size = size

    def unique_method1(self):
        print("This is a unique method of Jack Russell Terrier")

    def unique_method2(self):
        print("This is a another unique method of Jack Russell Terrier")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def unique_method1(self):
        print("This is a unique method of Bulldog")

    def unique_method2(self):
        print("This is another unique method of Bulldog")

# Creating Dog object
dog1 = Dog("Buddy", 3, "Brown")
dog1.description() 
dog1.get_info()

# Creating JackRussellTerrier object
jack_russell1 = JackRussellTerrier("Max", 5, "White", "Small")
jack_russell1.description()
jack_russell1.get_info()
jack_russell1.unique_method1()

# Creating Bulldog object
bulldog1 = Bulldog("Rocky", 4, "Fawn", "Heavy")
bulldog1.description()
bulldog1.get_info()
bulldog1.unique_method2()

# Output
# Name: Buddy
# Age: 3
# Coat Color: Brown
# Name: Max
# Age: 5
# Coat Color: White
# This is a unique method of Jack Russell Terrier
# Name: Rocky
# Age: 4
# Coat Color: Fawn
# This is another unique method of Bulldog 
