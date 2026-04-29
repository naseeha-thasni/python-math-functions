def exponention(num,pow):
    return num**pow
def squareroot(num):
    return num**0.5
def factorial (num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

print("exponention\n-----------")
n=int(input('enter number:'))
power=int(input('enter power:'))
exponention=exponention(n,power)
print('exponention =',exponention)
print('squareroot\n----------')
no=int(input('enter number'))
squareroot=squareroot(no)
print('squareroot =',squareroot)
print('factorial \n---------')
num=int(input('enter a number'))
factorial=factorial(num)
print('factorial =',factorial)