import random
import csv

def onektup(tuple_count):
    unique1=[]
    unique2=[]
    string4=["AAAA","HHHH","OOOO","VVVV"]
    stringlist=[]
    convertedstring=""
    for i in range(48):
        stringlist.append('x')
    #print(stringlist)
    for st in stringlist:
            convertedstring+=st
    #print(convertedstring)
    with open('TENKTUP.csv', mode='w',newline='', encoding='utf-8') as onektup:
        rownames = ['unique1', 'unique2','two','four','ten','twenty','onePercent','tenPercent','twentyPercent','fiftyPercent','unique3','evenOnePercent','oddOnePercent','stringu1','stringu2','string4']
        data_writer = csv.DictWriter(onektup,fieldnames=rownames)
        data_writer.writeheader()
        
        unique2 = list(range(0, tuple_count))
        unique1 = random.sample(unique2, tuple_count)
        #print(unique1)
        
        for i in range(tuple_count):            
            data_writer.writerow({
                    "unique1" : unique1[i],
                    "unique2" : unique2[i],
                    "two": unique1[i]%2,
                    "four" : unique1[i]%4,
                    "ten" : unique1[i]%10,
                    "twenty": unique1[i]%20,
                    "onePercent" : unique1[i]%100,
                    "tenPercent" : unique1[i]%10,
                    "twentyPercent" : unique1[i]%5,
                    "fiftyPercent" : unique1[i]%2,
                    "unique3" : unique1[i],
                    "evenOnePercent":(unique1[i]%100)*2,
                    "oddOnePercent": ((unique1[i]%100)*2)+1,
                    "stringu1":convert(unique1[i]),
                    "stringu2":convert(unique2[i]),
                    "string4":string4[unique2[i]%4]+convertedstring
    })
if __name__ == '__main__':
    tuple_count = 10000
    onektup(tuple_count)
	
def convert(unique):
    result=['A','A','A','A','A','A','A']
    tmp=[65,65,65,65,65,65,65]
    i=6
    while(unique>0):
        rem=unique % 26
        tmp[i]=ord('A')+rem
        unique=int(unique/26)
        i=i-1
    for j in range(7):
        result[j]=tmp[j]    
    string = ""   
    for k in result:
        string += chr(k)
    #print(string)
    stringlist=[]
    for i in range(45):
        stringlist.append('x')
        convertedstring=""
        for st in stringlist:
            convertedstring+=st     
        #print(convertedstring)
    return string+convertedstring
