#stupid_cat.py
#input1= open ('point1_output_1.txt' ,'r')
input2=open ('point1_output2.txt' ,'r').read().splitlines()
input3=open ('point1_output3.txt' ,'r')
input4=open ('point1_output4.txt' ,'r')
input5=open ('point1_output5.txt' ,'r')
input6=open ('point1_output6.txt' ,'r')


train1=open ('training2345.txt','w')
train2= open('training3456.txt', 'w')
train3= open ('training4562.txt', 'w')
train4= open ('training5623.txt','w')
train5=open ('training6234.txt', 'w')

train1.write(str(input2) + str(input3) + str(input4) + str(input5))
#train2.write(input3 + input4 + input5 + input6)

train1.close
#train2.close
