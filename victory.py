from random import randint
import random

names = "а.с.пушкин,л.н.толстой,фмдостоевский,мюлермонтов,апчехов".split(',')
dates = '9.091928,28.081828,11111921,27061941,29011960'.split(',')
print(names)
print(dates)
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



count_right=0
for i in range(len(names)):







    d_answ=input('введите дату рождения'+names[i]+ 'в формате ddmmyyyy:')
    if(d_answ==dates[i]):

        print('right answer!!!!!!!!!!!!!!!!')


        count_right+=1
print('gпроцент правильных ответов',round(count_right/len(names)*100,2))