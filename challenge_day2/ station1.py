
def fibonacci (n):
    if n <=1 :
        print(f'{n} is a wrong number, enter number bigger than 1')
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) 


user_number = int(input('enter a number:'))
print(f'{user_number} is {fibonacci(user_number)} number in fibonacci sequance')


