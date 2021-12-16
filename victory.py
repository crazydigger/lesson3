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
    famous_persons={names[i]:dates[i]}
    #famous_persons(names[i],dates[i])
print(famous_persons)



count_right=0
for question in names:
    print('name:::',famous_persons[question])
    try:
        print('right answer!!!!!!!!!!!!!!!!', famous_persons[names[0]])
    #except:
        continue


        d_answ=input('введите дату рождения'+question+ 'в формате ddmmyyyy:')
        if(d_answ==famous_persons[question]):

            print('right answer!!!!!!!!!!!!!!!!',famous_persons[question])
    except:
        pass
        count_right+=1