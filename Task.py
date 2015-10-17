import json
from pprint import pprint

def search( list_of, **kwargs):
    list1=[]
    new_list=[]
    if kwargs.get('class_room'):
        kwargs['class']=kwargs.pop('class_room')
    list1=kwargs.keys()
    for el in list1:
        for l in list_of:
            if l[el]==kwargs[el]:
                new_list.append(l['id'])
    new_list=set(new_list)
    return(new_list)

def get_index(data, surname):
    for el in data:
        if el['surname'] == surname:
            return data.index(el)


list2 = []
list1 = []
p = 1
schools = set()
# teach = json.load(open('Teachers_id.json'))
# stud = json.load(open('Students_id.json'))

with open('Students_id.json', 'r') as f:
   stud = json.load(f)
with open('Teachers_id.json','r') as f:
    teach=json.load(f)

cls = '6 А'

for el in teach:
    print('имя учителя:', el['name'])

for el in stud:
    print('имя ученика:', el['name'])

for el in stud:
    if el['class'] == cls:
        print('ученик учащиеся в ', cls, el['name'], el['surname'])

for el in teach:
    schools.add(el['school'])
print(schools)

for el in stud:
    list1.append(el['surname'])
    list2.append(el['name'])

for el in list1:
    for l in list1[p:]:
        if el == l:
            print('однофомильцы:', el)
    p=p + 1

# 2.1
print('2.1')
teach_name = 'Владимир Вышкин'
classlist = []
for el in teach:
    if teach_name == '%s %s' % (el['name'], el['surname']):
        classlist = el['class']

for el in classlist:
    for l in stud:
        if l['class'] == el:
            print(l['surname'], l['name'], l['middle_name'])

# 2.2
print('2.2')
stud_name = 'Матвей Петров'
classlist2 = []

for el in stud:
    if stud_name == '%s %s' % (el['name'], el['surname']):
        stud_class = el['class']

for el in teach:
    classlist2 = el['class']
    for l in classlist2:
        if l == stud_class:
            print(el['surname'], el['name'], el['middle_name'])

# 3.1
# print('3.1')
for el in stud:
    id1=el['id']
id1=id1+1
new_stud={'name':'Дмитрий',
          'middle_name':'Васильевич',
          'surname':'Егоров',
          'school':'23 Школа',
          'class':'7 В',
          'birth_day':'03.12.1993',
           'id':id1}
stud.append(new_stud)
# print(stud)
all_st_new=json.dumps(stud, ensure_ascii=False)
with open('Students_id.json','w') as stud1:
    stud1.write(all_st_new)
    


# 3.2
print('3.2')
for el in teach:
    id=el['id']
id=id+1
new_teach = {'name': 'Евгений',
             'middle_name': 'Васильевич',
             'surname': 'Романов',
             'school': '43 Школа',
             'class': '6 В',
             'birth_day': '03.12.1993',
             'id':id}
teach.append(new_teach)
# print(teach)
all_teach_new = json.dumps(teach, ensure_ascii=False)
with open('Teachers_id.json','w') as teach1:
    teach1.write(all_teach_new)
    

# 3.3
print('3.3')
surname = 'Черный'
new_class = '7 А'
teach_index = get_index(teach, surname)
teach[teach_index]['class'].append(new_class)
# print(teach)
new_class_teach = json.dumps(teach, ensure_ascii=False)
with open('Teachers_id.json','w') as teach1:
    teach1.write(new_class_teach)
    

# 3.4
print('3.4')
del_stud_name = 'Егоров Дмитрий Васильевич'
del_stud_list = del_stud_name.split(' ')
# print(del_stud_list)
for el in stud:
    if del_stud_list[0] == el['surname'] and del_stud_list[1] == el['name']:
        # print(el)
        stud.remove(el)
        all_st_new=json.dumps(stud, ensure_ascii=False)
        with open('Students_id.json','w') as stud1:
            stud1.write(all_st_new)
            

# 3.5
print('3.5')
del_class = '6 А'
for el in stud[:]:
    if el['class'] == del_class:
        print(el)
        stud.remove(el)
new_class=json.dumps(stud, ensure_ascii=False)
with open('Students_id.json','w') as stud1:
    stud1.write(new_class)
    

# 3.6
print('3.6')
del_teach_name = 'Егоров Дмитрий Васильевич'
del_teach_list = del_teach_name.split(' ')
# print(del_stud_list)
for el in teach[:]:
    if del_teach_list[0] == el['surname'] and del_teach_list[1] == el['name']:
        # print(el)
        teach.remove(el)
        # print(teach)
        new_teach=json.dumps(teach, ensure_ascii=False)
        with open('Teachers_id.json','w') as teach1:
            teach1.write(new_teach)
            

# 3.7
print('3.7')
school = '67 школа'
for el in teach[:]:
    if school == el['school']:
        teach.remove(el)
        new_teach=json.dumps(teach, ensure_ascii=False)
        with open('Teachers_id.json','w') as teach1:
            teach1.write(new_teach)
            
# 3.8
print('3.8')
teach_class = '6 Б'
teach_name = 'Вышкин Владимир Сергеевич'
teach_name = teach_name.split(' ')
print(teach_name)
for el in teach:
    if el['surname'] == teach_name[0] and el['name'] == teach_name[1]:
        teach_class_list = el['class']
for el in teach_class_list[:]:
    if teach_class == el:
        teach_class_list.remove(el)
for el in teach:
    if el['surname'] == teach_name[0] and el['name'] == teach_name[1]:
        el['class'] = teach_class_list
new_class_list=json.dumps(teach, ensure_ascii=False)
with open('Teachers_id.json','w') as teach1:
    teach1.write(new_class_list)
    

# 4.2
print('4.2')
surname='Кузин'
id_list=[]
for el in stud:
    if el['surname']==surname:
        id_list.append(el['id'])
for el in id_list:
    for l in stud:
        if el==l['id']:
            print(l['surname'],l['name'],l['middle_name'])

# 4.3
print('4.3')
a=search(stud,name='Кузин',class_room='8 Д')
print(a)

# 4.4
print('4.4')
teachers_class='7 В'
for el in teach:
    for l in el['class']:
        if teachers_class==l:
            print(el['id'])

