numberInput = input("Enter a number ")
num = 1;
while num <= int(numberInput):
        output = '';  
        if num % 3 == 0:
            output = output + 'fizz';
        if num % 5 == 0:
            output =  output + 'buzz';
        if num % 5 != 0 and num % 3 != 0:
            output = str(num);
        print(output)
        num += 1;


         