class A:
    def __init__(self, i=0):
        self.i = i


class C:
    def __init__(self, k=1):
        self.k = k

class B(A,C):
    def __init__(self, j=0):
        A.__init__(self)
        C.__init__(self)
        self.j = j


def main():
    b = B()
    print(b.i)
    print(b.j)
    print(b.k)
main()