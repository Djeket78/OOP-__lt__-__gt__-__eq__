class Box:
    def __init__(self,value=None):
        self.value=value
        
    def __eq__(self,value=None):
        return self.value ==value
        
    def __lt__(self,value=None):
        if value==None:
            value=0
        return self.value < value
    
    
    def __gt__(self,value=None):
        if value==None:
            value=0
        return self.value >value
        
    def isEmpty(self):
        if self.value == None:
            return True
        else:
            return False
        
        
        
        
#################################33
b1 = Box(30)

b2 = Box()

print(b1==b2)
print(b1<b2)
print(b1>b2)

if b1.isEmpty():
    print("the BOX1 is empty")

        
if b2.isEmpty():
    print("the BOX2 is empty")

         