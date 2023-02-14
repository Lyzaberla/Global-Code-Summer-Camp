#calculate surface area and volume of a sphere
radius=int(input('input any radius of a sphere'))
import math
surf_area=4*math.pi*radius*radius
vol=4/3 *math.pi*radius*radius*radius
print('surface area is %.2f'%surf_area)
print('volume is %.2f'%vol)

#tell a user the current time and date
name=input('hello user,please input your name')
type(name)
import datetime
now = datetime.datetime.now()
print('hello,'+name+' the current time and and date is')
print(now.strftime("%d-%m-%y %H:%M:%S"))

#split sentence into words
sentence='global code has been educative so far'
splitsentence =sentence.split(' ')
print(splitsentence)

#join list of words in sentence
word_list = [['Global'], ['code'], ['has'], ['been'], ['educative'], ['so'], ['far']]
print(' ' .join(word[0] for word in word_list))

