class Recruiter:
    def __init__(self, name, company, email, charge, locations = [], skills = [], languages = [], schedule = {}):
        self.name = name
        self.company = company
        self.email = email
        self.charge = charge
        self.locations = locations
        self.skills = skills
        self.languages = languages
        self.schedule = schedule