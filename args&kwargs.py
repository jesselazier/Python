
'''*args,**kwargs'''

def m1(*args,**kwargs):
    print('the type of args is:',type(args))
    print('the type of kwargs is:',type(kwargs))
'===================================================='
#*args
def add(*args):
    print(sum(args))

add(1,4)
'===================================================='

'===================================================='
#**kwargs
def someone(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)

someone(name='jesse',age='31',height='175')
'===================================================='