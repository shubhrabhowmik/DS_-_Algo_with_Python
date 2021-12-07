class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print("Cookie one is", cookie_one.get_color())
print("Cookie two is", cookie_two.get_color())

cookie_one.set_color('red')

print(cookie_one.get_color())
print(cookie_two.get_color())

########################################################

# class LinkedList:
#     def __init__(self, value):

#     def append(self, value):

#     def pop(self):

#     def prepend(self, value):

#     def insert(self, index, value):

#     def remove(self, index):
