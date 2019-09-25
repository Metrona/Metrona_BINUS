#%%
def count(string):
    lit = {}
    for x in z:
        if x in lit:
            lit[x] += 1
        else:
            lit[x] = 1
    for data in lit:
        print(f"{data} = {lit[data]}")
z = input("type here:")
print(count(z))
        
