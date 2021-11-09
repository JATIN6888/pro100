class Atm(object):
    def __init__(self,cardnumber,pin,username):
        self.cardnumber=cardnumber
        self.pin=pin
        self.username=username
    def start(self):
        print("started")
        
    def stop(self):
        print("stoped")
a=Atm(98765,1234,"chotta Bheem")
print(a.start())

print(a.cardnumber)
print(a.pin)
print(a.username)
