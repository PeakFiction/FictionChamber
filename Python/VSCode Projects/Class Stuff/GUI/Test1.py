class A:
    def __init__(self, i=0):
        self.i=i #i would be 0
    def m1(self):
        self.i += 1 #add i of itself with a 1 and it becomes the new self.i

class B(A):
    def __init__(self, j = 0): #j would be equal to 0
        super().__init__(3) 
        self.j = j #j equals to J itself
    
    def m1(self):
        self.i += 1

def main():
    b = B()
    b.m1()
    print(b.i)
    print(b.j)

main()