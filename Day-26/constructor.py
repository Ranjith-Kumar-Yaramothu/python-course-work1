'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to Instagram, {self.username}")

Ranjith = Instagram('Ranjith','345678')
'''

'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._post
  
Ranjith = Instagram('Ranjith','2345678')
print(Ranjith.username)
print(Ranjith.getpassword())
print(Ranjith.accesspost)
'''


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    def setpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)
  
Ranjith = Instagram('Ranjith','2345678')

print(Ranjith.username)
print(Ranjith.getpassword())
print(Ranjith.accesspost)

Ranjith.username = 'Ranjith_436'
print(Ranjith.username)

Ranjith.setpassword('Ranjith@1526')
print(Ranjith.getpassword())

Ranjith.accesspost = 'kerela'
Ranjith.accesspost = 'goa'
Ranjith.accesspost ='munnar'
print(Ranjith.accesspost)