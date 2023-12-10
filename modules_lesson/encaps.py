class UserAccount():
    def __init__(self, email, password, username) -> None:
        self._email = email
        self._password = password
        self._username = username

    def getEmail(self):
        return self.getEmail

    def setEmail(self, address):
        self.setEmail = address
    
    def getPassword(self):
        return self.getPassword
    
    def setPassword(self, new_password):
        self.setPassword = new_password

    def getUsername(self):
        return self.getUsername
    
    def setUsername(self, new_username):
        self.setUsername = new_username

newUser = UserAccount("test@email.com", "Password1", "testUser")

print(newUser.getUsername())
#print(newUser.getUsername())
# newUser.setUsername("RandomUser")
# print(newUser.getUsername())
# #newUser.set_username

# # print(newUser.getEmail())
# newUser.setEmail("newEmail@email.com")
# print(newUser.getEmail())

# newUser.setPassword("newPassword")
# #newUser.setPassword("error")

# # alex = Person(26)

# # print(alex.age())

# # alex.set_age(-1)

# # print(alex.age())

# # alex.set_age(27)