def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

scorearray = [1,2,0,0,4,1,6,2,1,3];
overscoreArray = split(scorearray,6)
firstbatsmen = [];
secondbastmen = [];
currentbatting = 'first'
firstbatsmenscore = 0
secondbatsmenscore = 0
for i in overscoreArray:
    count = 0;
    for j in i:
        count += 1;
        templen = len(i)
        if currentbatting == 'first':
           firstbatsmen.append(j);
           firstbatsmenscore += j;
           if j % 2 != 0:
               currentbatting = 'second'
           else:
               currentbatting = 'first';    
        elif currentbatting == 'second':
            secondbastmen.append(j)  
            secondbatsmenscore += j;
            if j%2 == 0:
                currentbatting = 'second';
            else:
                currentbatting = 'first'    
        if(count == templen):
           if currentbatting == 'second':
                currentbatting = 'first';
           else:
                currentbatting = 'second'; 
print('first batsman score',firstbatsmenscore,firstbatsmen)             
print('second batsman score',secondbatsmenscore,secondbastmen)             


