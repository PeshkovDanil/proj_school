
import json
from pprint import pprint

list2=[]
list1=[]
p=1
schools=set()
Teach = json.load(open('Teachers.json'))
Stud = json.load(open('Students.json'))

cls='6 А'

for el in Teach:
    print('имя учителя:', el['name'])

for el in Stud:
    print('имя ученика:', el['name'])

for el in Stud:
    if el['class']==cls:
            print('ученик учащиеся в ',cls,el['name'],el['surname'])

for el in Teach:
    schools.add(el['school'])
print(schools)


for el in Stud:
    list1.append(el['surname'])
    list2.append(el['name'])

for el in list1:
    for l in list1[p:]:
        if el==l:
            print('однофомильцы:',el)
    p=p+1

# 2.1
print('2.1')
teach_name='Владимир Вышкин'
classlist=[]
for el in Teach:
    if teach_name=='%s %s' % (el['name'], el['surname']):
        classlist=el['class']


for el in classlist:
    for l in Stud:
        if l['class']==el:
            print(l['surname'], l['name'], l['middle_name'])

# 2.2
print('2.2')
stud_name='Матвей Петров'
classlist2=[]

for el in Stud:
    if stud_name=='%s %s' % (el['name'], el['surname']):
        stud_class=el['class']

for el in Teach:
    classlist2=el['class']
    for l in classlist2:
        if l==stud_class:
            print(el['surname'], el['name'], el['middle_name'])