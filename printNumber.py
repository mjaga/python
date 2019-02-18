def printnumbers(numberInput):
    if numberInput < 1 :
        # Return inValid Indicator
        return -1;
    num: int = 1;
    while num <= numberInput:
        output = '';
        if num % 3 == 0:
            output = output + 'fizz';
        if num % 5 == 0:
            output = output + 'buzz';
        if num % 5 != 0 and num % 3 != 0:
            output = str(num);
        print(output)
        num += 1;
        # Return Valid Indicator
    return 1;


