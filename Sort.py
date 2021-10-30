import json

States = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar","Delhi","Jammu and Kashmir"]

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid]["Pincode"] == x:
            return mid
        elif arr[mid]["Pincode"] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1

def extractPin(data):
    #data=""
    pincode = ""
    num=0
    for i in range(len(data)-1,-1,-1):
        if (data[i].isnumeric()):
            num+=1
            pincode+=data[i]
            if (num==6):
                break
        else:
            num=0
            pincode=""
    return pincode[::-1]

def extractState(data, expected, pincode):
    lst = data.split(",")
    lst = list(i.lower() for i in lst if i!="")
    selected=""
    if expected!="":
        for i in lst[::-1]:
            temp=i.lower().replace(pincode,"").replace(expected.lower(),"")
            chars=0
            for c in temp:
                if c.isalpha():
                    chars+=1
            if chars<3:
                selected = i
                break
        if selected!="":
            lst.remove(selected)
            return (lst,expected)
    for i in lst[::-1]:
        if (selected!=""):
            break
        temp=i.lower().replace(pincode,"")
        for state in States:
            temp2 = temp.replace(state.lower(),"")
            chars=0
            for c in temp2:
                if c.isalpha():
                    chars+=1
            if chars<3:
                selected=i
                break
    if selected=="":
        return (lst,expected)
    else:
        lst.remove(selected)
        return (lst,selected)

def extractDistrict(lst,expected,state,pincode):
    dataJSON = ""
    with open("Data\\Districts.json","r") as f:
        dataJSON = json.loads(f.read())
    if (state!=""):
        districts = list(i["districts"] for i in dataJSON["states"] if state.lower() in i["state"].lower())[0]
        for dist in districts:
            if "(" in dist:
                districts.remove(dist)
                districts.extend(list(i.replace(")","") for i in dist.split("(")))
        print(districts)
    selected=""
    if expected!="":
        for i in lst[::-1]:
            temp=i.lower().replace(pincode,"").replace(expected.lower(),"")
            chars=0
            for c in temp:
                if c.isalpha():
                    chars+=1
            if chars<3:
                selected = i
                break
        if selected!="":
            lst.remove(selected)
            return (lst,expected)
    for i in lst[::-1]:
        if (selected!=""):
            break
        temp=i.lower().replace(pincode,"")
        for dist in districts:
            temp2 = temp.replace(dist.lower(),"")
            chars=0
            for c in temp2:
                if c.isalpha():
                    chars+=1
            if chars<3:
                selected=i
                break
    if selected=="":
        selected = expected
    else:
        lst.remove(selected)
        return (lst,selected)

    

def beautify(addr):
    pincode = extractPin(addr)
    print(pincode)
    addr.replace(pincode,"")
    if pincode=="":
        pincode="0"
    dataString = ""
    with open("Data\\PincodeModified.json","r") as f:
        dataString = f.read()
    dataJSON = json.loads(dataString)
    index = binary_search(dataJSON,0,len(dataJSON)-1,int(pincode))
    expectedState=""
    expectedDistrict=""
    if (index!=-1):
        expectedState = dataJSON[index]["State"]
        expectedDistrict =dataJSON[index]["District"]
    (lst, state)=extractState(addr, expectedState, pincode)
    print(lst,state)
    (lst, district)=extractDistrict(lst,expectedDistrict,state,pincode)
    print(lst, district)


if __name__=="__main__":

   beautify("B-616, Sangam Vihar, New Delhi,Delhi, Near Saket 1001")