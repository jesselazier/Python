#老方法
# file=open('practice_for_R&W_file.txt')
# text=file.read()
# print(text)
# file.close()

#python3.0的打开文件方式，好处是不用close（默认为'r'，所以可以不用写）
with open('practice_for_R&W_file.txt') as f:
    f=f.read()
    print(f)

#写入 'w'是覆盖，'a'是续写 'r'是读，  默认为'r'，所以可以不用写
with open('practice_for_R&W_file.txt','w') as f:
    f.write('hello world')