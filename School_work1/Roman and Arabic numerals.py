#%%
def convertnum(romnum):
    x = 0
    for num in romnum:
        if(num == "X"):
            x += 10
        elif(num == "V"):
            x += 5        
        elif(num == "I"):
            if(romnum == "IV" or romnum == "XIV" or romnum == "IX"):
                x -= 1
            else:
                x += 1
        else:
            x = "invalid"
    return print(x)
    
#%%
def convertrom(num):
    y = ""
    if(len(str(num)) == 2):
        y += int(num/10)*"X"
    if(9 > num >= 5 or 19 > num >= 15):
        y += "V"
    if("9" in str(num)):
        y += "IX"
    if("4" in str(num)):
        y += "IV"
    if(4 > num >= 1 or 9 > num >= 6 or 14 > num >= 11 or 19 > num >= 16):
        y += num%5*"I" 
    return print(y)