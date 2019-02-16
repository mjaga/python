initialArray = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1,90, 8, 1,90];
print("array",initialArray);
tempobj={};
for i in initialArray:
  tempobj[i] = initialArray.count(i);
for j in tempobj:
    print(j,'-',tempobj[j]);