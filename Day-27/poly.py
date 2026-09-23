class Hotstar:
    def __init__(self,name):
        print(f'welcome to the Hotstar, {name}--------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Play start pause")
    def ads(self):
        print("You can see ads")
    def quality(self):
        print("You can see low quality")
    def devices(self):
        print("Single devices")
    def access(self):
        print("Limited access")
    def download(self):
        print("You can download")
class PremiumHotstar(Hotstar):
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Play start pause")
    def ads(self):
        print("You can see ads")
    def quality(self):
        print("You can see low quality")
    def devices(self):
        print("Multiple devices")
    def access(self):
        print("Limited access")
    def download(self):
        print("You can download")

Ranjith = Hotstar("Ranjith")
Ranjith.auth()
Ranjith.dashboard()
Ranjith.search()
Ranjith.history()
Ranjith.playcontrollers()
Ranjith.ads()
Ranjith.quality()
Ranjith.devices()
Ranjith.access()
Ranjith.download()

Rasool = PremiumHotstar("Rasool")
Rasool.auth()
Rasool.dashboard()
Rasool.search()
Rasool.history()
Rasool.playcontrollers()
Rasool.ads()
Rasool.quality()
Rasool.devices()
Rasool.access()
Rasool.download()