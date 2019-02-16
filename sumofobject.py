mainObj = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
print('Main object:',mainObj);
addvalue = 0;
for i in mainObj:
    addvalue += mainObj[i];
    
print('total value:',addvalue);