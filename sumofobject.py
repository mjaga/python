import unittest
class SumOfObject:
   def __init__(self, Obj):
       self.mainObj = Obj
   def display(self): 
        print('Main object:',self.mainObj);
        addvalue = 0;
        for i in self.mainObj:
           addvalue += self.mainObj[i];
    
        print('total value:',addvalue);


output = SumOfObject({"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35})
output.display()    

