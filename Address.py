class Address:
    # --------------------- Structure of the Address class starts ----------------------------
    # If NOT in UT:
    # (*)House/Building/Apartment, 
    # Street/Road/Lane,
    # (*)Area/Locality/Sector,
    # Landmark,
    # (*)Village/Town/City,         (if it is district also, then remove it)
    # Sub District, 
    # (*)District, 
    # (*)State - 
    # (*)Pincode
    
    # If in UT:
    # (*)House/Building/Apartment, 
    # Street/Road/Lane,
    # (*)Area/Locality/Sector,
    # Landmark,
    # Village/Town/City,            (no use)
    # Sub District,                 (no use)
    # (*)District,              
    # (*)State -                    (city itself)
    # (*)Pincode

    # --------------------- attributes of the Address class object ----------------------------    
    _localAddr = []         # House/Building/Apartment, Street/Road/Lane, Area/Locality/Sector, Landmark
    _vtc = ""               # Village/Town/City
    _subNdistrict = []      # Subdistrict and district
    _state = ""             # State/UT
    _pincode = ""           # Pincode
    
    # --------------------- getter methods ----------------------------    
    def get_localAddr(self):
        return self._localAddr
    
    def get_vtc(self):
        return self._vtc
    
    def get_subNdistrict(self):
        return self._subNdistrict

    def get_state(self):
        return self._state

    def get_pincode(self):
        return self._pincode

    def get_all(self):
        return self._localAddr + [self. _vtc] + self._subNdistrict + [self._state, self._pincode]

    # --------------------- settor methods ----------------------------    
    def set_localAddr(self, params):
        self._localAddr = params

    def set_vtc(self, params):
        self._vtc = params

    def set_subNdistrict(self, params):
        self._subNdistrict = params

    def set_state(self, params):
        self._state = params

    def set_pincode(self, params):
        self._pincode = params
