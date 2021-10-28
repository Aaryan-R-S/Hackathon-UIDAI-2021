class address:
    def __init__(self,house,street,area,landmark,city,pincode,subdistrict,district,state):
        if type(house)==int and type(street)==str and type(area)==str and type(landmark)==str and type(city)==str and type(pincode)==int and type(subdistrict)==str and type(district)==str:
            self.house=house #this is an integer denoting the house or apartment number 
            self.street=street #this is a string denoting the name of street,road,lane
            self.area=area #this is a string denoting the area/locality/sector
            self.landmark=landmark #this is a string denoting the landmark
            self.city=city #this is a string denoting the village/town/city
            self.pincode=pincode #this is a integer denoting the pincode
            self.subdistrict=subdistrict #this is a string denoting the sub-district
            self.district=district #this is a string denoting the district
            self.state=state #this is a string denoting the state
        else:
            print("invalid values for arguments")
    def gethousenumber():
        return self.house
    def getstreet():
        return self.street
    def getarea():
        return self.area
    def getlandmark():
        return self.landmark
    def getcity():
        return self.city
    def getpincode():
        return self.pincode
    def getsubdistrict():
        return self.subdistrict
    def getdistrict():
        return self.district
    def getdetails():
        return self.__dict__
    
if __name__=="__main__":
    
    
