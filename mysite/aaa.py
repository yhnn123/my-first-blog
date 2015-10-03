# encoding='utf-8'

a = 'sonja'

if a == 'soonja':
    print("a")
elif a == 'sonja':
    print("b")
else:
    print("c")


def hi(name):
    if a == 'soonja':
        print("a")
    elif a == 'sonja':
        print("b")
    else:
        print("c")

hi('sonja')


def hi(name):
    print('Hi ' + name + '!')

girls = ['aaa', 'bbb', 'ccc', 'ddd']
for name in girls:
    hi(name)
    print('next girl')