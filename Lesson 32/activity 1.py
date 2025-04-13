class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if self.a<other.a:
            return "the first object is smaller than the second object"
        else:
            return "the second object is bigger than the frist object"
    def __eq__(self,other):
        if self.a==other.a:
            return "the first object is equals to the second object"
        else:
            return "the first objects doesn't equal the second object"
        
ob1 = A(2)
ob2 = A(5)
print(ob1<ob2)

ob3 = A(4)
ob4 = A(4)
print(ob3==ob4)