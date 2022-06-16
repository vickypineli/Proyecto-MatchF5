class Recruiter:
    def __init__(
        self,
        id,
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
        self.id = id
        self.name = name
        self.company = company
        self.email = email
        self.linkedin = linkedin
        self.charge = charge
        self.locations = locations
        self.skills = skills
        self.languages = languages
        self.schedule = schedule

    def location_dict(self, posible_locations):
        for location in self.locations:
            posible_locations[location] = "x"
        return posible_locations

    def skills_dict(self, posible_skills):
        for skill in self.skills:
            posible_skills[skill] = "x"
        return posible_skills
