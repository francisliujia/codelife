class User():
    '''representing a simple user profile'''
    def __init__(self, first_name, last_name, username, email, location):
        '''initiasing the user'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        '''display a summary of the user's info'''
        print(f"name: {self.first_name} {self.last_name}")
        print(f"username: {self.username}")
        print(f"email: {self.email}")
        print(f"location: {self.location}")

    def greet_user(self):
        '''display a message to greet user'''
        print(f"\nWe love you {self.username} !")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempt(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("-This user has no privileges.")


class Admin(User):
    '''a user with administrative privileges'''
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()