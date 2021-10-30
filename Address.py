class Address:
    def get_address_details():
        return self.address_details
    def get_VTC():
        return self.VTC
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
    def set_address_details(address_details):
        self.address_details=address_details
    def set_VTC(city):
        self.VTC=city
    def set_pincode(pincode):
        self.pincode=pincode
    def set_subdistrict(subdistrict):
        self.subdistrict=subdistrict
    def set_district(district):
        self.district=district
    def set_state(state):
        self.state=state
