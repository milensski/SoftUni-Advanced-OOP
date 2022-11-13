import datetime


class DVD:

    def __init__(self, name, d_id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = d_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, d_id, name, date, age_restriction):
        day,month_integer,year = [int(x) for x in date.split('.')]

        month = datetime.date(year, month_integer, day).strftime('%B')
        return cls(name,d_id,year,month,age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}'





