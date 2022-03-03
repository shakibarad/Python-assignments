import statistics
class A:
    count=0
    
    def __init__(self,number,age,height,weight):
        self.age=age
        self.height=height
        self.weight=weight
        self.number=number
        
    def get_number(self):
        k=int(input())
        return k
        
    def get_age(self):
        y = [float(x) for x in input().split()]
        t = statistics.mean(y)
        return t
    
    def get_height(self):
        y = [float(x) for x in input().split()]
        t = statistics.mean(y)
        return t
       
    def get_weight(self):
        y = [float(x) for x in input().split()]
        t = statistics.mean(y)
        return t
    
class B(A):
    def get_number(self):
        k=int(input())
        return k
        
    def get_age(self):
        y = [float(x) for x in input().split()]
        t = statistics.mean(y)
        return t
    
    def get_height(self):
        y = [float(x) for x in input().split()]
        t = statistics.mean(y)
        return t
       
    def get_weight(self):
        y = [float(x) for x in input().split()]
        t = statistics.mean(y)
        return t
        
class_A=A(2,6,9,7)
class_A.get_number()
age_A=class_A.get_age()
height_A=class_A.get_height()

weight_A=class_A.get_weight()

class_B=B(2,6,9,7)
class_B.get_number()
age_B=class_B.get_age()
height_B=class_B.get_height()
weight_B=class_B.get_weight()


print(age_A)
print(height_A)
print(weight_A)

print(age_B)
print(height_B)
print(weight_B)

if height_A>height_B:
    print("A")
elif height_A==height_B:
    if weight_A<weight_B:
        print("A")
    elif weight_A==weight_B:
        print("Same")
    else:
        print("B")
else:
    print("B")

