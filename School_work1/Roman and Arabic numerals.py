#%%
def convertnum(romnum):
    x = 0
    for num in romnum:
        if(num == "X"):
            x += 10
        elif(num == "V"):
            x += 5        
        elif(num == "I"):
            if(romnum[-1] == "V" or romnum[-1] == "X"):
                x -= 1
            else:
                x += 1
        else:
            x = "invalid"
    return print(x)
    
#%%
def convertrom(num):
    y = ""
    if(num >= 10):
        y += int(num/10)*"X"
    if(9 > num%10 >= 5):
        y += "V"
    if(num%10 == 9):
        y += "IX"
    if(num%10 == 4):
        y += "IV"
    if(num%5 != 0 and num%5 != 4):
        y += num%5*"I" 
    return print(y)