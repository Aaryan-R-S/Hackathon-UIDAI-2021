import json

class pinCode:
    def __init__(self, pincode,district,state):
        self.pincode = pincode
        self.state = state
        self.district = district

def merge(arr, list, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    Lp = [0]* (n1)
    Rp = [0]* (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
        Lp[i] = list[l+i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        Rp[j] = list[m + 1 +j]
    i = 0
    j = 0
    k = l 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            list[k] = Lp[i]
            i += 1
        else:
            arr[k] = R[j]
            list[k] = Rp[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        list[k] = Lp[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        list[k] = Rp[j]
        j += 1
        k += 1

 
def mergeSort(arr, list, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, list, l, m)
        mergeSort(arr, list, m+1, r)
        merge(arr, list, l, m, r)


data = open("Data\\Pincode.csv","r")
lines = data.readlines()
data.close()
Pins = []                 ## 19252 unique pincodes
list = []
for line in lines[1:]:
    temp = line.split(",")
    pincode = int(temp[4])
    if (pincode not in Pins):
        Pins.append(pincode)
        p1 = pinCode(pincode, temp[7],temp[8])
        list.append(p1)
print(len(Pins))
print(len(list))
mergeSort(Pins,list,0,len(Pins)-1)
print(Pins[:10])
for i in list[:10]:
    print(i.state,end=", ")
data = open("Data\\PincodeModified.csv","w")
data.write("Pincode,District,State\n")
for i in list:
    data.write(str(i.pincode)+","+i.district+","+i.state)
data.close()