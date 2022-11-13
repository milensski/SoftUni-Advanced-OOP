class DVD:

    def __init__(self, name, d_id,  creation_year, creation_month,age_restriction):
        self.name = name
        self.id = d_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, d_id, name,  date, age_restriction):
        
