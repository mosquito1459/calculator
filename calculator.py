print('Now enter your number')
a = int(input('ตัวแรก: '))
c = int(input('ตัวแปร: '))
print('ตอนนี่ คุณใส่เลขมาแล้วคือ',a,c)
loop = 'true'
while (loop == 'true'):
    print('กรุณาใส่ + - * /')
    b = input()
    if ('+' == b):
        print('ผลลัพท์คือ',a+c)
        input("กด Enter เพื่อปิดโปรแกรม")
        break
    if ('-' == b):
        print('ผลลัพท์คือ',a-c)
        input("กด Enter เพื่อปิดโปรแกรม")
        break
    if ('*' == b):
        print('ผลลัพท์คือ',a*c)
        input("กด Enter เพื่อปิดโปรแกรม")
        break
    if ('/' == b):
        print('ผลลัพท์คือ',a/c)
        input("กด Enter เพื่อปิดโปรแกรม")
        break
    else:
        print('คุณใส่เครื่องหมายผิด')