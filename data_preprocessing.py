import pandas as pd
import os
from State import *
from Agent import *
import csv  
header = []
data = []
path_of_the_directory= './dataset/'
print("Files and directories in a specified path:")
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    print("*************************")
    print(f)
    print("*************************")
    if os.path.isfile(f) and f != './dataset/imagenet_b_darija.csv':
        with open(f) as file:
            i = 0
            for line in file:    
                if i == 0 and line.replace(',','',len(line)).replace('"','',len(line)).replace('\n','',len(line)) != "n1n2n3n4eng":
                    break
                i = i + 1
                row = line.replace('\n','',len(str(file))).replace('"','',len(str(file))).split(',')
                row = list(filter(None, row))
                print(row[0] + " ------------------ " + f)
                agent = Agent(expression = row[0],number=20)
                items = agent.getWords(l=3,j=0.95,n=0.95,iter=1000,number=21-len(row))
                row  = row[:-1] + items + [row[-1]]
                data.append(row)
            file.close()
            
header = ['n'+str(i+1) for i in range(20)] + ['eng']

with open('./dataset/data.csv', 'a', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
                

