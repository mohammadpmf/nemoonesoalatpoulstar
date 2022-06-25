# # Q 6
# class Person():
#     def __init__(self, name='', family='', age=0):
#         self.name = name
#         self.family = family
#         self.age = age
#     def get_age(self):
#         print (self.age)

# p1 = Person('Mahan', 'Alidoost', 20)
# print(p1.get_age())

# # Q 7
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def test(self, second):
        return (self.x*second.x, self.y*second.y)

p1 = Point(5,4)
p2 = Point(3,2)
res = p1.test(p2)
print(res)


