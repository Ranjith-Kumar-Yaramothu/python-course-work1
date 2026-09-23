'''
class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("you an upload the status for 24hrs")

class whatsappv3(whatsappv2):
    def groups(self):
        print("you can create group and talk with multiple at the same time")

Ranjith = whatsappv1()
Ranjith.message()

Rasool = whatsappv2()
Rasool.message()
Rasool.status()

Dinesh = whatsappv3()
Dinesh.message()
Dinesh.status()
Dinesh.groups()
'''
'''
class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("you an upload the status for 24hrs")

class whatsappv3:
    def groups(self):
        print("you can create group and talk with multiple at the same time")

class whatsappv4:
    def community(self):
        print("you can multiple groups")

class whatsappv5(whatsappv4,whatsappv3,whatsappv2):
    def channels(self):
        print("you can post regulary with huge crowd")

Ranjith = whatsappv5()
Ranjith.message()
Ranjith.status()
Ranjith.groups()
Ranjith.community()
Ranjith.channels()
'''

class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("you an upload the status for 24hrs")

class whatsappv3(whatsappv1):
    def groups(self):
        print("you can create group and talk with multiple at the same time")

class whatsappv4(whatsappv1):
    def community(self):
        print("you can multiple groups")2-