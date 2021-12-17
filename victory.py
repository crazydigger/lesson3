from random import randint
import random
names = "а.с.пушкин,л.н.толстой,фмдостоевский,мюлермонтов,апчехов".split(',')
dates = '9.091928,28.081828,11111921,27061941,29011960'.split(',')
famous_persons={}
for i in range(len(names)):
    famous_persons=famous_persons.fromkeys(names)
    print(names[i],dates[i])
    n = names[i].replace('','')
    d = dates[i].replace('','')
    print('name!!!!!',n)
    print('date=====',d)
    famous_persons={n:d}
    #famous_persons(names[i],dates[i])
print(famous_persons)
def long_date(m):
    months={'01':'январь','02':'февраль','03':'март','04':'апрель','05':'май','06':'июнь','07':'июль','08':'август','09':'сентябрь','10':'октябрь','11':'ноябрь','12':'декабрь'}
    result=''
    try:
        result =months[m]
    except:
        result=''


    return result
for i in range(1,9):
        print(long_date('0'+str(i)))

while(input('повторим?-1нет-0')):
    for i in range(len(names)):
        famous_persons=famous_persons.fromkeys(names)
        print(names[i],dates[i])
        n = names[i].replace('','')
        d = dates[i].replace('','')
        print('name!!!!!',n)
        print('date=====',d)
        famous_persons={n:d}
        #famous_persons(names[i],dates[i])
    print(famous_persons)



    count_right=0
    for i in range(len(names)):








        d_answ=input('введите дату рождения'+names[i]+ 'в формате ddmmyyyy:')
    if(d_answ==dates[i]):

        print('right answer!!!!!!!!!!!!!!!!',d_answ[:3]+long_date(int(d_answ[2:3]))+d_answ[3:])


        count_right+=1
print('gпроцент правильных ответов',round(count_right/len(names)*100,2))
print('gпроцент неправильных ответов',100-round(count_right/len(names)*100,2))
