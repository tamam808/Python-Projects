

#Parent class User
class User:
    name = 'Tama'
    email = 'tama@gmail.com'
    password = '123abc'
#this function will ask the user to input an email and a password
#if the input values = to the email and password stored it will print a Welcome back message.
#otherwise it will state that one or both of the inputs didnt match
    def getLoginInfo(self):
        entry_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_password == self.password):
            print('Welcome back, {}!'.format(self.name))
        else:
            print('The password or email is incorrect.')

#Child class Employee
class Employee(User):
    base_pay = 11.00
    department = 'General'
    pin_number = '3980'

#this function is the same function from the parent class
#but instead of a password we use a pin number to verify the user
    def getLoginInfo(self):
        entry_email = input('Enter your email: ')
        entry_pin = input('Enter your pin: ')
        if (entry_email == self.email and entry_pin == self.pin_number):
            print('Welcome back, {}!'.format(self.name))
        else:
            print('The pin number or email is incorrect.')


#Child class Customer
class Customer(User):
    cur_balance = 20.00
    cur_orders = 2
    auth_key = '265'

#this function is the same function from the parent class
#but for added security, after verifying the user through the email and password inputs
#it will then ask for an authenticator key
#if the user inputs all the correct information the function will output a greeting that tells the user
#how much money they have in their online account and how many orders they have currently processing
    def getLoginInfo(self):
        entry_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_password == self.password):
            entry_auth = input('Please enter your authenticator key: ')
            if (entry_auth == self.auth_key):
                print('Welcome back, {}!\nYou have ${} in your account and {} order(s) currently in processing!'.format(self.name,self.cur_balance,self.cur_orders))
            else:
                print('You the authenticator key is incorrect.')
        else:
            print('The email or password is incorrect.')


general = User()
general.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

cust = Customer()
cust.getLoginInfo()
