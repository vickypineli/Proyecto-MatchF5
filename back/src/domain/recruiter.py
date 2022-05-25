class Recruiter:
    def __init__(
        self,
        name,
        company,
        charge,
        email="-",
        linkedin="-",
        locations=[],
        skills=[],
        languages=[],
        schedule={},
    ):
        self.name = name
        self.company = company
        self.email = email
        self.linkedin = linkedin
        self.charge = charge
        self.locations = locations
        self.skills = skills
        self.languages = languages
        self.schedule = schedule
