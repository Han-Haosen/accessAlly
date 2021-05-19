duration = input()
def spot_arithmatic(time):
    strTime = str(time)
    diff = int(strTime[1]) - int(strTime[0])
    for i in range(2,len(strTime)):
        if int(strTime[i]) - int(strTime[i - 1]) != diff:
            return False
    return True
counter = 0
halfaday = 720
halfadaycounter = 31
hours = [12,1,2,3,4,5,6,7,8,9,10,11]
minutes = ["00","01","02","03","04","05","06","07","08","09"]
minutes.extend(range(10,60))
duration += 1
numberofhalfdays = duration / 720
duration = duration % 720 
for i in hours:
    for j in minutes:
        duration -= 1
        if(duration < 0):
            break
        inputStr = str(i) + str(j)
        if(spot_arithmatic(inputStr)):
            counter += 1
counter = counter + (numberofhalfdays * halfadaycounter)
print(counter)
