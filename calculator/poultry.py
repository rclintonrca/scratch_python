class Duck(object):

    def quack(self):
        print("quack")

    def fly(self):
        print("i am flying")


class Turkey(object):

    def gobble(self):
        print("gobble")

    def fly(self):
        print("I'm flying... only a short dist")


class TurkeyAdapter(object):

    def __init__(self, turkey: Turkey):
        self.turkey = turkey
    
    def fly(self):
        for _ in range(5):
            self.turkey.fly() 
    
    def quack(self):
        self.turkey.gobble()

def duck_interactions(duck: Duck):
    duck.quack()
    duck.fly()

if __name__ == "__main__":
    turkey = Turkey()
    duck = Duck()
    poultry = TurkeyAdapter(turkey)
    # poultry.quack()
    # poultry.fly()
    duck_interactions(poultry)
    duck_interactions(duck)