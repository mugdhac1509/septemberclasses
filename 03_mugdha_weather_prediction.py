weather = (1,0,0,0,1,0,0)
sunny = 0
rain = 0
for i in range(0,7):
    if weather [i]==0:
        rain = rain+1
    else:
        sunny = sunny+1
if sunny > rain:
    print("Good Weather!")
else:
    print("Bad Weather.")