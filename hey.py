class numbers:
    def __iter__(n):
        n.number = 1
        return n
    def __next__(n):
        x = n.number
        n.number += 1
        return x
myclass = numbers()
s = iter(myclass)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
 