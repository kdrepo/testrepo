print("Hello Github")


class laborclass:
    def __init__(self, iq, age):
        self.iq = iq
        self.age = age

    def status(self):
        if self.age >= 25 or self.iq <=120:
            print(self.age, "is old and dumb")
        else: print("You r ok")

        

    
vivek = laborclass(200, 20)
vivek.status()

    
    