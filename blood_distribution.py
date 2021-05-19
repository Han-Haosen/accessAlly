import sys 
inputSys = []
for i in sys.stdin:
    inputSys.append(i.rstrip())
# press command D to finish inputting
blooddonor = inputSys[0]
bloodreceiver = inputSys[1]
blooddonor = blooddonor.split()
bloodreceiver = bloodreceiver.split()
intdonor = []
intreceiver = []
for i in blooddonor:
    intdonor.append(int(i))
for j in bloodreceiver:
    intreceiver.append(int(j))
patientcount = 0
for i in range(8):
    while True:
        if(intreceiver[i] <= 0 or intdonor[i] <= 0):
            break
        if(intdonor[i] > 0):
            intreceiver[i] -= 1
            intdonor[i] -= 1
            patientcount += 1
            continue
for i in range(0,8,2):
    while True:
        if intreceiver[i] <= 0:
            break
        if intdonor[0] > 0:
            intreceiver[i] -= 1
            intdonor[0] -= 1
            patientcount += 1
            continue
        if i == 6:
            if intdonor[2] > 0:
                intreceiver[i] -= 1
                intdonor[2] -= 1
                patientcount += 1
                continue
            if intdonor[4] > 0:
                intreceiver[i] -= 1
                intdonor[4] -= 1
                patientcount += 1
                continue
            break
        break
for i in range(1,8,2):
    while True:
        if intreceiver[i] <= 0:
            break
        if intdonor[0] > 0:
            intreceiver[i] -= 1
            intdonor[0] -= 1
            patientcount += 1
            continue
        if intdonor[1] > 0:
            intreceiver[i] -= 1
            intdonor[1] -= 1
            patientcount += 1
            continue
        if i == 7:
            for j in range(8):
                if(intdonor[j] > 0):
                    intreceiver[i] -= 1
                    intdonor[j] -= 1
                    patientcount += 1
                    continue
            break
        break
print(patientcount)

