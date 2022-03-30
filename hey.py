class numbers:
    def __iter__(self):
        self.a = 1
        return(self)

    def __next__(self):
        x = self.a
        self.a += 1
        return (x)

mynumber = numbers()
myiter = iter(mynumber)

print(next(myiter))