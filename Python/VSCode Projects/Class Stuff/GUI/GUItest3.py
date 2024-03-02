class Player():
    name = 'DefaultName'
    
    def __init__(self, name):
        self.name = name
        
    def Attack(self, condition):
        print(self.name, "Attacks!", condition)
    
    def Block(self, condition):
        print(self.name, "Blocks!", condition)

John = Player('John')

print(John.name)