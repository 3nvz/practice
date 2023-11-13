class Foo:
    def __init__(self, name):
        self.name = name
    
a = Foo("a")
b = Foo("b")
a.name = b.name
b.name = "c"
a.x = 2
b.x = 1
x = (a.x + b.x) * (a.name + b.name)

print(x)