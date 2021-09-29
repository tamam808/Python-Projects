#creating a class named Base
class Base(object):
    #defining a private method that prints out a sentence
    def __private(self):
        print('This is a private method')
    #defining a protected method that prints out a sentence
    def _protected(self):
        print('This is a protected method')
    #defining a public method that prints out a sentence
    def public(self):
        print('This is a public method')



x = Base()
#we call the public method from the Base class
x.public()
#calling the private method from the Base class
x._Base__private()
#calling the protected method from the Base class
x._protected()
