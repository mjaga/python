class SumAmount:
    def __init__(self, Obj):
        self.mainObj = Obj

    def aggregatetotal(self):
        print('Main object:', self.mainObj);
        addvalue = 0;
        for i in self.mainObj:
            addvalue += self.mainObj[i];

        print('total value:', addvalue);

        return addvalue;


