'''List Comprehension 列表解析式
 List 生成新 List的过程就是 List Conprehension 的一种'''


'''我的需求： 从0-10的数字分别乘以2，然后放到新的列表（list）里'''

#传统用法
newList=[]
for i in range(11):
    newList.append(i*2)
print(newList)#结果[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#List Comprehension 列表解析式
print([i*2 for i in range(11)])


list=['小明','小红','李四','张三']
emptyList=[]
for name in list:
    if name.startswith('小'):
        emptyList.append(name)
        print(emptyList)

print([name for name in list if name.startswith('小')])