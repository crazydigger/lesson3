from random import randint
import random

names = 'а.с.пушкин,л.н.толстой,фмдостоевский,мюлермонтов,апчехов'.split(',')
dates = '9.091928,28.081828,11111921,27061941,29011960'.split(',')
print(names)
print(dates)
famous_persons={}
for i in range(len(names)):
#famous_persons.fromkeys(names)
    famous_persons={names[i]:dates[i]}

i = random.randint(0,len(names))
print('!!!!!!!!!!!!!!!!!random:',i)

#dates=(
