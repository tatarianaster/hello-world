# 列表
students = ['杜莱叮', '陈智仪', '赖敏','蒋欣','刘飞']
#增
print(students.append('沈凯'))
print(students.insert(0,'王崇茂'))
#删
print(students.pop(3))
del students[1]
#改
students[1:3] = ['刘晨','李海']
#查
print(students[:])
students.sort(reverse=True)
print(students)
#列表生成式
sum1 = [n*(n-1) for n in range(7)]
print(sum1)

# 元组
id_number = (1000, 1001, 1002, 1003, 1004)
#查
print(id_number[1])
age_height_standard = ([16,172],[15,165],[14,160],[13,155])
#元组内部修改
age_height_standard[0][0] = 17
print(age_height_standard)

# 字典
classroom = {'room1':'A1', 'room2':'A2', 'room3':'A3'}
#dict（）使用
c = dict([('room1','A1'), ('room2','A2'), ('room3','A3')])
print(c == classroom)
#增
classroom['room4'] = 'A4'
print(classroom)
#删
del classroom['room1']
print(classroom)
#改
classroom['room2']='B2'
print(classroom)
#查
print(classroom['room2'])
print('room2' in classroom)