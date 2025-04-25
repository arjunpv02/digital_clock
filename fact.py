#  program to find factorial 

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(4))