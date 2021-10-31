from Address import Address

def declutter(allCities, allDistricts, allStates, myAddr):
    # --------------------- Split the address by commas ------------------------
    newAddr = Address()
    myAddr = [x.strip() for x in myAddr.split(',')]
    myAddr = [x for x in myAddr if x != '']
    
    # --------------------- Split the address by hyphen ------------------------
    myAddrT = []
    for x in myAddr:
        if '-' in x:
            curr = [i.strip() for i in x.split('-')]
            curr = [i for i in curr if i != '']
            for j in curr:
                myAddrT.append(j)
        else:
            myAddrT.append(x)
    myAddr = myAddrT.copy()

    # --------------------- Search and validate State ------------------------
    state_idx = -1
    for i in range(len(myAddr)-1,-1,-1):
        if myAddr[i] in allStates:
            state_idx = i
            break
    if(state_idx==-1):
        return "Missing the required argument State in the address", -1
    
    # --------------------- Search and validate Pincode ------------------------
    pin_idx = -1
    for i in range(len(myAddr)-1,-1,-1):
        if myAddr[i].isnumeric() and len(myAddr[i])==6:
            pin_idx = i
            break
    if(pin_idx==-1):
        return "Missing the required argument 6-digit Pincode in the address", -1
    
    # --------------------- Search and validate City/Town ------------------------
    city_idx = -1
    for i in range(len(myAddr)-1, -1, -1):
        if myAddr[i] in allCities:
            city_idx = i
            break
    
    if city_idx == state_idx or (city_idx!=-1 and myAddr[city_idx]==myAddr[state_idx]):
        city_idx = -1
    
    # --------------------- Search and validate District ------------------------
    dist_idx = -1
    if city_idx == -1:
        find_idx = -1
        for i in range(len(allDistricts["states"])):
            if allDistricts["states"][i]["state"] == myAddr[state_idx]:
                find_idx = i
                break
        if find_idx == -1:
            return "Missing the required argument 'state' from the address", -1
        for i in range(len(myAddr)-1,-1,-1):
            if myAddr[i] in allDistricts["states"][find_idx]["districts"]:
                dist_idx = i
                break
        if dist_idx == state_idx:
            dist_idx = -1
        if(dist_idx==-1):
            return "Missing the required argument district, city, village or town from the address", -1
    
    # --------------------- Set the fields of our Address class object ------------------------
    newAddr.set_state(myAddr[state_idx])
    newAddr.set_pincode(myAddr[pin_idx])
    
    if city_idx!=-1:
        newAddr.set_vtc(myAddr[city_idx])
        newAddr.set_localAddr(myAddr[:city_idx])
        if (state_idx-city_idx) >= 2:
            newAddr.set_subNdistrict(myAddr[(city_idx+1):state_idx])
    else:
        newAddr.set_localAddr(myAddr[:dist_idx])
        newAddr.set_subNdistrict(myAddr[dist_idx:state_idx])

    # --------------------- Remove the repetitive constituents in local address ------------------------
    temp_l = []
    for i in range(len(newAddr.get_localAddr())):
        if newAddr.get_localAddr()[i] not in newAddr.get_localAddr()[i+1:]:
            temp_l.append(newAddr.get_localAddr()[i])
    newAddr._localAddr = temp_l.copy()
    for i in range(len(newAddr.get_localAddr())):
        if (newAddr.get_localAddr()[i] == newAddr.get_pincode()) or (newAddr.get_localAddr()[i] == newAddr.get_state()) or (newAddr.get_localAddr()[i] == newAddr.get_vtc()):
            newAddr._localAddr[i] = ''
    newAddr._localAddr = [t for t in newAddr.get_localAddr() if t!='']
            
    # --------------------- Remove the repetitive constituents in district/sub-district/state/city ------------------------
    temp_l = []
    for i in range(len(newAddr.get_subNdistrict())):
        if newAddr.get_subNdistrict()[i] not in newAddr.get_subNdistrict()[i+1:]:
            temp_l.append(newAddr.get_subNdistrict()[i])
    newAddr._subNdistrict = temp_l.copy()
    for i in range(len(newAddr.get_subNdistrict())):
        if (newAddr.get_subNdistrict()[i] == newAddr.get_pincode()) or (newAddr.get_subNdistrict()[i] == newAddr.get_state()) or (newAddr.get_subNdistrict()[i] == newAddr.get_vtc()):
            newAddr._subNdistrict[i] = ''
    newAddr._subNdistrict = [t for t in newAddr.get_subNdistrict() if t!='']

    # --------------------- Getting the final address ready ------------------------
    formatted_addr = ""
    formatted_addr += ", ".join(newAddr.get_localAddr())
    if newAddr.get_vtc() != '':
        formatted_addr += ", " + newAddr.get_vtc()
    if newAddr.get_subNdistrict()!= []:
        formatted_addr += ", " + ", ".join(newAddr.get_subNdistrict())
    formatted_addr += ", " + newAddr.get_state()
    formatted_addr += " - " + newAddr.get_pincode()

    # --------------------- Return the verdict and final formatted address  ------------------------
    # return newAddr.__dict__, 0
    return formatted_addr, 0