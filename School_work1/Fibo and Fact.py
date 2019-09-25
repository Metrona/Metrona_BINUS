def fibonacci(number):
    if(number > 1):
        return fibonacci(number-1) + fibonacci(number-2)
    else:
        return number

print (fibonacci(10))
#%%
def factorial(number):
    if(number > 1):
        return number * factorial(number-1)
    else:
        return number
    
print (factorial(4))