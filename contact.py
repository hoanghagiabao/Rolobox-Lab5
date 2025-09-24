class contact:
    def __init__(self, fn, ln, ph, addr, city, zip):
        """
        INPUT:
            fn   (str): first name
            ln   (str): last name
            ph   (str): phone number
            addr (str): street address
            city (str): city
            zip  (str): zip code
        OUTPUT:
            None.
        """
        self.first_name = fn
        self.last_name = ln
        self.phone = ph
        self.address = addr
        self.city = city
        self.zip = zip
    # Less-than operator for sorting
    def __lt__(self, other):  
        if self.last_name == other.last_name:
            if self.first_name == other.first_name:
                return self.first_name < other.first_name
        return self.last_name < other.last_name
    # String representation for display
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone}, {self.address}, {self.city}, {self.zip}"
    # Official representation for saving
    def __repr__(self):
        return f"contact({self.first_name}, {self.last_name}, {self.phone}, {self.address}, {self.city}, {self.zip})"
