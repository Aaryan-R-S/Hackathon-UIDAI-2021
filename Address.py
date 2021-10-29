class Address:
    def get_house_number():
        return self.house
    def get_street():
        return self.street
    def get_area():
        return self.area
    def get_landmark():
        return self.landmark
    def get_city():
        return self.city
    def get_pincode():
        return self.pincode
    def get_subdistrict():
        return self.subdistrict
    def get_district():
        return self.district
    def get_state():
        return self.state
    def get_details():
        return self.__dict__
    def set_house_number(house):
        self.house=house
    def set_street(street):
        self.street=street
    def set_area(area):
        self.area=area
    def set_landmark(landmark):
        self.landmark=landmark
    def set_city(city):
        self.city=city
    def set_pincode(pincode):
        self.pincode=pincode
    def set_subdistrict(subdistrict):
        self.subdistrict=subdistrict
    def set_district(district):
        self.district=district
    def set_state(state):
        self.state=state
