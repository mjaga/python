numberInput = input("Enter a number ")
print ("Your age is: ", numberInput)
print(type(numberInput)); strng = '';
num = 1;
while num <= int(numberInput):
        strng = '';  
        if num % 3 == 0:
            strng = strng + 'fizz';
        if num % 5 == 0:
            strng =  strng + 'buzz';
        if num % 5 != 0 and num % 3 != 0:
            strng = num;
        print(strng)
        num += 1;


         