'''
class Fancode:
    pass
Dinesh = Fancode()
Ranjith = Fancode()
Rasool = Fancode()
dipak = Fancode()
'''
'''
class Fancode:
    discount = 88
    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Fancode page',self.name)

Ranjith = Fancode()
Ranjith.info('Dinesh',9618535842,'Hyd')
Dinesh = Fancode()
Dinesh.info('Ranjith',9618535862,'Zym')
Rasool = Fancode()
Rasool.info('Rasool',9618535862,'Pak')
dipak = Fancode()
dipak.info('dipak',9618535862,'Mars')
'''
class Flipkart:
    discount = 30

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("Updated Discount:",cls.discount)

    
    def info(self,name,phonenum,address):
        self.name = name
        self.phonenum = phonenum
        self.address = address
        print(f'Welcome to the flipkart',self.name)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is going,grab it")
 
Ranjith = Flipkart()
Ranjith.info('Ranjith',9876543210,'hyd')
Ranjith.updatediscount()
Ranjith.banner()

Rasool  = Flipkart()
Rasool.info('Rasool',9876543210,'hyd')
Rasool.updatediscount()
Rasool.banner()

Dinesh = Flipkart()
Dinesh.info('Dinesh',9876543210,'hyd')
Dinesh.updatediscount()
Dinesh.banner()