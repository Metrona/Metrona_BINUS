str_tocheck = input("Enter your string: ")

def ispalindrome(input_str):
    return (input_str == input_str[::-1])

print (ispalindrome(str_tocheck))
#%%
def reverse(input_str):
    return (input_str[::-1])
#%%
def even(lit):
    x = 0
    for num in lit:
        if (num%2 == 0):
            x += num
    print(x)
