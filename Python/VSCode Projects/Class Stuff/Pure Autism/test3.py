class A:
    def feature1(self):
        print('Feature 1 Working')
        
    def feature2(self):
        print('Feature 2 Working')


a1 = A()

a1.feature1()
a1.feature2()

class B(A): #Subclass
    def feature3(self):
        print('Feature 3 Working')
        
    def feature4(self):
        print('Feature 4 Working')

b1 = B()

b1.feature1()
b1.feature4()


class C:
    def feature5(self):
        print('Feature 5 Working')
    
    def feature6():
        print('Feature 6 Working ')