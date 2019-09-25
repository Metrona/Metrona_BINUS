#%%
W1 = "micheal"
W2 = "lemicha"
x = 0
if(len(W1) == len(W2)):
    for element in W1:
        if (element in W2):
            x += 1
            W2.replace(element, "")
if (x == len(W1)):
    print(True)
else:
    print(False)
    
#%%
def check(W1, W2)
    if(sorted(W1) == sorted(W2)):
        print(True)
    else:
        print(False)
#%%